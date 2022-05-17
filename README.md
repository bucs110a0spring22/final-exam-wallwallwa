#### CS 110
# Final Exam - Advanced Programming with Python

### [Exam Description](https://docs.google.com/document/d/1FI-WV95nSTK1JMg5j5sKhxcbl46DPVPkBrxC3FMo45g/edit?usp=sharing)

***


_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
Please make sure you have completed the soot survey at:
    [soot.binghamton.edu](https://soot.binghamton.edu)

Please list the urls for the APIs you used: http://api.airvisual.com/v2/nearest_city, https://nominatim.openstreetmap.org/search

Summary of Program: This program takes a location in the form of a free-forms string, and retrieves the latitude and longitude of that location. It then retrieves the Air Quality Index (AQI) and the main pollutant from the city nearest to those coordinates, and prints them out.

Most Challenging topic in the course:
GUI's
## KNOWN BUGS AND INCOMPLETE PARTS:
If there is no air quality sensor in a location, it will not alert the user, however it will automatically find the nearest one. Also, this API only allows 5 calls per minute, and it will return an error if you exceed that amount.

## REFERENCES:
none
## MISCELLANEOUS COMMENTS:
none