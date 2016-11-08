#!python
# log/urls.py
from django.conf.urls import url
from . import views
from log import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^$',views.homepage, name='homepage'),
    url(r'^review$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^user/(?P<user_name>[a-z]+)/$', views.user_detail, name='user_detail'),
    url(r'^course$', views.course_list, name='course_list'),
    url(r'^faculty$', views.faculty_list, name='faculty_list'),
    url(r'^course/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^course/(?P<course_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^user_login$', views.user_login, name='auth'),
]
