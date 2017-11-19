from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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

	def get_queryset(self):
		location = self.request.GET.get('location', None)
		listing_type = self.request.GET.get('listing_type', None)
		bedroom = self.request.GET.get('bedroom', None)
		bathroom = self.request.GET.get('bathroom', None)
		status = self.request.GET.get('status', None)
		print ("location", location)

		queryset = models.Listing.objects.filter(Q(town=location,
													listing_type=listing_type,
													bedroom=bedroom,
													bathroom=bathroom) |
												Q(state=location,
													listing_type=listing_type,
													bedroom=bedroom,
													bathroom=bathroom)
												)
		return queryset

	def get_serializer_class(self):
		response = serializers.serialize("json", self.get_queryset())
		return Response(response)



