from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST['city']

        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q = ' + city + '&appid = your_api_key').read()

        data_list = json.loads(source)

        data = {
            "country_code": str(data_list['sys']['country']),
            "coordinate" : str(data_list['coord']['lon']) + ' '+ str(data_list['coord']['lat']),
            "temp" :       str(data_list['main']['temp']) + 'k',

        }
    else:
        data = { }
    return render (request, 'index.html',data)