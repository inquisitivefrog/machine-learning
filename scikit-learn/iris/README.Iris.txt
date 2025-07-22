
(py3ml) tim@Tims-MBP machine-learning % ./iris.py
2025-04-24 14:18:22,637 - INFO - Pairplot saved to output/iris_pairplot_20250424_141819.png
2025-04-24 14:18:27,744 - INFO - Description: Iris plants dataset
2025-04-24 14:18:27,744 - INFO - Sample Size: 150
2025-04-24 14:18:27,744 - INFO - Training Size: 120
Best Parameters: {'classifier__max_depth': None, 'classifier__min_samples_split': 10, 'classifier__n_estimators': 50}
2025-04-24 14:18:36,327 - INFO - Test Set Accuracy: 0.967
2025-04-24 14:18:36,789 - INFO - Confusion matrix saved to output/iris_rfc_confusion_matrix_20250424_141836.png
2025-04-24 14:18:39,072 - INFO - Training Set Accuracy: 0.975
2025-04-24 14:18:39,072 - INFO - Test Set Accuracy: 0.967
2025-04-24 14:18:39,394 - INFO - Mean CV Accuracy: 0.958
Best Parameters: {'classifier__C': 0.5, 'classifier__gamma': 'scale', 'classifier__kernel': 'rbf'}
2025-04-24 14:18:40,225 - INFO - Test Set Accuracy: 0.967
2025-04-24 14:18:40,654 - INFO - Confusion matrix saved to output/iris_svc_confusion_matrix_20250424_141840.png
2025-04-24 14:18:42,370 - INFO - Training Set Accuracy: 0.967
2025-04-24 14:18:42,370 - INFO - Test Set Accuracy: 0.967
2025-04-24 14:18:42,391 - INFO - Mean CV Accuracy: 0.983
2025-04-24 14:18:42,396 - INFO - Model saved to output/iris_svc_model.pkl
2025-04-24 14:18:42,414 - INFO - Model saved to output/iris_rfc_model.pkl

(py3ml) tim@Tims-MBP machine-learning % ls -lt | head -7
total 10480
drwxr-xr-x@ 93 tim  staff     2976 Apr 24 14:18 output
-rwxr-xr-x   1 tim  staff     6231 Apr 24 14:18 test_iris.py
drwxr-xr-x@  4 tim  staff      128 Apr 24 14:13 __pycache__
-rwxr-xr-x   1 tim  staff     7142 Apr 24 14:12 iris.py
-rwxr-xr-x   1 tim  staff      450 Apr 24 13:37 clean_output.py
-rw-r--r--   1 tim  staff     3123 Apr 24 11:15 README.md
(py3ml) tim@Tims-MBP machine-learning % ls -lt output | head -7
total 27576
-rw-r--r--  1 tim  staff    5510 Apr 24 14:18 iris.log
-rw-r--r--  1 tim  staff   65866 Apr 24 14:18 iris_rfc_model.pkl
-rw-r--r--  1 tim  staff    5973 Apr 24 14:18 iris_svc_model.pkl
-rw-r--r--  1 tim  staff   82137 Apr 24 14:18 iris_svc_confusion_matrix_20250424_141840.png
-rw-r--r--  1 tim  staff   80943 Apr 24 14:18 iris_rfc_confusion_matrix_20250424_141836.png
-rw-r--r--  1 tim  staff  357467 Apr 24 14:18 iris_pairplot_20250424_141819.png

(py3ml) tim@Tims-MBP machine-learning % pytest ./test_iris.py 
=================================================== test session starts ====================================================
platform darwin -- Python 3.11.6, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/tim/Documents/workspace/python3/machine-learning
collected 19 items                                                                                                         

test_iris.py ...................                                                                                     [100%]

============================================== 19 passed in 72.12s (0:01:12) ===============================================
(py3ml) tim@Tims-MBP machine-learning % pytest ./test_iris.py -v
=================================================== test session starts ====================================================
platform darwin -- Python 3.11.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/tim/Desktop/Work/Python_Practice/py3ml/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/tim/Documents/workspace/python3/machine-learning
collected 19 items                                                                                                         

test_iris.py::test_load_dataset PASSED                                                                               [  5%]
test_iris.py::test_train_rfc_model PASSED                                                                            [ 10%]
test_iris.py::test_train_rfc_model_pipeline PASSED                                                                   [ 15%]
test_iris.py::test_train_rfc_model_predictions PASSED                                                                [ 21%]
test_iris.py::test_train_rfc_model_best_params PASSED                                                                [ 26%]
test_iris.py::test_evaluate_rfc_model PASSED                                                                         [ 31%]
test_iris.py::test_measure_model PASSED                                                                              [ 36%]
test_iris.py::test_save_rfc_model PASSED                                                                             [ 42%]
test_iris.py::test_evaluate_rfc_classification_report PASSED                                                         [ 47%]
test_iris.py::test_train_svc_model PASSED                                                                            [ 52%]
test_iris.py::test_train_svc_model_pipeline PASSED                                                                   [ 57%]
test_iris.py::test_train_svc_model_predictions PASSED                                                                [ 63%]
test_iris.py::test_train_svc_model_best_params PASSED                                                                [ 68%]
test_iris.py::test_evaluate_svc_model PASSED                                                                         [ 73%]
test_iris.py::test_save_svc_model PASSED                                                                             [ 78%]
test_iris.py::test_evaluate_svc_classification_report PASSED                                                         [ 84%]
test_iris.py::test_debug PASSED                                                                                      [ 89%]
test_iris.py::test_print_dataset_info PASSED                                                                         [ 94%]
test_iris.py::test_load_dataset_error PASSED                                                                         [100%]

============================================== 19 passed in 93.27s (0:01:33) ===============================================

(py3ml) tim@Tims-MBP machine-learning % ./clean_output.py 
(py3ml) tim@Tims-MBP machine-learning % ls -lt | head -7
total 10488
-rw-r--r--    1 tim  staff     6021 Apr 24 14:25 README.Iris.txt
drwxr-xr-x@ 103 tim  staff     3296 Apr 24 14:22 output
drwxr-xr-x@   4 tim  staff      128 Apr 24 14:19 __pycache__
-rwxr-xr-x    1 tim  staff     6231 Apr 24 14:18 test_iris.py
-rwxr-xr-x    1 tim  staff     7142 Apr 24 14:12 iris.py
-rwxr-xr-x    1 tim  staff      450 Apr 24 13:37 clean_output.py
(py3ml) tim@Tims-MBP machine-learning % ls -lt output | head -7
total 30264
-rw-r--r--  1 tim  staff  357467 Apr 24 14:22 iris_pairplot_20250424_142049.png
-rw-r--r--  1 tim  staff   81454 Apr 24 14:22 iris_svc_confusion_matrix_20250424_142204.png
-rw-r--r--  1 tim  staff   81454 Apr 24 14:22 iris_svc_confusion_matrix_20250424_142202.png
-rw-r--r--  1 tim  staff   79992 Apr 24 14:21 iris_rfc_confusion_matrix_20250424_142140.png
-rw-r--r--  1 tim  staff   79992 Apr 24 14:21 iris_rfc_confusion_matrix_20250424_142119.png
-rw-r--r--  1 tim  staff  357467 Apr 24 14:20 iris_pairplot_20250424_141932.png

