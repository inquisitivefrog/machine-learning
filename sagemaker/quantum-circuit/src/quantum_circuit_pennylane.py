#!/usr/bin/env python

import pennylane as qml
dev = qml.device(
    'braket.aws.qubit',
    device_arn='arn:aws:braket:::device/quantum-simulator/amazon/sv1',
    s3_destination_folder=('amazon-braket-my-quantum-output-20250514-kerstarsoc', 'quantum-output'),
    shots=1000,
    wires=2  # Specify the number of qubits
)
@qml.qnode(dev)
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.CNOT(wires=[0, 1])
    #return qml.expval(qml.PauliZ(1))
    return qml.counts()
print(circuit([0.5, 0.3]))
