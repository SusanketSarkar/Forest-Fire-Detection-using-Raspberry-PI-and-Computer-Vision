## Import Libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.optimizers import Adam
from keras.callbacks import History
import PIL
from data_preprocessing import data_preprocess

def model_train():
    train_dataset, validation_dataset = data_preprocess()
    model=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3),activation='relu',input_shape=(224,224,3)),
                                 tf.keras.layers.MaxPool2D(2,2),
                                  tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(224,224,3)),
                                 tf.keras.layers.MaxPool2D(2,2),
                                  tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(224,224,3)),
                                 tf.keras.layers.MaxPool2D(2,2),
                                 tf.keras.layers.Flatten(),
                                   tf.keras.layers.Dense(512,activation='relu'),
                                  tf.keras.layers.Dense(3,activation='softmax'),
                                  
                                 ])
    model.compile(  loss='categorical_crossentropy',
                    optimizer=Adam(lr=0.0001),
                    metrics=['acc'])

    history= model.fit( train_dataset,
                        steps_per_epoch = 15,
                        epochs =100,
                        validation_data = validation_dataset,
                        validation_steps = 15)
    return model, history


