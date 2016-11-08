
#!python
# project/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.conf.urls.static import static
from django.contrib.auth import views
from log.forms import LoginForm
from log.views import user_login

urlpatterns = [
    url(r'^reviews/', include('log.urls', namespace="reviews")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^login_failed/$', views.login, {'template_name': 'login_failed.html', 'authentication_form': LoginForm}, name='login_failed'),
    url(r'^login1/$', user_login, name='auth'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
#    url(r'^ratings/', include('ratings.urls')),
#    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
