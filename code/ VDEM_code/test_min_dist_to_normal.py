#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (23T3) 

You can use this file to test your min_dist_to_normal().

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import min_dist_to_normal as dist_to_normal

# %% Tests 
test_index = 0 # Can be 0, 1 or 2 

if test_index == 0:
    measurements = [2.1, 3.1]
    measurements_normal_all = [[3.3, 4.2], [2.4, 3.2], [4.2, 1.7]]
    weights = [1, 0.86]
    expected_answer = 0.314
elif test_index == 1: 
    measurements = [12.1, 23.1, 134.5]
    measurements_normal_all = [[25.3, 34.2, 146.7], 
                        [10.2, 25.5, 115.8],
                        [41.4, 13.2, 152.8],
                        [14.3, 28.6, 129.7]]
    weights = [1, 0.85, 0.23]
    expected_answer = 5.9876
elif test_index == 2: 
    measurements = [27.1, 86.1, 12.4, 23.5]
    measurements_normal_all = [[29.3, 68.2, 21.7, 43.6]]
    weights = [1, 0.7, 1.2, 0.9]
    expected_answer = 26.3917

# %% Run the function and check the answers     
    
your_answer = dist_to_normal.min_dist_to_normal(
                  measurements, measurements_normal_all, weights)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

TOL = 1e-3 # Maximum allowed deivation 
comparison_output = abs(your_answer-expected_answer) <= TOL 

if comparison_output:
    print('Your answer is within the expected tolerance')
else:
    print('Your answer is NOT within the expected tolerance')        
        

