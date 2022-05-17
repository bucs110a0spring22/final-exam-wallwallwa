import requests
import sys

UNITS = {
    'p2': 'pm2.5',
    'p1': 'pm10',
    'o3': 'Ozone O3',
    'n2': 'Nitrogen dioxide NO2',
    's2': 'Sulfur dioxide SO2',
    'co': 'Carbon monoxide CO'
}

class AirQuality:
    def __init__(self):
        '''
        initialize instance of class, creating instance variables
        '''
        self.api_url = 'http://api.airvisual.com/v2/nearest_city'
        self.api_key = '4fda7549-fc39-4b0d-909e-b9d94f5d71d3'
        self.location = ''
        self.aqi = 0
        self.mainPollutant = ''

    def __str__(self):
        '''
        string representation of class, location, AQI, main pollutant, api_url, and api_key
        return: (string) string containing instance variables of class
        '''
        return f'location: {self.location}, AQI: {self.aqi}, Main Pollutant: {self.mainPollutant}, api_url: {self.api_url}, api_key: {self.api_key}'

    def get(self, lat, lon):
        '''
        sends API request to retrieve all air quality data from the nearest city to a given location, and populates instance variables
        args: (float, float) the latitude and longitude of the desired location
        return: (json) a json-formatted response containing all air quality data
        '''
        try:
            
            params = {'lat': lat, 'lon': lon, 'key': self.api_key}
            response = requests.get(self.api_url, params=params)
            response = response.json()
            
            data = response['data']
            pollution = data['current']['pollution']
            self.location = f"{data['city']}, {data['state']}, {data['country']}"
            self.aqi = pollution['aqius']
            self.mainPollutant = UNITS[pollution['mainus']]
        except:
            sys.exit('Something went wrong retrieving the air quality, please try again, or use a different location.')

        return response

    def getPollution(self, lat, lon):
        '''
        retrieves the AQI and main pollutant for a given location
        args: (float, float) the latitude and longitude of the desired location
        return: (tuple) tuple containing the AQI (integer), and the main pollutant (string)
        '''
        self.get(lat, lon)
        return (self.aqi, self.mainPollutant)

    def getLocationName(self, lat, lon):
        '''
        retrieves the name of a location formatted to CITY, STATE, COUNTRY, given latitude and longitude
        args: (float, float) the latitude and longitude of the desired location
        return: (string) string location formatted to CITY, STATE, COUNTRY
        '''
        self.get(lat, lon)
        return self.location