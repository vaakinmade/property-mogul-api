from rest_framework import serializers

from . import models


class ListingSerializer(serializers.ModelSerializer):
	class Meta:
		extra_kwargs = {
			'added_by': {'write_only': True}
		}
		fields = (
			'name',
			'address',
			'town',
			'state',
			'status',
			'listing_type',
			'bedroom',
			'bathroom',
			'added_by',
			'created_at'
		)
		model = models.Listing

