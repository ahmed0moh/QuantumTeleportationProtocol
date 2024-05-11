from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer 
from qiskit.visualization import plot_histogram

qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')

#Quantum Circuit
qc = QuantumCircuit(qr, cr)

#EPR Server
qc.h(qr[1])
qc.cx(qr[1], qr[2])

# Alice Side incoding
qc.cx(qr[0], qr[1])
qc.h(qr[0])

# Measure qubits 0 and 1
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

# Bob side decoding
qc.x(qr[2]).c_if(cr[1], 1)
qc.z(qr[2]).c_if(cr[0], 1)

# Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Transpile the circuit for the simulator
tqc = transpile(qc, simulator)

# Run the transpiled circuit on the simulator
job = simulator.run(tqc, shots=1)


# Grab the results from the job
result = job.result()

# Get the counts (measurement results)
counts = result.get_counts(qc)
print(counts)

# Plot the results
plot_histogram(counts)