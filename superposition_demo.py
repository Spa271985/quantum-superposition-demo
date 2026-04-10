from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1: Create quantum circuit
qc = QuantumCircuit(1, 1)

# Step 2: Apply Hadamard gate (creates superposition)
qc.h(0)

# Step 3: Measure the qubit
qc.measure(0, 0)

# Step 4: Print circuit
print("Quantum Circuit:")
print(qc)

# Step 5: Run simulation
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()

# Step 6: Get results
counts = result.get_counts(qc)
print("\nMeasurement Results:")
print(counts)

# Step 7: Plot histogram
plot_histogram(counts)
plt.title("Superposition Measurement Results")
plt.show()

# Step 8: Interpretation
print("\nInterpretation:")
print("The results show approximately equal probability for |0> and |1>,")
print("demonstrating quantum superposition and probabilistic measurement.")
