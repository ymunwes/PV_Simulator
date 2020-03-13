import os
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import pvlib
from pvlib import clearsky, atmosphere, solarposition
from pvlib.location import Location
from pvlib.iotools import read_tmy3


class pvSim():
    def __init__(self, deviceSize=12.0, latitude=49.4, longitude=8.67, height=114, dateStart='2020-03-01',dateEnd='2020-03-02', freq='1s'):
        self._deviceSize=deviceSize
        self._latitude=latitude
        self._longtitude=longitude
        self._height=height

        self._dateStart = dateStart
        self._dateEnd = dateEnd
        self._freq =freq
        self._time = []
        self._power = []
        
    def __del__(self):
        print('Destructor called')

    def simulate(self):
        place = Location(self._latitude, self._longtitude, 'Europe/Paris', self._height, 'Heidelberg')
        #tus = Location(49.4, 8.67, 'Europe/Paris', 114, 'Heidelberg')
        times = pd.date_range(start=self._dateStart, end=self._dateEnd, freq=self._freq, tz=place.tz)
        #times = pd.date_range(start='2020-03-01', end='2020-03-02', freq='5s', tz=tus.tz)
        cs = place.get_clearsky(times)
        c = cs.dni
        for t in range(len(times)):
            #print(times[t], c[t],times[t].time().second)  
            self._time.append(times[t])
            self._power.append(c[t]*self._deviceSize)
    def getVal(self, time):
        if time > len(self._time):
            print("out of simulation range")
            return -1 , -1
        return self._time[time], self._power[time]

