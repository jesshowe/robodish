import serial
import json

class Positioner:
    ser = serial.Serial('/dev/ttyACM0')
    def writeSatellites(self):

    def readSatellites(self):
        with open('satellites.txt') as json_file:
            data = json.load(json_file)
            for satellite in data['satellite']:

    def gotoSatellite(SatelliteName):
        #Look up SatelliteName in db
        #Figure out where we are first
        #Figure out how many ticks it will take to get to SatelliteName
        #
