#!/usr/bin/env python3

import tensorflow as tf
print('TensorFlow version - ',tf.__version__)
# Check if GPU is available
gpu_available = tf.config.list_physical_devices('GPU')

if gpu_available:
    print("TensorFlow is installed as GPU version.")
else:
    print("TensorFlow is installed as CPU version.")
