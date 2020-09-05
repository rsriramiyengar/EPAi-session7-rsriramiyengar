import random
import math
from random import randint
from functools import partial
from functools import reduce

vowels = ['a', 'e', 'i', 'o', 'u']
cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X', 'Y', 'Z']

fibonacci_number_list=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

def function_1_fibonacci_list(l1: 'List1') -> 'Returns List with only fibonaci number':
    """
    This function only returns only fibonacci numbers from a given list
    """
    return list(filter(lambda a:a if a in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765] else [],l1))


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

def function_3_paragraph_profanity_check(para:'Paragraph of text to be check'):
    """
    This Function checks for input paragraph does not contain any profanity
    """
    f = open("profanity_words_list.txt", "r")
    content_profanity = f.read()
    f.close()
    return set([True if p in content_profanity else False for p in ' '.join(para).split()])


def function_4_1_even_addition(l1: 'list of number for addition') -> 'sum of even numbers':
    """
    This function returns sum of even number in given list
    """
    return reduce(lambda a,b:(a if a%2==0 else 0) + (b if b%2==0 else 0),l1)


def function_4_2_biggest_acii_char(l1: 'string') -> 'largest printable printable ascii characters':
    """
    This function  returns largest printable printable ascii characters from a given string
    """
    return reduce(lambda a,b:a if ord(a)>ord(b) else b,*l1)


def function_4_3_third_element_addition(l1: 'List of Number') -> 'sum of every 3rd element in list':
    """
    This function returns sum of every 3rd element in list
    """
    return reduce(lambda a,b:a+b,l1[2::3])


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




