import serial
import time

py_serial = serial.Serial(
    port='COM5',
    baudrate=9600,
)

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Load the model
model = load_model('keras_model.h5', compile=False)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open('test.jpg')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
predictions = model.predict(data)[0]
max_index = 0;
for i, prediction in enumerate(predictions):
    if predictions[max_index] <= prediction: max_index = i
    print(prediction * 100)

v = int(predictions[max_index] * 100)
print(max_index, v)

commend = str(max_index) + str(v).rjust(3, ' ')
print(commend)
py_serial.write(commend.encode())

time.sleep(0.1)

if py_serial.readable():
    response = py_serial.readline()
    print(response[:len(response)-1].decode())