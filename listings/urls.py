from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreateListing.as_view(), name="listing_list"),
	url(r'^(?P<pk>\d+)$', views.RetrieveUpdateDestroyListing.as_view(),
		name='listing_detail'),
	url(r'^images$', views.ListCreateImage.as_view(), name="image_list"),
	url(r'^images/(?P<pk>\d+)$', views.RetrieveUpdateDestroyImage.as_view(), name="image_view"),
	url(r'^search$', views.SearchListView.as_view(), name='search'),
	url(r'^rent$', views.RentListView.as_view(), name='rent'),	
]