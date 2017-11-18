from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreateListing.as_view(), name="listing_list"),
	url(r'^(?P<pk>\d+)/$', views.RetrieveUpdateDestroyListing.as_view(),
		name='listing_detail'),
	
]