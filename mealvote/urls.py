from django.conf.urls import url, include
from . import views

app_name = 'mealvote'
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),

]
