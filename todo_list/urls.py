from django.urls import path
from . import views
from .views import *

urlpatterns=[
        path('',views.home,name="home"),
        path('delete/<list_id>',views.delete,name="delete"),
        path('cross_off/<list_id>',views.cross_off,name="cross_off"),
        path('Uncross/<list_id>',views.Uncross,name="Uncross"),
        path('edit/<list_id>',views.edit,name="edit"),
        path('Email_Subscription', views.Email_Subscription,name="signup"),

]