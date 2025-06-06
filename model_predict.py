import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st

@st.cache_resource
def model_loading():
    model=load_model('casting_detection.h5')
    return model


def load_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels = 3)
    image = tf.image.resize(image, size=(256, 256))
    image = tf.cast(image, dtype= tf.float32)/255
    return image


def prediction(path):

    img=load_image(path)
    model=model_loading()
    img=tf.expand_dims(img,axis=0)
    pred=model(img)
    print("Logger Prediction",pred)
    if float(pred[0][0])<=0.5:
        return "DEFECT"
    else:
        return "NO DEFECT"


