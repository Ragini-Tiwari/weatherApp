import requests
from django.shortcuts import render

def index(request):
    # Replace with your OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'

    # Get user's city input (example using a form)
    city = request.GET.get('city')

    if city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            # Extract relevant weather data
            weather = data['weather'][0]['main']
            temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
            # Add more data as needed (humidity, pressure, etc.)
            context = {'weather': weather, 'temperature': temperature}
            return render(request, 'weather/index.html', context)
        else:
            error_message = 'City not found. Please try again.'
            context = {'error_message': error_message}
            return render(request, 'weather/index.html', context)
    else:
        context = {}
        return render(request, 'weather/index.html', context)
