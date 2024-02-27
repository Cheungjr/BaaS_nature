#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (23T3) 

You can use this file to test your dist_two_lists_of_measurements().

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import dist_two_lists_of_measurements as dist_2_lists

# %% Tests 
test_index = 0 # Can be 0, 1 or 2 

if test_index == 0:
    measurements_1 = [2.1, 3.1]
    measurements_2 = [2.3, 4.2]
    weights = [1, 0.86]
    expected_answer = 1.0395
elif test_index == 1: 
    measurements_1 = [12.1, 23.1, 134.5]
    measurements_2 = [25.3, 34.2, 146.7]
    weights = [1, 0.85, 0.23]
    expected_answer = 17.6975
elif test_index == 2: 
    measurements_1 = [27.1, 86.1, 12.4, 1.27]
    measurements_2 = [29.3, 68.2, 21.7, 1.46]
    weights = [1, 0.7, 0.8, 11.1]
    expected_answer = 17.2835

# %% Run the function and check the answers     
    
your_answer = dist_2_lists.dist_two_lists_of_measurements(measurements_1,
                      measurements_2, weights)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

TOL = 1e-3 # Maximum allowed deivation 
comparison_output = abs(your_answer-expected_answer) <= TOL 

if comparison_output:
    print('Your answer is within the expected tolerance')
else:
    print('Your answer is NOT within the expected tolerance')        
        

