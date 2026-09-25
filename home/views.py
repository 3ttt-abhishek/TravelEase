from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def gallery(request):
    return render(request, 'home/gallery.html')


def contact(request):
    return render(request, 'home/contact.html')


def login(request):
    return render(request, 'home/login.html')


def registration(request):
    return render(request, 'home/create_account.html')


def domestic(request):
    return render(request, 'home/domestic.html')


def international(request):
    return render(request, 'home/international.html')


def flight_booking(request):
    return render(request, 'home/flight_booking.html')


def hotel_page(request):
    return render(request, 'home/hotel_page.html')


def hotel_booking(request):
    return render(request, 'home/hotel_booking.html')


def booknow(request):
    return render(request, 'home/booknow.html')


def password(request):
    return render(request, 'home/password.html')
