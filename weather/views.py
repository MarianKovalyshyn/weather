import os
import requests

from dotenv import load_dotenv
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = None
TEMPERATURE = None
CONDITION = None


class City(APIView):
    def get(self, request: Request) -> Response:
        global CITY
        return Response({"city": CITY})

    def post(self, request: Request) -> Response:
        global CITY
        CITY = request.data["city"]
        return Response({"city": CITY})

    def put(self, request: Request) -> Response:
        global CITY
        CITY = request.data["city"]
        return Response({"city": CITY})

    def delete(self, request: Request) -> Response:
        global CITY
        CITY = None
        return Response({"city": CITY})


class Temperature(APIView):
    def get(self, request: Request) -> Response:
        global TEMPERATURE, CITY
        city = CITY if CITY else "London"
        return Response({"temperature": TEMPERATURE, "city": city})

    def post(self, request: Request) -> Response:
        global TEMPERATURE, CITY
        city = CITY if CITY else "London"
        result = requests.get(url=BASE_URL, params={"key": WEATHER_API_KEY, "q": city}).json()
        TEMPERATURE = result["current"]["temp_c"]
        return Response({"temperature": TEMPERATURE, "city": city})

    def put(self, request: Request) -> Response:
        global TEMPERATURE
        TEMPERATURE = request.data["temperature"]
        return Response({"temperature": TEMPERATURE})

    def delete(self, request: Request) -> Response:
        global TEMPERATURE, CITY
        city = CITY if CITY else "London"
        TEMPERATURE = None
        return Response({"temperature": TEMPERATURE, "city": city})


class Condition(APIView):
    def get(self, request: Request) -> Response:
        global CONDITION, CITY
        city = CITY if CITY else "London"
        return Response({"condition": CONDITION, "city": city})

    def post(self, request: Request) -> Response:
        global CONDITION, CITY
        city = CITY if CITY else "London"
        result = requests.get(url=BASE_URL, params={"key": WEATHER_API_KEY, "q": city}).json()
        CONDITION = result["current"]["condition"]["text"]
        return Response({"condition": CONDITION, "city": city})

    def put(self, request: Request) -> Response:
        global CONDITION
        CONDITION = request.data["condition"]
        return Response({"condition": CONDITION})

    def delete(self, request: Request) -> Response:
        global CONDITION, CITY
        city = CITY if CITY else "London"
        CONDITION = None
        return Response({"condition": CONDITION, "city": city})
