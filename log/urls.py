#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
#    url(r'^$', views.home, name='home'),
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^course$', views.course_list, name='course_list'),
    url(r'^course/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^course/(?P<course_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]