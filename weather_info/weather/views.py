from django.shortcuts import render,redirect
from django.contrib import messages
import requests
from .models import City
from .forms import CityForm

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e060cba52334e04c36a20d890cda914f'    
    
    form = CityForm()
    
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data':weather_data,'form':form,}
    
    return render(request,'home.html',context)

def addcity(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e060cba52334e04c36a20d890cda914f'    
    
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            exising_city_count = City.objects.filter(name=new_city).count()
            
            if exising_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                    messages.info(request,'City save successfully!!')
                else:
                    messages.info(request,'City not exists in world yet!')
            else:
                messages.info(request,'City already exists in database!')
                
    else:
        form = CityForm()

    return redirect('home')

def delete(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')