
WINDOW A
--------
(py3ml) tim@Tims-MBP tensorflow % which tensorboard
/Users/tim/Desktop/Work/Python_Practice/py3ml/bin/tensorboard
(py3ml) tim@Tims-MBP tensorflow % tensorboard --logdir=logs/fit
2025-05-09 13:25:14.622671: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

NOTE: Using experimental fast data loading logic. To disable, pass
    "--load_fast=false" and report issues on GitHub. More details:
    https://github.com/tensorflow/tensorboard/issues/4784

Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.16.2 at http://localhost:6006/ (Press CTRL+C to quit)

WINDOW B
--------
(py3ml) tim@Tims-MBP tensorflow % curl http://localhost:6006/ -o webpage
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  521k  100  521k    0     0   150M      0 --:--:-- --:--:-- --:--:--  169M
(py3ml) tim@Tims-MBP tensorflow % wc -l webpage 
     556 webpage

