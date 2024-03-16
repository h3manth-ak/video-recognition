from frame_extraction import VideoFrameExtractor
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
# import os

video_path = 'C:/Users/USER/Desktop/main-project/dataset/program/sample.mp4'
frame_extractor = VideoFrameExtractor(video_path)

frames = frame_extractor.get_frames()

loaded_model = tf.keras.models.load_model('C:/Users/USER/Desktop/main-project/dataset/program/model1.h5')

# load each frame and predict

for frame in frames:
    img = image.load_img(frame, target_size=(224, 224))  # Adjust target_size based on your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    prediction = loaded_model.predict(img_array)
    print(prediction)
    # print(np.argmax(prediction))
    # print(np.max(prediction))
    # print(np.argmax(prediction), np.max(prediction))
    # print(np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction))
    # print(np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction))
    # print(np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction))
    # print(np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction), np.argmax(prediction), np.max(prediction))


