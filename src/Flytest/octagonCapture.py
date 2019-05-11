from djitellopy import Tello
# import numpy as np
import cv2
import time
from predictf import predict_frame, contruct_net
from confluent_kafka import Producer

# Define input camera
cap = cv2.VideoCapture(0)

# Define the codec
output = 'capturing.mp4'
fourcc = cv2.VideoWriter_fourcc(*'vp09')
width = int(cap.get(3))
height = int(cap.get(4))

# Create VideoWriter object
writer = cv2.VideoWriter(output, fourcc, 25, (width, height))

# Start Tello cnx
tello = Tello()

tello.connect()
time.sleep(5)

tello.takeoff()
time.sleep(5)

tello.streamon()
time.sleep(5)

# Contruct net
input_node, net = contruct_net()


# Kafka connect
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))

p = Producer({'bootstrap.servers': '192.168.56.51:9092'})

try:
    for val in range(1, 10):
        p.produce('mytopic', 'myprod #{0}'
                  .format(val), callback=acked)
        p.poll(0.5)

except KeyboardInterrupt:
    pass

p.flush(30)


ret=0
frame_read = tello.get_frame_read()
# while(cap.isOpened()):
while(ret<9):
    frame = frame_read.frame
    ret+=1

    # Rotate 45 avance 100 (octagon)
    tello.rotate_clockwise(45)
    time.sleep(5)

    tello.move_left(100)
    time.sleep(5)

    # write the flipped frame

    writer.write(frame)
    pred = predict_frame('models/NYU_FCRN.ckpt', frame, ret, input_node, net)

    p.produce('mytopic', 'myframe #{0}'.format(val), callback=acked)

    print("Actual frame:", ret)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished


writer.release()
tello.streamoff()

tello.land()
time.sleep(5)

tello.end()

cv2.destroyAllWindows()



#
#
#
# plt.imshow(video[frame,:,:,:])
#
# print(frame)
