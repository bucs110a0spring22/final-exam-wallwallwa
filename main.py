from location import Location
from airquality import AirQuality

def main():
    # get location in latitude and longitude
    loc = Location()
    locationString = input('Enter a location to see the air quality: ')

    if len(locationString) > 0:
        lat, lon = loc.getLatLon(locationString)
    else:
        # if location string is empty, default arg is 'Binghamton, NY'
        lat, lon = loc.getLatLon()
        
    # get AQI and main pollutant at location
    airQuality = AirQuality()
    aqi, mainPollutant = airQuality.getPollution(lat, lon)

    # determine safety level based on AQI value
    safety = ''
    if aqi <= 50:
        safety = 'good'
    elif aqi <= 100:
        safety = 'moderate'
    elif aqi <= 150:
        safety = 'unhealthy for sensitive groups'
    elif aqi <= 200:
        safety = 'unhealthy'
    elif aqi <= 300:
        safety = 'very unhealthy'
    else:
        safety = 'hazardous'

    # print air quality and location
    locationName = airQuality.getLocationName(lat, lon)
    print(f'In {locationName} the AQI is {aqi} ({safety}), and the main pollutant is {mainPollutant}.')
    
main()