#!/usr/bin/env python
# coding: utf-8

# # Creating reusable applications
# 
# Having a program with hard-coded values limits its flexibility. Your first officer likes the program you built to convert parsecs to lightyears, but wants the ability to specify a value for parsecs. She wants you to create a program which can accept user input.
# 
# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.
# 
# ## Accepting user input
# 
# In the prior exercise you created code to convert parsecs to lightyears and display the results, which looked like the following:
# 
# ```python
# parsecs = 11
# lightyears = parsecs * 3.26
# print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")
# ```
# 
# Using this code as a foundation, update how `parsecs` is set. Start by creating a variable named `parsecs_input` and setting it to the result of `input`, which should prompt the user to enter the number of parsecs. Then convert `parsecs_input` to an integer by using `int` and storing it in `parsecs`. Finish by performing the calculation and displaying the result.

# In[1]:


# Enter code below
parsecs_input = input('Number of parsecs:')
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


# Your code should look something like the following:
# 
# ```python
# parsecs_input = input("Input number of parsecs:")
# parsecs = int(parsecs_input)
# lightyears = 3.26156 * parsecs
# 
# print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")
# ```
# 
# 
