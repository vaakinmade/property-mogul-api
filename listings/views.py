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
	queryset = models.Image.objects.all()
	serializer_class = serializers.ImageSerializer


class ListCreateImage(generics.ListCreateAPIView):
	queryset = models.Image.objects.all()
	serializer_class = serializers.ImageSerializer


class SearchListView(generics.ListAPIView):
	serializer_class = serializers.ListingSerializer

	def get_queryset(self):
		location = self.request.GET.get('location')
		listing_type = self.request.GET.get('listing_type', 'listing_type')
		bedroom = self.request.GET.get('bedroom', 'bedroom')
		min_price = self.request.GET.get('min_price', 'min_price')
		max_price = self.request.GET.get('max_price', 'max_price')
		status = self.request.GET.get('status')
		
		location = [SearchQuery(term) for term in location.split()]
		query = functools.reduce(operator.or_, location)
		vector = SearchVector('name', 'address', 'town', 'state')
		rank_parameters = SearchRank(vector, query)
	
		queryset = models.Listing.objects.annotate(
			search=vector, rank=rank_parameters
			).filter(search=query,
					status__iexact=status,
					listing_type__iexact=listing_type
					).order_by('-rank')
		print("queryset", queryset)
		return queryset



