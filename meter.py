#!/usr/bin/env python
import pika
import random 
import numpy as np 
import matplotlib.pyplot as plt 
import time
from randomWalk import randomWalk
import argparse


# Define the parser
parser = argparse.ArgumentParser(description='read meter based on random walk')

parser.add_argument('-delay', action="store", dest='delay', default=0.001,help="-delay: delay between random walk steps (to reduce runing time)[sec]")
parser.add_argument('-stepTime', action="store", dest='stepTime', default=5,help="-stepTime: delta time between simulation steps [sec]")
parser.add_argument('-plot', action="store", dest='plot', default=False,help="-plot: plotting at the end the meter vs time")

#get the parameters
args = parser.parse_args()
stepTime = int(args.stepTime)
delay = float(args.delay)
doPlot = bool(args.plot)

#open connection to broker
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Meter')

if doPlot:
    positions = [0]
    timeStep = [0]

#define the random walk object
rWalk = randomWalk(probDown=0.2, probUp=0.8)

#init values
power = 0
fullDay = 60*60*24

#loop for 24 hours with steps of 5 sec
for dt in range(0, fullDay, stepTime):
    power = rWalk.getVal(power)
    power = power
    print("time:"+str(dt)+" power:"+str(power))
    toSend = power + 100000*dt
    channel.basic_publish(exchange='', routing_key='Meter', body=str(toSend))
    if doPlot:
        positions.append(power)
        timeStep.append(dt)
    
    time.sleep(delay)
    

if doPlot:
    plt.plot(timeStep,positions)
    plt.xlabel('time[s]')
    plt.ylabel('Power[W]')
    plt.show()

print(" [x] Sent 'Finished")
connection.close()
