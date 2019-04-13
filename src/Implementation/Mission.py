from tello import *
from flight_states import *
import numpy as np

class States(Enum):
    MANUAL = 0
    ARMING = 1
    TAKEOFF = 2
    WAYPOINT = 3
    LANDING = 4
    DISARMING = 5

class Mission(object):
    def __init__(self):
        #super().__init__(connection)
        self.target_position = np.array([0.0, 0.0, 0.0])
        self.all_waypoints = []
        self.in_mission = True
        self.check_state = {}
        self.current_waypoint = 0
        self.starting_point = [0,0,0]
        self.navigating = False
        self.Drone = Tello()
        self.flight_state = States.MANUAL
        print(self.Drone.response)
        self.Drone.connect()
        #self.Drone.takeoff()
        print(self.Drone.response)
        #self.Drone.land()
        print(self.Drone.response)
        self.callbacks = {}

        self.register_callback(MessageID.STATE, self.state_callback)

        #for c in self.callbacks:
        #    print(c)


    def state_callback():
        print('STATE CALLBACK called....')

    def register_callback(self, event, callback):
        if self not in self.callbacks:
            self.callbacks[self] = {}
        self.callbacks[self][event] = callback

