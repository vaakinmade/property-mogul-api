from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Listing(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=225)
	address = models.TextField()
	town = models.CharField(max_length=225)
	state = models.CharField(max_length=225)
	bedroom = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	added_by = models.ForeignKey(User)
	description = models.TextField(default="")
	features = models.TextField(default="")

	LISTING_STATUS = (
	    ('for sale','For Sale'),
	    ('for rent', 'For Rent'),
	)

	LISTING_TYPE = (
    	('apartments','Apartments'),
    	('houses', 'Houses'),
    	('studios', 'Studios'),
    	('commercial', 'Commercial'),
	)
	
	status = models.CharField(max_length=25,
								choices=LISTING_STATUS,
								default='Property Status')
	listing_type = models.CharField(max_length=25,
									choices=LISTING_TYPE,
									default='Property Type')
	
	def __str__(self):
		return self.name


class Image(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	listing = models.ForeignKey(Listing)
	image = models.ImageField(upload_to='images/mogul', default='pic_folder/None/no-img.jpg')

	ORDER = []
	for i in range(1,7):
		values = i, i
		ORDER.append(values)
	
	ordering = models.IntegerField(
        choices=ORDER,
        default=0,
    )

	def __str__(self):
		return str(self.listing) + " 's Image"