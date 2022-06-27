# import picamera
from time import time, sleep, gmtime, strftime
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from email_message import send_email_message, get_recievers
from log_handler import open_log_file, close_log_file
# from GPS_Capture import getPositionData
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def test_model(image_for_testing):
    test_image=image.load_img(image_for_testing,target_size=(224,224))
    test_image=image.img_to_array(test_image)
    test_image=test_image/255
    test_image=np.expand_dims(test_image,axis=0)
    result=np.argmax(my_model.predict(test_image),axis=1)
    return result


old_stdout, log_file = open_log_file("fire_proj_main")

my_model = load_model("./fireproject/Smoke_and_Fire_Classifier.h5")

# with picamera.PiCamera() as camera:
#     camera.resolution = (256, 256)
#     camera.framerate = 80
#     camera.start_preview()
#     sleep(1)

#     start = time()
#     for filename in camera.capture_continuous('./testFolder/image{timestamp:%H:%M:%S.%f}.jpg'):
#         prediction = test_model(filename)
#         finish = time()
#         print('Captured %s at %.2ffps' % (filename, 1 / (finish - start)))
#         send_email_message(lat_lon=getPositionData(),
#                         receivers=get_recievers(),
#                         warning_level=prediction)
#         sleep(0.1)
#         start = time()

send_email_message(lat_lon= (45, 45),
                receivers=get_recievers(),
                warning_level=test_model('smoke.jpg'))

close_log_file(old_stdout, log_file)
