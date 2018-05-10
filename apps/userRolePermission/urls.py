from django.conf.urls import url

from . import views

# Routers provide an easy way of automatically determining the URL conf.


urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
]