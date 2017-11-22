from rest_framework import serializers

from . import models


class ListingSerializer(serializers.ModelSerializer):
	class Meta:
		extra_kwargs = {
			'added_by': {'write_only': True},
			'description': {'write_only': True},
			'features': {'write_only': True}
		}
		fields = (
			'name',
			'address',
			'town',
			'state',
			'status',
			'listing_type',
			'bedroom',
			'price',
			'added_by',
		)
		model = models.Listing


class ListingDetailSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'name',
			'address',
			'town',
			'state',
			'status',
			'listing_type',
			'bedroom',
			'price',
			'description',
			'features',
			'added_by',
			'created_at'
		)
		model = models.Listing


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'image',
			'listing',
			'created_at'
		)
		model = models.ListingImage


