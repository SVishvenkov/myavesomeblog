from django.shortcuts import render
from .models import Event
# Create your views here.
def home(reqest):
	events = Event.objects
	return render(reqest, 'events/home.html', {'events': events})