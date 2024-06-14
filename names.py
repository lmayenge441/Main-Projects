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
   enter = input("Enter a name (or 'stop' to stop): ")
   if enter.lower() == 'stop':
      return
   elif enter:
      names = enter.split()
      if len(names) >= 1:
         print("Names in order:")
         for name in names:
            print(name)
      else:
         print("Please enter at least two names.")
      get_names()


get_names()
   #words.append(enter)
# #return words
