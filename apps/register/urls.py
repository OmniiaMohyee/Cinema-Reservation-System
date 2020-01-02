from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^customer$', views.customer),
    url(r'^admin$', views.admin),
    url(r'^add_screen$', views.add_screen),
    url(r'^add_movie$', views.add_movie),
    url(r'^add_screen_time$', views.add_screen_time),
    url(r'^screen_success$', views.screen_success),
    url(r'^screen_failure$', views.screen_failure),
    url(r'^movie_success$', views.movie_success),
    url(r'^movie_failure$', views.movie_failure),
    url(r'^screen_time_success$', views.screen_time_success),
    url(r'^screen_time_failure$', views.screen_time_failure),
    url(r'^error$',views.error),
    url(r'^get_movie$',views.get_movie),
    url(r'^reserve_seat$',views.reserve_seat)
    
]