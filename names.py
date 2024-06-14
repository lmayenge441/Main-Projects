"""
File: names.py
Name: Lydia Mayenge
Date: 10/14/2020
Section: 10
Email: lmayeng1@umbc.edu
Description: To create functions, pass parameters, and implement scope into a working program.
"""
def sum_list(numbers):
# adds up all the integers & returns the sum
   sum = 0
   for x in numbers:
      sum = sum + x
   return sum
def get_string_lengths(strings):
   List= []
   for x in strings:
      List.append(len(x))
   return List
def get_names():
   words= []
   enter = input("Enter a name: ")
   if enter == 'STOP' or 'stop' or 'Stop':
         break
      words.append(enter)
   return words
