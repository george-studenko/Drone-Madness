import os
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from PIL import Image
import cv2
import glob

import models

# RUN WITH
# python36 predicts.py models/NYU_FCRN.ckpt images3
#
#

# Default input size
height = 228
width = 304
path = "captured"
channels = 3
batch_size = 1
j=0
    
def contruct_net():
    # Create a placeholder for the input image
    input_node = tf.placeholder(tf.float32, shape=(None, height, width, channels))
    # Construct the network
    net = models.ResNet50UpProj({'data': input_node}, batch_size, 1, False)
    return input_node,net
    
def predict_frame(model_data_path, frame, frame_number, input_node, net):
    print("-----------Working on:", frame_number)
        
#   img = Image.open(path+"/"+filename)
    img = Image.fromarray(frame)
    img = img.resize([width,height], Image.ANTIALIAS)
    img = np.array(img).astype('float32')
    img = np.expand_dims(np.asarray(img), axis = 0)

    with tf.Session() as sess:
        # Load the converted parameters
        print('Loading the model')
        saver = tf.train.Saver()     
        saver.restore(sess, model_data_path)

        # Use to load from npy file
        #net.load(model_data_path, sess) 

        # Evalute the network for the given image
        pred = sess.run(net.get_output(), feed_dict={input_node: img})

        # Plot result
        fig = plt.figure()
        ii = plt.imshow(pred[0,:,:,0], interpolation='nearest')

        if frame_number == 40:
            myfile = open("kaka.txt", 'w')
            np.set_printoptions(threshold=np.inf, linewidth=960)
            myfile.write(np.array2string(pred, formatter={'float_kind':lambda x: "%.3f" % x}, precision=2, separator=',', suppress_small=True).replace(',\n', '').replace('   ', '\t').replace('[', '').replace(']', ''))
            myfile.close()

        fig.colorbar(ii)

    outname=str(frame_number) + ".jpg"
    plt.savefig(path+"/"+outname)
    plt.close(fig)
        
    return pred