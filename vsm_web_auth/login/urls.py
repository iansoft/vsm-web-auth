from django.conf.urls import include, url
from login.views import login
urlpatterns = [
    url(r'^$', login, name="login")
]