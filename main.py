## Import Libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os, random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.optimizers import Adam
from keras.callbacks import History
import PIL
from data_preprocessing import data_preprocess
from model_training import model_train
from model_eval import model_eval, model_eval_acc, model_eval_loss
from test import test_model

## Training the model
model, history = model_train()
model_eval_acc(history)
model_eval_loss(history)
model_eval(model)
model.save("Smoke_and_Fire_Classifier.h5")

## Testing the model
dir = "E:\Data Science\PROJECTS\FORESTFIRE\Dataset\Testing\\"+os.listdir("E:\Data Science\PROJECTS\FORESTFIRE\Dataset\Testing")[random.rand(0, len(os.listdir("E:\Data Science\PROJECTS\FORESTFIRE\Dataset\Testing")
test_model(dir+os.listdir(dir)[random.rand(0,len(dir))])



