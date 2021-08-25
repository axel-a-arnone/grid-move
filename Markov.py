# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 08:39:59 2021

@author: Axel Aleksandr Arnone

Written using Python 3.8.5

"""

import numpy as np

transition_matrix = [
    [-6,   3,   3],
    [ 4, -12,   8],
    [ 2,  16, -18]
    ]

state_vector = ["State 1", "State 2", "State 3"]

initial_state = "State 1"
simulation_length = 1000

rng = np.random.default_rng()

def evolve_state (current_state, state_vector, transition_matrix):
    
    state_index = state_vector.index(current_state)
    transition_vector = np.copy(transition_matrix[state_index])
    
    total_transition_rate = -1*transition_vector[state_index]
    holding_time = rng.exponential(total_transition_rate)
    
    # Zeroing probability to transition to current state
    transition_vector[state_index] = 0
    transition_vector = [x / sum(transition_vector) \
                            for x in transition_vector]
        
    new_state = rng.choice(state_vector, p = transition_vector)
    
    return new_state, holding_time


simulation_time = 0
current_state = initial_state


while simulation_time < simulation_length:
    
    new_state, holding_time = evolve_state(current_state, 
                                           state_vector, 
                                           transition_matrix)
    
    print ("System stayed in ", current_state, 
           " for ", holding_time, 
           " then moved to ",  new_state, "\n")
    
    current_state = new_state
    simulation_time += holding_time