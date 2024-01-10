"""Views for the weather app."""
import os

import requests
from django.core.cache import cache
from dotenv import load_dotenv
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = 'https://api.weatherapi.com/v1/current.json'


class City(APIView):
    """City APIView that allows to get, set, update and delete the current city."""

    def get(self, request: Request) -> Response:
        """Get the current city."""
        city = cache.get('city', None)
        return Response({'city': city})

    def post(self, request: Request) -> Response:
        """Set the current city."""
        city = request.data['city']
        cache.set('city', city)
        return Response({'city': city})

    def put(self, request: Request) -> Response:
        """Update the current city."""
        city = request.data['city']
        cache.set('city', city)
        return Response({'city': city})

    def delete(self, request: Request) -> Response:
        """Delete the current city."""
        cache.delete('city')
        return Response({'city': None})


class Temperature(APIView):
    """Temperature APIView that allows to get, set, update and delete the current temperature."""

    def get(self, request: Request) -> Response:
        """Get the current temperature."""
        temperature = cache.get('temperature', None)
        city = cache.get('city', 'London')
        return Response({'temperature': temperature, 'city': city})

    def post(self, request: Request) -> Response:
        """Set the current temperature via request to weatherapi.com."""
        city = cache.get('city', 'London')
        payload = {'key': WEATHER_API_KEY, 'q': city}
        weather_data = requests.get(url=BASE_URL, params=payload, timeout=5).json()
        temperature = weather_data['current']['temp_c']
        cache.set('temperature', temperature)
        return Response({'temperature': temperature, 'city': city})

    def put(self, request: Request) -> Response:
        """Update the current temperature."""
        temperature = request.data['temperature']
        cache.set('temperature', temperature)
        return Response({'temperature': temperature})

    def delete(self, request: Request) -> Response:
        """Delete the current temperature."""
        city = cache.get('city', 'London')
        cache.delete('temperature')
        return Response({'temperature': None, 'city': city})


class Condition(APIView):
    """Condition APIView that allows to get, set, update and delete the current condition."""

    def get(self, request: Request) -> Response:
        """Get the current condition."""
        condition = cache.get('condition', None)
        city = cache.get('city', 'London')
        return Response({'condition': condition, 'city': city})

    def post(self, request: Request) -> Response:
        """Set the current condition via request to weatherapi.com."""
        city = cache.get('city', 'London')
        payload = {'key': WEATHER_API_KEY, 'q': city}
        weather_data = requests.get(url=BASE_URL, params=payload, timeout=5).json()
        condition = weather_data['current']['condition']['text']
        cache.set('condition', condition)
        return Response({'condition': condition, 'city': city})

    def put(self, request: Request) -> Response:
        """Update the current condition."""
        condition = request.data['condition']
        cache.set('condition', condition)
        return Response({'condition': condition})

    def delete(self, request: Request) -> Response:
        """Delete the current condition."""
        city = cache.get('city', 'London')
        cache.delete('condition')
        return Response({'condition': None, 'city': city})
