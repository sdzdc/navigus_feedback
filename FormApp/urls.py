from django.contrib import admin
from django.conf.urls import url
from . import views


app_name = 'FormApp'

urlpatterns = [
    url(r'^$',views.vForm,name="vForm"),
]
