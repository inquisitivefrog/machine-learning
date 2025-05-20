#!/usr/bin/env python3
"""Run a hybrid quantum-classical job to create a GHZ state using AWS Braket."""

from braket.circuits import Circuit
from braket.jobs import hybrid_job
from botocore.exceptions import ClientError

@hybrid_job(
    device="arn:aws:braket:::device/quantum-simulator/amazon/sv1",
    role_arn="arn:aws:iam::084375569056:role/AmazonBraketJobsExecutionRole",
    job_name="run-ghz-hybrid",
    wait_until_complete=True
)
def run_ghz_hybrid():
    """Create a 3-qubit GHZ state and measure the probability of the |000> state.

    Returns:
        dict: A dictionary containing the probability of the |000> state.
    """
    circuit = Circuit().h(0).cnot(0, 1).cnot(1, 2)
    # Device is handled by the decorator, no need for AwsDevice
    result = circuit.run(shots=1000).result()
    counts = result.measurement_counts
    probability_000 = counts.get('000', 0) / 1000
    return {"probability_000": probability_000}

if __name__ == "__main__":
    try:
        job = run_ghz_hybrid()
        print(f"Job ARN: {job.arn}")
        print(f"Job Status: {job.state()}")
        result = job.result()
        print(f"Result: {result}")
    except ClientError as e:
        print(f"AWS Braket Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
