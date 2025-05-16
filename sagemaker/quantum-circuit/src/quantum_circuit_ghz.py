#!/usr/bin/env python

from braket.aws import AwsDevice
from braket.circuits import Circuit

# Create a 3-qubit GHZ circuit
circuit = Circuit()
circuit.h(0)  # Hadamard on qubit 0
circuit.cnot(0, 1)  # CNOT between qubits 0 and 1
circuit.cnot(1, 2)  # CNOT between qubits 1 and 2

# Select the Braket simulator
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

# Run the circuit
task = device.run(
    circuit,
    s3_destination_folder=('amazon-braket-my-quantum-output-20250514-kerstarsoc', 'quantum-output'),
    shots=1000
)
print("Task ID:", task.id)

# Get the result
result = task.result()
print("Measurement counts:", result.measurement_counts)
