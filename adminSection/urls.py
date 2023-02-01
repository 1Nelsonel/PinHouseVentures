from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add-property/', views.addProperty, name="add-property"),
    path('add-location/', views.addLocation, name="add-location"),
    path('add-property-category/', views.addPropertyCategory, name="add-property-category"),
    path('bookings/', views.bookings, name="bookings"),
    path('my-property/', views.myProperty, name="my-property"),
    path('messages/', views.messages, name="messages"),
    path('my-profile/', views.myProfile, name="my-profile")
]