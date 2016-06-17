from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Login
    url(r'^login/', include('login.urls')),
    # url(r'^auth/', include('openstack_auth.urls')),
    # homepage
    url(r'^$', include('dashboard.urls')),
    url(r'^home/$', include('dashboard.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
]
