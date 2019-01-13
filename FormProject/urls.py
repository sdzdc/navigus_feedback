
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include,url
from FormApp import views

urlpatterns = [
    url('admin/', admin.site.urls),
]


urlpatterns += [

  url(r'^$',include('FormApp.urls')),

]
