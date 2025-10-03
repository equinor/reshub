""" Example script to demonstrate linting and code formatting with Ruff."""

import xtgeo
from datetime import datetime
import sys
import os
import json



def example_function(parameter1, parameter2):
    """This function demonstrates various linting and formatting issues."""
    if parameter1==1: print("Parameter 1 is one")
    if parameter2==2:
        print("Parameter 2 is two")

    print("This is a very long line that is meant to demonstrate how Ruff can automatically format code and break it into multiple lines if it exceeds the maximum line length set in the configuration.")

    json_string='{"name":"John", "age": 30, "city": "New York"}'
    data=json.loads(json_string)

    a_number = 42

    return data

def example_function_many_parameters(parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7, parameter8, parameter9, parameter10):
    """A function that takes many parameters to demonstrate line breaking."""


    print(f"Parameters received: {parameter1}, {parameter2}, {parameter3}, {parameter4}, {parameter5}, {parameter6}, {parameter7}, {parameter8}, {parameter9}, {parameter10}")




def another_function():
    '''A function with no parameters.'''
    print('Hello, World!')

if __name__ == "__main__":
    example_function(1,2)
    example_function_many_parameters(1, 2,3, 4,5,6, 7, 8, 9,10)
    another_function()

