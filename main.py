import string
import math

number_one = 23
number_two = 9


# Function definition on first line.
def add_two_numbers(number_one, number_two):
  return number_one + number_two  
  
  # Returns the sum of the numbers, and is indented by 2 spaces.

def add_two_numbers(number_one, number_two):
  result = number_one + number_two
  return result
def add_three_numbers_misformatted(number_one, number_two, number_three):
  result = number_one + number_two + number_three   
    # Indented by 4 spaces.
  return result     
  
#this was only indented by 3 spaces
def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.
        
        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number
        
        Takes number_one and raises it to the power of number_two, returning the result.
        """
        
        return number_one ** number_two

def number_to_the_power_of_default(number_one, number_two=2):
        """Raise a number to an arbitrary power.
        
        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number
        
        Takes number_one and raises it to the power of number_two, returning the result.
        """

        return number_one ** number_two