import sys
sys.path.insert(0,"../")

import api.ps_drone as ps_drone
import time


drone = ps_drone.Drone()  # Start using drone

drone.startup()  # Connects to drone and starts subprocesses
drone.reset()  # Always good, at start
drone.trim()
drone.getSelfRotation(5)
time.sleep(0.5)
print "Bateria: ", drone.getBattery()[0]
print "takeoff"
drone.takeoff()
time.sleep(3)

print "hovering"
drone.hover()
time.sleep(3)

drone.moveUp(0.999)
print("Going up on a Tuesday")
time.sleep(3)

print("Hovering bruh")
drone.hover()
time.sleep(2)

print "land"
drone.land()

