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


'''
******** Ferromagnetic chain ********

1. Try to make an anti-ferromagnetic chain
2. What happens when you add linear biases on either end of a ferromagnetic chain?
3. What happens when you modify the J's so they aren't all the same value?
'''

from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector


# Modifiable parameters
num_qubits = 10                        # Number of qubits in our chain
fm_qubit_bias = [0] * num_qubits       # List of biases to apply to each qubit in our chain
fm_coupler_strength = -1               # The coupling we want to apply to two adjacent qubits

# Ising model parameters
h = fm_qubit_bias
J = {}

for i in range(num_qubits-1):
    J[(i, i+1)] = fm_coupler_strength

# Submit the problem to the QPU
sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
sampleset = sampler.sample_ising(h, J, num_reads=10)

inspector.show(sampleset)

print("Ferromagetic QPU response")
print(sampleset)