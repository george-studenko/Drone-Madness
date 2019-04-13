from Mission import *


#Drone = Tello()

#Drone.connect()
#Drone.takeoff()
#Drone.land()

def main():

    print('Starting...')
    mission = Mission()
    #while (True):
    print(mission.Drone.response)
    print(mission.Drone._)
    # run frontend
    # frontend.run()
    mission.Drone.end()
    print('Closing...')


if __name__ == '__main__':
    main()