###############################################
#	PV simulator		              #
#					      #
#   writen by Y.Munwes 2020/03		      #
###############################################

This project simulate a power meter readout and PV readout

The meter class is simulated using random walk in randomWalk.py
paramters:
initial value, probabilites to go up or down, step resolution, and limits

meter.py:
open connetion to broker and generate values using the randomWalk
user can send arguments for changing the delay between each step, time difference in real time, and also to plot.
(example: python meter.py -plot=True -delay=0.000001)
pvSim.py:
simulator class of PV using the pvlib library
Simple simulation, with clear sky conditions

PV_simulator.py:
open connection to the borker, simulate single day of PV values, once the broker send meter values it get the simulated PV value and calculate the difference+ the integration of the meters.
Save data to file results.txt

plotResult.py:
plot all values with respect to time

Run:
1. run rabbitmq-server
2. python meter.py (another termianl)
3. python PV_simulator.py (another termianl)

if needed at the end run python plotResult.py
