import traci
import time
import traci.constants as tc
from sumolib import checkBinary
step = 0
sumoBinary = checkBinary('sumo-gui')


traci.start([sumoBinary,"-c","osm.sumocfg","--quit-on-end", "--start"])


while step < 1000:
    traci.simulationStep()
    step +=1
    time.sleep(1)

traci.close()