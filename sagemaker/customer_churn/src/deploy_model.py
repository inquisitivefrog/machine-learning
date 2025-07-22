predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium"
)
predictor.delete_endpoint()
