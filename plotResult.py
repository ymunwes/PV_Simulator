import matplotlib.pyplot as plt
import numpy as np

time=[0]
meter=[0]
PV=[0]
sumMeter=[0]
sumPV=[0]
sumAll=[0]
count=0
with open('results.txt') as fp:
    for line in fp:
        if count % 10 == 0:
            date, t, m, pv, sm, spv, sall = line.split(" ")
            
            time.append(count*5)
            meter.append(float(m))
            PV.append(float(pv))
            sumMeter.append(float(sm))
            sumPV.append(float(spv))
            sumAll.append(float(sall))
            #print(date,t,m, pv,sm,spv,sall)
        count+=1


plt.plot(time, meter, label='Meter')
plt.plot(time,PV, label='PV simulator')
plt.plot(time, sumMeter, label='Meter integrated')
plt.plot(time, sumPV, label='PV integrated')
plt.plot(time, sumAll, label='total power')

plt.xlabel('time[s]')
plt.ylabel('Power[W]')

plt.legend()
plt.show()

