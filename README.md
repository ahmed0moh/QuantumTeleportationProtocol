# 🌀 Quantum Teleportation with Qiskit

This project is a basic implementation of the *Quantum Teleportation Protocol* using [Qiskit](https://qiskit.org/), IBM's open-source quantum computing framework.  
It serves as a practical exercise to understand how quantum teleportation works at the circuit level.

---

## 📌 What is Quantum Teleportation?

*Quantum teleportation* is the transfer of quantum information (a qubit state) from one location (Alice) to another (Bob), using entanglement and classical communication — without physically sending the qubit itself.

It is not science fiction! It relies on quantum entanglement and measurement.

> 🔗 Learn more:  
> - [IBM Quantum – Teleportation Explained](https://quantum-computing.ibm.com/docs/learn/quantum-teleportation)  
> - [Wikipedia - Quantum Teleportation](https://en.wikipedia.org/wiki/Quantum_teleportation)

![Quantum Teleportation Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Quantum_teleportation.svg/800px-Quantum_teleportation.svg.png)
> Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Quantum_teleportation.svg)

---

## 📜 Code Overview

The protocol involves three qubits:
- q0: The qubit to teleport (Alice's qubit)
- q1: Entangled with q2 (shared between Alice and Bob)
- q2: The target qubit (Bob's qubit)

Steps:
1. *Entanglement*: Create an EPR pair between q1 and q2.
2. *Encoding*: Alice performs a CNOT and Hadamard gate to entangle her qubit with the EPR pair.
3. *Measurement*: Alice measures her qubits and sends the classical bits to Bob.
4. *Decoding*: Bob applies conditional gates (X and Z) based on Alice’s measurement.

---

## ▶ How to Run

### 📦 Prerequisites

Make sure you have:
- Python 3.7+
- qiskit installed

```bash
pip install qiskit

🧪 Execute the Code

python teleportation.py

You should see a printed result like:

{'011': 1}

And a histogram plot showing the output state.


---

📊 Output Example

The result will be a histogram of measurement results, similar to:



> Source: Qiskit Documentation




---

📂 Project Structure

.
├── teleportation.py       # Main code implementing teleportation
├── README.md              # This file


---

🎓 Learn More

📘 Qiskit Tutorials

🧪 Qiskit Textbook: Teleportation

🎥 Intro to Quantum Teleportation Video (CC0)



---

🪪 License

This project is provided for educational purposes under the MIT License.


---

🙋‍♂ Author

Developed as a personal learning experiment by Ahmed Dakrory
Feel free to fork or contribute!
