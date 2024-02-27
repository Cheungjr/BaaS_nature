#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 23T3 Assignment 1 

Template file for find_fault_duration()

@author:  
"""

def find_fault_duration(time_list, fault_time_indices):
    mids = []
    for i in range(len(time_list)):
        mid.append( (time_list[i]+time_list[i+1])/2 )
    duration = 0
    index = 0
    #3 cases to calculate time duration of each time_indices
    for j in range(len(fault_time_indices)):
        index = fault_time_indices[j]
        if index == 0:
            duration = duration + mid[index] - time_list[index]
        elif index == len(fault_time_indices):
            duration = duration + time_list[index] - mid[index]
        else:
            duration = duration + mid[index+1] - mid[index]
    return duration