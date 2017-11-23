from rest_framework import serializers

from . import models
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'image',
			'listing'
		)
		model = models.ListingImage

class ListingSerializer(serializers.ModelSerializer):
	listingimages = ImageSerializer(read_only=True, many=True)
	added_by_user = serializers.ReadOnlyField(source='added_by.email')

	class Meta:
		extra_kwargs = {
			'description': {'write_only': True},
			'features': {'write_only': True},
			'added_by': {'write_only': True},
		}
		fields = (
			'id',
			'name',
			'address',
			'town',
			'state',
			'status',
			'listing_type',
			'bedroom',
			'price',
			'listingimages',
			'added_by',
			'added_by_user',
			'created_at'
		)
		model = models.Listing


class ListingDetailSerializer(serializers.ModelSerializer):
	listingimages = ImageSerializer(read_only=True, many=True)
	added_by_user = serializers.ReadOnlyField(source='added_by.email')

	class Meta:
		fields = (
			'id',
			'name',
			'address',
			'town',
			'state',
			'status',
			'listing_type',
			'bedroom',
			'price',
			'listingimages',
			'description',
			'features',
			'added_by_user',
			'created_at'
		)
		model = models.Listing

