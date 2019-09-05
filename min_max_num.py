# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:21:09 2019

@author: creddersen
"""
"""
    From a string of numbers, find the min and max numbers
    then return the two numbers as a single string of two separate numbers
"""
def high_and_low(numbers):
#Convert string of numbers to a list 
    for x in numbers:
        num_list = numbers.split()
        
#convert list containing string of numbers to a list of integers
    number_list = []
    for num in num_list:
        number = int(num)
        number_list.append(number)
        
#Find the min and max integer, and convert back to a string
    h_num = str(max(number_list))
    l_num = str(min(number_list))
#Make two separate strings into one string   
    numbers = h_num + " " + l_num
#return that string    
    return numbers
    
