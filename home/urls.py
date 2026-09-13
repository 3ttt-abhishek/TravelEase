from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('domestic/', views.domestic, name='domestic'),
    path('international/', views.international, name='international'),
    path('flight-booking/', views.flight_booking, name='flight_booking'),
    path('hotel/', views.hotel_page, name='hotel_page'),
    path('hotel-booking/', views.hotel_booking, name='hotel_booking'),
    path('booknow/', views.booknow, name='booknow'),
    path('password/', views.password, name='password'),
]
