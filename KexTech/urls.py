from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, name="logout"),
    url(r'^admin/', admin.site.urls),
    url(r'^course', include('course.urls')),
]
