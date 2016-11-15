from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Adventure
import datetime
import stripe
#Also going to need something here to grab the db objects

# Create your views here.
def home(request):
    #gotta do this same thing where I order only the objects that are upcoming
    featured_trips = Adventure.objects.filter(start_date__gte=datetime.date.today()).order_by('-start_date')[:4]

    context = {
    'featured_trips': featured_trips
    }
    return render(request, "swiing/index.html", context)

def about(request):
    return render(request, "swiing/about.html")

def adventures(request):
    #remember this is a query so this has to be in db style, not python.
    for_sale_adventures = Adventure.objects.filter(start_date__gte=datetime.date.today()).order_by('-start_date')
    context = {
    'for_sale_adventures': for_sale_adventures,
    }
    return render(request, "swiing/adventures.html", context)

def singletrip(request, a_slug):
    adventure = Adventure.objects.get(a_slug = a_slug)
    context = { 'adventure': adventure, }
    return render(request, "swiing/singletrip.html", context)

def contact(request):
    return render(request, "swiing/contact.html")

def charge(request):
    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here: https://dashboard.stripe.com/account/apikeys
    stripe.api_key = "sk_test_RYJpRydqzXGHoT9rYm9piIXk"
    stripe.api_base = "https://api-tls12.stripe.com"
    # Get the credit card details submitted by the form
    token = request.POST['stripeToken']

    # Create a charge: this will charge the user's card
    try:
        charge = stripe.Charge.create(
        amount=1000, # Amount in cents
        currency="usd",
        source=token,
        description="Example charge"
        )
    except stripe.error.CardError as e:
        # The card has been declined
        pass
    return HttpResponse("Hello, world. You're at the polls index.")
