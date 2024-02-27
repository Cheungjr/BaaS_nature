#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 23T3 Assignment 1 

Template file for fault_detection_main()

@author:  
"""

import find_fault_time_indices as find_indices
import find_fault_duration as find_duration

def fault_detection_main(time_list, measurements_over_time, 
                         measurements_normal_all, weights, threshold):
