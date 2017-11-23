import functools
import operator
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

#from django.core.serializers import serialize

from . import models
from . import serializers


class ListCreateListing(generics.ListCreateAPIView):
	queryset = models.Listing.objects.all()
	serializer_class = serializers.ListingSerializer


class RetrieveUpdateDestroyListing(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Listing.objects.all()
	serializer_class = serializers.ListingDetailSerializer


class RetrieveUpdateDestroyImage(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.ListingImage.objects.all()
	serializer_class = serializers.ImageSerializer


class ListCreateImage(generics.ListCreateAPIView):
	queryset = models.ListingImage.objects.all()
	serializer_class = serializers.ImageSerializer


class SearchListView(generics.ListAPIView):
	serializer_class = serializers.ListingSerializer

	def get_queryset(self):
		values_dict = {
			'listing_type__iexact': self.request.GET.get('listing_type', None),
			'status__iexact': self.request.GET.get('status', None),
			'bedroom': self.request.GET.get('bedroom', None),
			'price__lte': self.request.GET.get('max_price', "").replace(" ", ""),
			'price__gte': self.request.GET.get('min_price', "").replace(" ", "")
		}

		input_list = ["", None, "Any Bed", "Max.", "Any Type", "Any Status"]
		arguments = {k:v for k,v in values_dict.items() if v not in input_list}
		location = self.request.GET.get('location', 'lagos')
		location_list = [SearchQuery(term) for term in location.split()]

		query = functools.reduce(operator.or_, location_list)
		vector = SearchVector('name', 'address', 'town', 'state')
		rank_parameters = SearchRank(vector, query)

		queryset = models.Listing.objects.annotate(
			search=vector, rank=rank_parameters
			).filter(search=query, **arguments).order_by('-rank')
		return queryset
