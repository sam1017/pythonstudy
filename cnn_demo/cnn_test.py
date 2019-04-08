
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from cnn_settings import Cnn_settings

def testing_image(file_string):
    settings = Cnn_settings()
    model_path = settings.model_path
    testImage = Image.open(file_string)

    with tf.Graph().as_default():
        output_graph_def = tf.GraphDef()
        with open(model_path, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            tf.import_graph_def(output_graph_def, name="")
