#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (23T3) 

You can use this file to test your fault_detection_main(). All tests in 
this file are expected to return a string. 

This file containing five test cases which you can choose by
adjusting the variable test_index in Line 19. 

You can use this file to come out with additional tests. 
"""

# %% import 
import fault_detection_main as detect

# %% Tests 
test_index = 0 # Can be 0, 1, 2 or 3

if test_index == 0:
    measurements_normal_all = [[405.6, 36.1],
                               [595.0, 52.7],                           
                               [791.3, 72.4],
                               [995.5, 86.0]]    
    measurements_over_time = [[790.1, 68.1],
                              [812.2, 71.3],
                              [767.1, 67.2],
                              [799.2, 20.5],
                              [816.7, 22.4],
                              [778.4, 18.3]]
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6]
    weights = [1, 16]
    threshold = 45
    expected_answer = 'inconsistent number of time points'

if test_index == 1:
    measurements_normal_all = [[405.6, 36.1],
                               [595.0, 52.7],                           
                               [791.3, 72.4],
                               [995.5, 86.0]]    
    measurements_over_time = [[790.1, 68.1],
                              [812.2, 71.3],
                              [767.1, 67.2],
                              [799.2, 20.5],
                              [816.7, 22.4],
                              [778.4, 18.3]]
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6]
    weights = [1, 16]
    threshold = -6
    expected_answer = 'inconsistent number of time points'

if test_index == 2:
    measurements_normal_all = [[405.6, 36.1],
                               [595.0, 52.7],                           
                               [791.3, 72.4],
                               [995.5, 86.0]]    
    measurements_over_time = [[790.1, 68.1],
                              [812.2, 71.3],
                              [767.1, 67.2],
                              [799.2, 20.5],
                              [816.7, 22.4],
                              [778.4, 18.3]]
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6, 2.9]
    weights = [1, 16]
    threshold = [45]
    expected_answer = 'invalid threshold'
    
elif test_index == 3: 
    measurements_normal_all = [[405.6, 36.1],
                               [595.0, 52.7],                           
                               [791.3, 72.4],
                               [995.5, 86.0]]    
    measurements_over_time = [[790.1, 68.1],
                              [812.2, 71.3],
                              [767.1, 67.2],
                              [799.2, 20.5],
                              [816.7, 22.4],
                              [778.4, 18.3]]
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6, 2.9]
    weights = [1, 16]
    threshold = -6.1
    expected_answer = 'invalid threshold'

# %% 

your_answer = detect.fault_detection_main(time_list, measurements_over_time, 
                  measurements_normal_all, weights, threshold)

print('Your function returns:',your_answer)
print('The expected answer is:',expected_answer)

try:    
    if your_answer.lower() == expected_answer:
        print('Your answer is correct')
    else:
        print('Your answer is NOT correct')  
except:
    print('Your answer is NOT correct.')
    print('Possibly because your answer is not a string.')