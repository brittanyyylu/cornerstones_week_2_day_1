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
******** FM and AFM Bonus ********

Now that you've played around with the h's and J's, let's look at some annealing properties. By default
the will anneal for 20 us and will follow the schedule shown here:
https://docs.dwavesys.com/docs/latest/c_fd_as.html#anneal-schedule-variations

Leap allows you to change the length of time you anneal for and the shape of the energy waveform (or the 
anneal schedule). We support annealing times in the range of 1 us to 2 ms. 

The anneal schedule allows you to modify the way the QPU progresses through the anneal. The anneal trajectory is 
represented by s, where s=0 is the beginning of the anneal and s=1 is the end. By changing the time at which the QPU
ends up in a certain part of the anneal (s), you can change the shape of the energy waveform. For example, you can 
introduce a pause or finish the anneal really quick part way through (quench). 
Here's an example of how you would specify the default anneal schedule:
    default_anneal_schedule = [(0.0, 0.0), (20.0, 1)]
    
Let's say you want to change the anneal schedule so that in 15 us you are 40% of the way through the anneal. Then you
want to pause for 5 us and then progress through the remaining 60% of the anneal in another 10 us. This is how you would 
do it:
    new_anneal_schedule = [(0.0, 0.0), (15, 0.4), (20, 0.4), (30, 1)]

Investigate
    1. What happens to your FM or AFM chain when you lengthen or shorten the annealing time?
    2. What happens when you change the anneal schedule?
    3. What kinds of problems do you think would be more susceptible to changes in the anneal schedule?
'''

# Import packages
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector

# Modifiable parameters
num_qubits = 10                        # Number of qubits in our chain
fm_qubit_bias = [0] * num_qubits       # List of biases to apply to each qubit in our chain
fm_coupler_strength = -1               # The coupling we want to apply to two adjacent qubits

annealing_time = 20
anneal_schedule = [(0.0, 0.0), (20, 1)]

# Ising model parameters
h = fm_qubit_bias
J = {}

for i in range(num_qubits-1):
    J[(i, i+1)] = fm_coupler_strength

# Submit the problem to the QPU
#   NOTE: The annealing_time and annealing_schedule parameters are mutually exclusive. You can only use one at a time.
#         To use annealing_time:
#               response = sampler.sample_ising(h, J, annealing_time=annealing_time num_reads=10)
#         To use annealing_schedule:
#               response = sampler.sample_ising(h, J, annealing_schedule=annealing_schedule num_reads=10)
sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
sampleset = sampler.sample_ising(h, J, anneal_schedule=anneal_schedule, num_reads=100)

inspector.show(sampleset)

print("QPU response")
print(sampleset)