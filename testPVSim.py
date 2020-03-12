from pvSim import pvSim
import matplotlib.pyplot as plt

pv = pvSim()
pv.simulate()

t,w = pv.getVal(0)
print(t,w)

t,w = pv.getVal(10000)
print(t,w)

