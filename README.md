# Weather API Service

This is a simple client (API) for getting weather data from [WeatherAPI](https://www.weatherapi.com/).

## Features
* You can read, add, edit and delete city, temperature, condition.
* You don't need any database, everything is stored in the local variable.


## Installing

```shell
git clone https://github.com/MarianKovalyshyn/weather.git
cd weather/
python -m venv venv
source venv/bin/activate (MacOS)
venv\Scripts\activate (Windows)
pip install -r requirements.txt
python manage.py runserver
```
To use the API, you need to register on the [WeatherAPI](https://www.weatherapi.com/) and get your API key.
Then you need to create a file .env in the root directory and add your API key to it.

## Examples

### Gettting current temperature for the city:
![img.png](img.png)

### Getting current condition for the city:
![img_1.png](img_1.png)

### Changing city:

![img_2.png](img_2.png)
