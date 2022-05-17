import requests
import sys

class Location:
    def __init__(self):
        '''
        initializes an instance of Location class, creating instance variables
        '''
        self.api_url = 'https://nominatim.openstreetmap.org/search'
        self.lat = 0
        self.lon = 0

    def __str__(self):
        '''
        string representation of class, lat, lon, and api_url
        return: (string) string containing instance variables of class
        '''
        return f'lat: {self.lat}, lon: {self.lon}, api_url: {self.api_url}'
    
    def get(self, locationString='Binghamton, NY'):
        '''
        sends API request to retrieve all information about a given location (defaults to Binghamton, NY)
        args: (string) a free-form query string of a location to get coordinates of
        return: (json) json-formatted response of information
        '''
        params = {'format': 'json', 'limit': '1', 'q': locationString}
        response = requests.get(self.api_url, params=params)
        response = response.json()

        if len(response) < 1:
            sys.exit('Something went wrong retrieving the location, please try again, or use a different location.')
            
        return response

    def getLatLon(self, locationString='Binghamton, NY'):
        '''
        retrieves longitude and latitude of a given location (defaults to Binghamton NY)
        args: (string) a free-form query string of a location to get coordinates of
        return: (tuple) tuple containing numerical values of latitude and longitude
        '''
        response = self.get(locationString)
        response = response[0]
        
        self.lat = response['lat']
        self.lon = response['lon']

        return (self.lat, self.lon)