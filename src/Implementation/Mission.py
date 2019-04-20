from tello import *
from flight_states import *
import numpy as np
import inspect
import time
import functools


class Mission(object):
    def __init__(self, debug_status = False):
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
        #self.print_state(self.Drone.state_dict)
        self.callbacks = {}
        self.in_mission = False
        self.end_mission = False
        self.stream_on = False

        functools.partial(print, flush=True)

        self.start_mission(debug_status)
        #self.register_callback(MessageID.STATE, se,lf.state_callback)


    
    def state_callback(self):
        time.sleep(2)

        if self.flight_state == States.DEBUG_SENSORS:
            self.check_drone_status_transition()

        elif self.flight_state == States.MANUAL:
            self.arming_transition()

        elif self.flight_state == States.TAKEOFF:
            self.takeoff_transition()
            #self.print_state(self.Drone.state_dict)

        elif int(self.Drone.state_dict['tof']) >= 29 and self.in_mission is False:
            self.in_mission = True
            self.mission_transition()

        #elif self.flight_state == States.IN_MISSION:
        #    self.mission_transition()


        elif self.flight_state == States.LANDING:
            #self.print_state(self.Drone.state_dict)
            self.landing_transition()



    def landing_transition(self):
        command_executed = self.Drone.land()
        if command_executed:

            time.sleep(1)
            self.Drone.end()
            self.end_mission = True
        else:
            self.landing_transition()

    def mission_transition(self):
        print('transition:',inspect.stack()[0][3])
        print('mission transtion started...')
        command_executed = self.Drone.rotate_clockwise(360)
        self.Drone.get_frame_read()
        if command_executed:
            #time.sleep(5)
            self.flight_state = States.LANDING
        else:
            time.sleep(1)
            self.mission_transition()

    def arming_transition(self):
        print('transition:',inspect.stack()[0][3])
        print('arming transtion started...')
        command_executed = self.Drone.connect()
        print('COMMAND STATUS: ',command_executed)
        if command_executed:
            #time.sleep(2)
            self.flight_state = States.TAKEOFF
        else:
            time.sleep(1)
            self.arming_transition()

    def takeoff_transition(self, do_not_takeoff = False):
        print('transition:', inspect.stack()[0][3])
        print('take off transtion started...')
        if do_not_takeoff:
            self.flight_state = States.IN_MISSION
            print('take off cancelled...')
        else:
            command_executed = self.Drone.takeoff()
            self.Drone.get_frame_read()
            if command_executed:
                #time.sleep(3)
                self.flight_state = States.IN_MISSION
            else:
                time.sleep(1)
                self.takeoff_transition()

    def check_drone_status_transition(self):
        self.print_state(self.Drone.state_dict)
        self.capture_img()



    def register_calclback(self, event, callback):
        if self not in self.callbacks:
            self.callbacks[self] = {}
        self.callbacks[self][event] = callback

    def print_state(self, drone_state):
        readings = ''
        for sensor, state in drone_state.items():
            if state == '':
                continue
            else:
                readings += ' ' + str.format('{0}: {1} ', sensor, state)
        if readings:
            print(readings)

    def capture_img(self):
        if not self.stream_on:
            self.Drone.streamon()
            self.stream_on = True
        self.Drone.get_frame_read()


    def start_mission(self, debug_status):
        print('Starting mission...')
        if debug_status:
            self.flight_state = States.DEBUG_SENSORS
        while(not self.end_mission):
            self.state_callback()
            if not debug_status:
                self.print_state(self.Drone.state_dict)
        print('Mission completed')



