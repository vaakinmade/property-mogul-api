from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

#from rest_framework import generics

class ListCreateListing(APIView):
	def get(self, request, format=None):
		listings = models.Listing.objects.all()
		serializer = serializers.ListingSerializer(listings, many=True)
		return Response(serializer.data)

