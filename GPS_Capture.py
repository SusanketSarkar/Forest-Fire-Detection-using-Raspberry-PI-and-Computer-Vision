# This file hase code that outputs the GPS Coords of a location
from gps import *
import time

running = True

def getPositionData():
    gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        print ("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
        return latitude, longitude


try:
    print ("Application started!")
    while running:
        getPositionData()
        time.sleep(1.0)

except (KeyboardInterrupt):
    running = False
    print ("Applications closed!")
