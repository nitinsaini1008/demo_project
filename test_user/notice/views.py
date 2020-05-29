from django.shortcuts import render

# Create your views here.
from . models import notification

def notice(request):
	d=notification.objects.all()
	return render(request,'home_2.html',{'d':d})
