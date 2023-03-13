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

## Data preproceesing
def data_preprocess():
    train=ImageDataGenerator(rescale=1/255)
    validation=ImageDataGenerator(rescale=1/255)
    train_dataset=train.flow_from_directory('Dataset/Training/',target_size=(224,224),
                                        class_mode='categorical',shuffle=True)
    validation_dataset=validation.flow_from_directory('Dataset/validation/',target_size=(224,224)
                                        ,class_mode='categorical',shuffle=True)

    print("The class Indices are:", train_dataset.class_indices)
    print("The classes are:", train_dataset.classes)

    return train_dataset, validation_dataset

