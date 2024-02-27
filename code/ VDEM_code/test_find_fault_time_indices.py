#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (23T3) 

You can use this file to test your find_fault_time_indices().

This file containing four test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_fault_time_indices as find_indices

# %% Tests 
test_index = 0 # Can be 0, 1, 2 or 3

if test_index == 0:
    measurements_over_time = [[2.1, 4.1],
                              [2.2, 4.3],
                              [2.1, 4.2],
                              [2.2, 4.5],
                              [2.2, 4.4],
                              [2.1, 4.3]]
    measurements_normal_all = [[2.3, 4.2], [2.5, 4.0], [2.1, 4.4], [2.4, 4.1]]
    weights = [1, 0.86]
    threshold = 0.5 
    expected_answer = []
elif test_index == 1:
    measurements_over_time = [[2.1, 4.1],
                              [2.2, 4.3],
                              [2.1, 4.2],
                              [4.2, 5.5],
                              [4.2, 5.4],
                              [2.1, 4.3]]
    measurements_normal_all = [[2.3, 4.2], [2.5, 4.0], [2.1, 4.4], [2.4, 4.1]]
    weights = [1, 0.86]
    threshold = 0.5 
    expected_answer = [3, 4]
elif test_index == 2:
    measurements_over_time = [[5.1, 2.1],
                              [2.2, 4.3],
                              [4.1, 2.2],
                              [2.2, 4.5],
                              [2.2, 4.4],
                              [1.1, 5.3]]
    measurements_normal_all = [[2.3, 4.2], [2.5, 4.0], [2.1, 4.4], [2.4, 4.1]]
    weights = [1, 0.86]
    threshold = 0.5 
    expected_answer = [0, 2, 5]
elif test_index == 3: 
    measurements_over_time = [[23.1, 23.1, 144.5],
                              [23.2, 24.1, 141.4],
                              [20.7, 25.2, 123.7],
                              [23.2, 23.7, 147.4],
                              [13.2, 24.6, 121.9],                              
                              [24.2, 25.1, 141.4]]
    measurements_normal_all = [[25.3, 24.2, 146.7], 
                        [21.2, 25.5, 145.8],
                        [21.4, 23.2, 152.8],
                        [24.3, 28.6, 149.7]]
    weights = [1, 0.85, 0.23]
    threshold = 3.7
    expected_answer = [2, 4]


# %% Run the function and check the answers     
    
your_answer = find_indices.find_fault_time_indices(
                   measurements_over_time, measurements_normal_all,
                   weights, threshold)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if your_answer == expected_answer:
    print('Your answer matches the expected answer')    
else:
    print('Your answer does NOT match the expected answer')        

