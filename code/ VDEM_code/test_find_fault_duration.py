#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (23T3) 

You can use this file to test your find_fault_duration().

This file containing four test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_fault_duration as find_duration

# %% Tests 
test_index = 0 # Can be 0, 1, 2 or 3

if test_index == 0:
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6, 2.9]
    fault_time_indices = [1]
    expected_answer = 0.2
    
elif test_index == 1:
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6, 2.9]
    fault_time_indices = [2, 3]
    expected_answer = 0.6
    
elif test_index == 2:
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6, 2.9]
    fault_time_indices = [0, 1, 2]
    expected_answer = 0.6
    
elif test_index == 3: 
    time_list = [1.7, 1.9, 2.1, 2.4, 2.8]
    fault_time_indices = []
    expected_answer =  0


# %% Run the function and check the answers     
    
your_answer = find_duration.find_fault_duration(time_list, fault_time_indices)

print('Your function returns', your_answer)
print('The expected answer is', expected_answer)

TOL = 1e-3 # Maximum allowed deivation 
comparison_output = abs(your_answer - expected_answer) <= TOL 

if comparison_output:
    print('Your answer is within the expected tolerance')
else:
    print('Your answer is NOT within the expected tolerance')        
        
     

