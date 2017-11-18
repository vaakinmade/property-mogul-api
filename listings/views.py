from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers

#from rest_framework import generics

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

