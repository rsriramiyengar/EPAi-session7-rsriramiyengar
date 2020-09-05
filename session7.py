import random
import math

vowels = ['a', 'e', 'i', 'o', 'u']

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