import sagemaker
from sagemaker.estimator import Estimator
from sagemaker.inputs import TrainingInput

session = sagemaker.Session()
estimator = Estimator(
    image_uri=sagemaker.image_uris.retrieve("xgboost", region="us-east-1", version="latest"),
    role="arn:aws:iam::084375569056:role/service-role/AmazonSageMaker-ExecutionRole-<new-timestamp>",
    instance_count=1,
    instance_type="ml.m5.large",
    output_path="s3://sagemaker-us-east-1-084375569056/output/",
    sagemaker_session=session
)
estimator.set_hyperparameters(
    max_depth=5,
    eta=0.2,
    gamma=4,
    min_child_weight=6,
    subsample=0.8,
    objective="binary:logistic",
    num_round=100
)
train_input = TrainingInput(
    s3_data="s3://sagemaker-us-east-1-084375569056/data/train_processed.csv",
    content_type="csv"
)
estimator.fit({"train": train_input})
