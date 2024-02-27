#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (23T3) 

You can use this file to test your fault_detection_main(). All tests in 
this file are expected to return a duration, not a string. 

This file contains four test cases which you can choose by
adjusting the variable test_index in Line 50. Note that 
- the test case with test_index 0 is the same as the sample code 
  in the assignment document 
- the test case with test_index 3 is a larger data set. There are 1000 sets
  of measurements from normal operation, and 304 sets of measurements that 
  require fault detection. The data for this test are in 3 external files:
      - measurements_normal_all.txt
      - measurements_over_time.txt
      - time_list.txt
  We expect these three files to be residing in the same folder as this
  test file and the code file.     

The data used in this test file are assumed to be irradiance and power. The 
last section of this file has code to plot the data so that you can 
visualise them. 

You can use this file to come out with additional tests. 

"""

# %% import 
import fault_detection_main as detect
import matplotlib.pyplot as plt 

# %% Function to load data set 
def load_data_from_file(file_name, output_type):
    with open(file_name, 'r') as file:
        file_contents = file.read().splitlines()
    
    if output_type == 'list_of_lists': 
        output_list = []
        for line in file_contents:
            output_list.append([float(num_str) for num_str in line.split()])
                
    if output_type == 'list':
        output_list = [float(num_str) for num_str in file_contents]
        
    return output_list

# %% Tests. Note: test_index 0 corresponds to the sample code 
test_index = 0 # Can be 0, 1, 2 or 3

# %% test_index 0
if test_index == 0:
    # Measurements collected from normal operation
    # The data sturcure is a list of lists
    # Each inner list contains measurements of irradiance and power 
    measurements_normal_all = [[405.6, 36.1],
                               [595.0, 52.7],                           
                               [791.3, 72.4],
                               [995.5, 86.0]]
    
    # Measurements collected from the current operation
    # Data structure is list of lists
    # Each inner list is collected at a time instant, and 
    # contains measurements of irradiance and power 
    measurements_over_time = [[790.1, 68.1],
                              [812.2, 71.3],
                              [767.1, 67.2],
                              [799.2, 20.5],
                              [816.7, 22.4],
                              [778.4, 18.3]]
    # The variable time_list contains the time instants at which the 
    # measurements in measurements_over_time were taken
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6, 2.9]
    
    # Two parameters used by the algorithm: weights and threshold 
    # Weights for computing distance
    weights = [1, 16]
    # Threshold for determining whether a fault has occurred
    threshold = 45
    
    # Expected answer
    expected_answer = 0.6

# %% test_index 1
if test_index == 1:
    # Note that the entries in the inner list are power and irradiance 
    measurements_normal_all = [[36.1, 405.6],
                               [52.7, 595.0],                           
                               [72.4, 791.3],
                               [86.0, 995.5]]
    
    measurements_over_time = [[68.1, 790.1],
                              [71.3, 812.2],
                              [43.8, 767.1],
                              [20.5, 799.2],
                              [22.4, 816.7],
                              [18.3, 778.4]]

    time_list = [1.7, 1.8, 2.3, 2.7, 3.3, 4.1]
    
    weights = [13.5, 1]
    
    threshold = 33.7
    
    # Expected answer
    expected_answer = 2.05

# %% test_index == 2
if test_index == 2:
    # Measurements collected from normal operation
    # The data sturcure is a list of lists
    # Each inner list contains measurements of irradiance and power 
    measurements_normal_all = [[405.6, 36.1],
                               [595.0, 52.7],                           
                               [791.3, 72.4],
                               [995.5, 86.0]]
    
    # Measurements collected from the current operation
    # Data structure is list of lists
    # Each inner list is collected at a time instant, and 
    # contains measurements of irradiance and power 
    measurements_over_time = [[790.1, 68.1],
                              [812.2, 71.3],
                              [767.1, 67.2],
                              [799.2, 70.5],
                              [816.7, 72.4]]
    # The variable time_list contains the time instants at which the 
    # measurements in measurements_over_time were taken
    time_list = [1.7, 1.8, 2.1, 2.5, 2.6]
    
    # Two parameters used by the algorithm: weights and threshold 
    # Weights for computing distance
    weights = [1, 16]
    # Threshold for determining whether a fault has occurred
    threshold = 45
    
    # Expected answer
    expected_answer = 0
# %% test_index is 3
if test_index == 3:
    measurements_normal_all = load_data_from_file(
                              'measurements_normal_all.txt', 'list_of_lists')

    measurements_over_time = load_data_from_file(
                              'measurements_over_time.txt', 'list_of_lists')
    
    time_list = load_data_from_file('time_list.txt', 'list')    

    weights = [1, 15.5]
    threshold = 27.4
    
    expected_answer = 85.595

# %% 

your_answer = detect.fault_detection_main(time_list, measurements_over_time, 
                  measurements_normal_all, weights, threshold)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

TOL = 1e-3 

try:    
    if abs(your_answer - expected_answer) < TOL:
        print('Your answer is correct')
    else:
        print('Your answer is NOT correct')  
except:
    print('Your answer is NOT correct.')
    print('Posssibly because your answer is not a number.')

# Plot the (irradiance,power) data for visualisation

# In order to do the plots, I need to put the irradiance and power data into
# a list of its own. The following function does that. 
def separate_irradiance_power_data(irradiance_power_data, test_index):
    # For test cases 0 and 2, the irradiance data are index 0 of
    # the inner list and power data are at index 1.
    # The order is the other way round for test case 2
    # 
    # Set up the index for irradiance and power
    if test_index in [0, 2, 3]:    
        IDX_IRRADIANCE = 0
        IDX_POWER = 1
    elif test_index == 1:
        IDX_IRRADIANCE = 1
        IDX_POWER = 0        

    # Extract the irradiance and power data from the list of list 
    irradiance_list = [irradiance_power_data[k][IDX_IRRADIANCE] 
                         for k in range(len(irradiance_power_data))]
    power_list = [irradiance_power_data[k][IDX_POWER] 
                    for k in range(len(irradiance_power_data))]

    return irradiance_list, power_list 

# Put the irradiance and power data in measurements_normal_all and
# measurements_over_time into list 
irradiance_normal, power_normal = \
    separate_irradiance_power_data(measurements_normal_all, test_index)

irradiance_current, power_current = \
    separate_irradiance_power_data(measurements_over_time, test_index)

fig1 = plt.figure()         
plt.plot(irradiance_normal,power_normal,'bs', label='Normal operation')     
plt.plot(irradiance_current,power_current,'m.', label='measurements_over_time',
         markersize="8")
plt.legend()
plt.xlabel('irradiance [W/m$^2$]')    
plt.ylabel('power [kW]')      
plt.title('PV characteristics') 
plt.show()


