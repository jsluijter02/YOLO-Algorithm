import torch
import torch.nn as nn
import tensorflow as tf
from tensorflow import keras
from keras import layers 

#for the link to the original yolo paper see:
#https://arxiv.org/pdf/1506.02640v5.pdf
#arc is the models architecture
arc = [
    #input = 448x448

    #conv layer (filter size, strides, num filters, padding)
    (7, 2, 64, 3),
    #maxpool layer (size, strides)
    (2,2),
    #conv layer (filter size, strides, num filters, padding)
    (3, 1, 192, 1),
    #maxpool layer (size, strides)
    (2,2),

    #conv
    (1,1,128,0),
    #conv
    (3,1,256,1),
    #conv
    (1,1,256,0),
    #conv 
    (3,1,512,1),
    #maxpool layer (size, strides)
    (2,2),

    #conv x4
    (1,1,256,0),
    (3,1,512,1),

    #conv
    (1,1,512,0),
    #conv
    (3,1,1024,1),
    #maxpool
    (2,2),

    #conv x2
    (1,1,512,0),
    (3,1,1024,1),
    #conv
    (3,1,1024,1),
    #conv
    (3,2,1024,1),

    #conv
    (3,1,1024,1),
    #conv
    (3,1,1024,1),

    #FC layer, 1x4096
    #FC layer, 7x7x30

   #output = 7x7, so number of cells of the yolo algo x 30, bounding boxes and num classes 
]



class Yolo_model(keras.Model):

    def __init__(self, input_size, output_size):
        super(Yolo_model, self).__init__()

    
    def forward(self, X):
        pass 








