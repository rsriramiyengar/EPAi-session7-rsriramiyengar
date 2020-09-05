import random
import math
from random import randint
from functools import partial

vowels = ['a', 'e', 'i', 'o', 'u']
cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X', 'Y', 'Z']

def function_2_1_sum_list(l1: 'List1', l2: 'List2') -> 'Returns List after sum':
    """
    This function adds element of 2 lists only when  element of list1 is even and element of list2 is odd.
    """
    return [a + b for a, b in zip(l1, l2) if a % 2 == 0 and b % 2 != 0]

def function_2_2_vowels_list(l1: 'string for checking') -> 'Return string after striping vowels':
    """
    This function strips the given string of all vowels.
    """
    return ["".join([a for a in l1 if a not in vowels])]


def function_2_3_1d_relu_list(l1: 'List of numbers') -> 'Relu output':
    """
    This function returns Relu function output for given List of numbers
    """
    return [a if a >= 0 else 0 for a in l1]

def function_2_4_1d_sigmoid_list(l1: 'List of numbers') -> 'Relu output':
    """
    This function returns Sigmoid function output for given List of numbers
    """
    return [(1 / (1 + math.exp(-a)) )for a in l1]

def function_2_5_acii_shifting(l1: 'string for shifting characters') -> 'shifted string':
    """
    This function returns List of string shifted by 5 character towards right for all small letters only
    """
    return ["".join([chr(ord(a)+5) if ord(a) <= 117 else chr(ord(a)+5-26) for a in l1])]


def function_5_number_plate_generator() -> 'Number Plate':
    """
    This function Generates Random plates for KA state  with RTO Location between 10 and 99 and series between AA and ZZ
    and series sub number between 1000 and 9999
    """
    return ['KA'+str(randint(10,99))+random.choice(cap_letters)+random.choice(cap_letters)+str(randint(1000,9999)) for x in range(15)]


def function_6_number_plate_generator_special(state:'State of registration',start:'start range',end :'end range') -> 'Number Plate':
    """
    This function Generates Random plates for Userdefined state state  with RTO Location between 10 and 99 and series between AA and ZZ
    and series sub number between user defined ranges
    """
    return [state+str(randint(10,99))+random.choice(cap_letters)+random.choice(cap_letters)+str(randint(start,end)) for x in range(15)]


function_6_number_plate_generator_special_partial=partial(function_6_number_plate_generator_special,start=1000,end=9999)
