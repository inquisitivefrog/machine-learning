
Online Simulators: for testing and prototyping
-----------------
1. SV1 (34 qubits)
2. TN1 (50 qubits)
3. DM1 (17 qubits)

Online QPUs: real quantum hardware (per-task, per-shot charges)
-----------
1. IonQ Forte 1
2. Forete Enterprise 1 (36 qubits)
3. IQM Garnet (20 qubits)
4. QuEra Aquila (256 qubits)
5. Rigetti Ankaa-3 (82 qubits)

Offline QPUs: real quantum hardware (unuseable when offline)
------------
1. IonQ Aria 1
2. IonQ Aria 2 (25 qubits)

Cost Effective Strategy
1. Use SV1, TN1, or DM1 for algorithm development, debugging, and initial testing. Simulators are orders of magnitude cheaper than QPUs.

2. SV1 is suitable for most gate-based algorithms, while TN1 is optimized for larger circuits with sparse connectivity. DM1 is useful for noisy simulations but has a lower qubit count.


3. Reserve QPUs (e.g., IonQ Forte, Rigetti Ankaa-3) for final experiments or when quantum hardware is necessary (e.g., to test real quantum noise or hardware-specific features).


4. Check QPU availability before submitting tasks. Offline devices like Aria 1 and 2 can’t be used, so avoid queuing tasks for them unnecessarily.


5. Cost tip: QPUs like QuEra Aquila (analog mode) may have different pricing structures. Review the pricing for each provider in the AWS Braket console or documentation.



