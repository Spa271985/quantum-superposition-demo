# Quantum Superposition Demo (Qiskit)

This project demonstrates the fundamental concept of **quantum superposition** using a single qubit in Qiskit.

## 🧠 Physics Background

In quantum mechanics, a qubit can exist in a superposition of states:

|\psi⟩ = (|0⟩ + |1⟩)/√2

Applying a Hadamard gate (H) to the |0⟩ state creates this superposition.

Upon measurement, the qubit collapses probabilistically:
- 50% chance → |0⟩
- 50% chance → |1⟩

## ⚙️ What this project does

- Prepares a qubit in superposition
- Measures it multiple times
- Visualizes the probability distribution

## 💻 Technologies Used

- Python
- Qiskit
- NumPy
- Matplotlib

## 📊 Expected Output

Running the simulation with many shots (~1000) should produce:

| State | Probability |
|------|------------|
| 0    | ~50%       |
| 1    | ~50%       |

## 🚀 How to run

```bash
pip install -r requirements.txt
python superposition_demo.py
