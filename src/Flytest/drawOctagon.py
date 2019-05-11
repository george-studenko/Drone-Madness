from djitellopy import Tello
import cv2
import time

tello = Tello()

tello.connect()

tello.takeoff()
time.sleep(5)

# tello.streamon()
# time.sleep(5)

# tello.move_left(100)
# time.sleep(5)

tello.rotate_clockwise(45)
time.sleep(5)

tello.move_forward(100)
time.sleep(5)

tello.rotate_clockwise(90)
time.sleep(5)

tello.move_forward(100)
time.sleep(5)

tello.rotate_clockwise(135)
time.sleep(5)

tello.move_forward(141)
time.sleep(5)


# tello.rotate_clockwise(45)
# time.sleep(5)


tello.land()
time.sleep(5)


# tello.streamoff()
# time.sleep(5)


tello.end()



h2 = c2+c2

