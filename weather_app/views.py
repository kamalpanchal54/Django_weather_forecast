from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bf9ac3124e32d8105727035213c296f4').read()
        json_data = json.loads(res)
        data = {
            "temp": int(json_data['main']['temp'] -273.15),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "wind" : str(json_data['wind']['speed']), 
            "description" : str(json_data['weather'][0]['description'] ),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html',   {'city': city, 'data': data})
