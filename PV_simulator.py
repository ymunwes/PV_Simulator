#!/usr/bin/env python
import pika
import matplotlib.pyplot as plt
from pvSim import pvSim

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Meter')

#simulate PV for 24h
pv = pvSim()
pv.simulate()

#open file to store the results
file = open("results.txt","w");

#parameters for integration
sumAll=0
sumMeter=0
sumPV=0
lastT=0
def callback(ch, method, properties, power):
    global lastT
    dt = int(int(power)/100000)
    delta= dt -lastT
    lastT = dt
    pW = int(power) - dt*100000
    pW = pW
    print(" [x] Received "+str(dt)+" "+str(pW))
    
    #get simulation value for the same t
    t,W = pv.getVal(dt)
    global sumMeter, sumAll,sumPV
    sumMeter= sumMeter + pW/3600 * delta #normilaize to hour
    sumPV = sumPV + W/3600 * delta #normilaize to hour
    sumAll=sumPV-sumMeter
    
    print(" simulatated value:"+str(t)+", "+str(W))

    file.write(str(t)+" "+ str(round(pW,2))+" " +str(round(W,2))+" "+str(round(sumMeter,2))+" " +str(round(sumPV,2))+" "+str(round(sumAll,2))+"\n")
    

channel.basic_consume(
    queue='Meter', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
file.close()


