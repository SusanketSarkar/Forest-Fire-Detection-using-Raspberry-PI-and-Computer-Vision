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
from model_training import model_train

def test_model(image_for_testing, model):
    test_image=image.load_img(image_for_testing,target_size=(224,224))
    test_image=image.img_to_array(test_image)
    test_image=test_image/255
    test_image=np.expand_dims(test_image,axis=0)
    result=np.argmax(model.predict(test_image),axis=1)

    Catagories=['fire', 'nofire', 'smoke']

    image_show=PIL.Image.open(image_for_testing)
    plt.imshow(image_show)

    plt.title(Catagories[int(result)])
    plt.axis("off")
    plt.show()