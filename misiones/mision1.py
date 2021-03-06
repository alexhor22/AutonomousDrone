import VL53L0X
import sys
sys.path.insert(0,"../")
import api.ps_drone as ps_drone
from tools import emergency
import time


def main():

    drone = ps_drone.Drone()  # Start using drone
    tof = VL53L0X.VL53L0X()
    thread = emergency.keyThread(drone)
    print "Configuracion del drone"
    drone.startup()  # Connects to drone and starts subprocesses
    drone.reset()  # Always good, at start
    drone.trim()                                       # Recalibrate sensors
    drone.getSelfRotation(5)
    time.sleep(0.5)
    thread.start()
    print "BATERIA ACTUAL: ", drone.getBattery()[0]

    print "Comienzo el programa"
    print "takeoff"
    drone.takeoff()
    time.sleep(2)
    drone.hover()
    time.sleep(3)
    #drone.setSpeed(0.1)
    print "hovering"
    tof.start_ranging(4)
    time.sleep(0.001)
    distance = tof.get_distance()

    print "Distance: "
    print distance
    while distance > 1000:
        print "Distance: "
        distance = tof.get_distance()
        print distance
        if distance < 1001:
            drone.moveBackward(0.5)
        else:
            drone.moveForward(0.08)
        print "next"
    tof.stop_ranging()
    #time.sleep(3)
    print "back"
    drone.moveBackward(0.60)
    time.sleep(1)
    drone.hover()
    time.sleep(1.5)
    print "land"
    drone.land()

if __name__ == "__main__":
    main()


