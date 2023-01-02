from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('agents/', views.agents, name='agents'),
    path('agent/', views.agent, name='agent'),
    path('listings/', views.listings, name='listings'),
    path('listing/<str:pk>/', views.listing, name='listing'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]