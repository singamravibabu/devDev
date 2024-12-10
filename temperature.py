'''This is a temperature module created on Dec. 5, 2024.
This module now conains two functions for temperature conversion.
Later we will add more functions to this module.'''

def to_celsius(fahrenheit):
    'Converts Fahrenheit to Celsius.'
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    'Converts Celsius to Fahrenheit.'
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit