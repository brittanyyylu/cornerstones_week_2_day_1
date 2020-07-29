# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector

'''
******** Ferromagnetic chain ********

The goals of this exercise are:
1. Get comfortable with submitting problems to the QPU and visualize the solutions using 
    the problem inspector
2. Explore the probabilistic nature of the solutions
3. Explore the physical qubit parameters (local h biases and inter-qubit couplings J) in a
    linear chain

Suggested exercises:
1. What do you see if you run the problem multiple times? 
    What about if you increase the number of reads? 
2. Make an anti-ferromagnetic chain by changing the sign of fm_coupler_strength
3. What happens if you add a linear bias (h) on one end of the chain? This can be 
    done in either the ferromagnetic or antiferromagnetic case. How does the 
    strength of that bias affect your results? (for example, try h = 0.1, 0.5 and 1.0. 
    What happens to the number of solutions in each state and the energies?)
4. What happens if you multiply all of the h and J biases by the same factor (2x, 5x, 10x)?
    Do your solutions change? What about their energies? 
5. What happens if you ferromagnetically couple the chain, and impose opposite 
    h bias on each end of the chain? What if those biases have different magnitude?  

'''
# Modifiable parameters
num_qubits = 10                        # Number of qubits in our chain
fm_qubit_bias = [0] * num_qubits       # List of biases to apply to each qubit in our chain
fm_coupler_strength = -1               # The coupling we want to apply to two adjacent qubits
num_reads = 10                         # The number of times the QPU is sampled

# Ising model parameters
h = fm_qubit_bias
J = {}                                # coupling strength is specified using a dictionary

for i in range(num_qubits-1):
    J[(i, i+1)] = fm_coupler_strength

# Submit the problem to the QPU
sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
response = sampler.sample_ising(h, J, num_reads=num_reads)

# Show the problem visualization on the QPU
#inspector.show(response)

print("QPU response")
print(response)