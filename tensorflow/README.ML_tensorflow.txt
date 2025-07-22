
(py3ml) tim@Tims-MBP tensorflow % vi gpu_check.py
(py3ml) tim@Tims-MBP tensorflow % chmod 755 gpu_check.py 
(py3ml) tim@Tims-MBP tensorflow % cat gpu_check.py 
#!/usr/bin/env python3

import tensorflow as tf
print('TensorFlow version - ',tf.__version__)
# Check if GPU is available
gpu_available = tf.config.list_physical_devices('GPU')

if gpu_available:
    print("TensorFlow is installed as GPU version.")
else:
    print("TensorFlow is installed as CPU version.")

(py3ml) tim@Tims-MBP tensorflow % ./gpu_check.py 
2025-05-09 12:24:02.507585: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
TensorFlow version -  2.16.2
TensorFlow is installed as CPU version.
