from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Listing(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=225)
	address = models.TextField()
	town = models.CharField(max_length=225)
	state = models.CharField(max_length=225)
	bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	added_by = models.ForeignKey(User)
	status = models.CharField(max_length=225)
	listing_type = models.CharField(max_length=225)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
   	    return reverse('listings:detail', kwargs={'pk': self.pk})