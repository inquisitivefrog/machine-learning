#!/usr/bin/env python

from braket.aws import AwsDevice
from braket.circuits import Circuit
circuit = Circuit().h(0).rx(0, 0.5).cnot(0, 1).ry(1, 0.3)
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
result = device.run(circuit, s3_destination_folder=('amazon-braket-my-quantum-output-20250514-kerstarsoc', 'quantum-output'), shots=1000).result()
print(result.measurement_counts)

