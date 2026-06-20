import os
import sys
import math

def Bad_Name_Function( x,y ):
    """A poorly styled function"""
    Result = x+y
    return Result

def check_score(score):
    if score > 90:
        return "A"
    else:
        return "B"
    print("This line can never be reached!")

class missing_docstring:
    def __init__(self):
        self.Value = 10

def long_lines_calculator():
    very_long_variable_name_that_goes_on_and_on_and_is_completely_unnecessary = "This line is extremely long and will definitely trigger a line length limit violation in almost every default python linter configuration out there"
    return very_long_variable_name_that_goes_on_and_on_and_is_completely_unnecessary

undefined_variable = some_random_variable + 5

print(Bad_Name_Function(5,10))
