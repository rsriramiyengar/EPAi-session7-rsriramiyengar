import pytest
import random
import string
import pytest

import session7
from  session7 import function_2_1_sum_list
from  session7 import function_2_2_vowels_list
from  session7 import function_2_3_1d_relu_list
from  session7 import function_2_4_1d_sigmoid_list
from  session7 import function_2_5_acii_shifting
from  session7 import function_4_1_even_addition
from  session7 import function_4_2_biggest_acii_char
from  session7 import function_4_3_third_element_addition
from  session7 import function_5_number_plate_generator
from  session7 import function_6_number_plate_generator_special
from  session7 import function_6_number_plate_generator_special_partial


import os
import inspect
import re
import math
import random
import decimal
from decimal import Decimal

cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X', 'Y', 'Z']


README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_2_1_sum_list():
    assert function_2_1_sum_list([2,4,10],[5,6,9])==[7,19],'Function is not working properly'

def test_function_2_2_vowels_list():
    assert function_2_2_vowels_list('tsai')==['ts'],'Function is not working properly'

def test_function_2_3_1d_relu_list():
    assert function_2_3_1d_relu_list([1,-10,0,20,15,-5])==[1,0,0,20,15,0],' List Relu Function is not working properly'

def test_function_2_4_1d_sigmoid_list():
    assert function_2_4_1d_sigmoid_list([1,-10,0,20,15,-5])==[0.7310585786300049, 4.5397868702434395e-05, 0.5, 0.9999999979388463, 0.999999694097773, 0.0066928509242848554],'List Sigmoid Function is not working properly'

def test_function_2_5_acii_shifting():
    assert function_2_5_acii_shifting('tsai')==['yxfn'],'List Function for string shifting is not working properly'

def test_function_4_1_even_addition_check():
    l1=[2,3,4,5,6,7]
    assert function_4_1_even_addition(l1)==12,'Reduce function for even addition not working properly'


def test_function_4_2_biggest_acii_char_check():
    l1=['ZORRO']
    assert function_4_2_biggest_acii_char(l1)=='Z','Reduce function for largest acii character  not working properly'

def test_function_4_3_third_element_addition_check():
    l1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    assert function_4_3_third_element_addition(l1)==30,'Reduce function for sum of third number  not working properly'

def test_function_5_number_plate_generator_state_check():
    l=function_5_number_plate_generator()
    state=[a[0:2] for a  in l]
    assert set(state)=={'KA'},'List Number plate generator for KA not working properly'

def test_function_5_number_plate_generator_rto_check():
    l=function_5_number_plate_generator()
    rto=[a[2:4] for a in l]
    rto_check=[True if int(a)>=10 and int(a)<=99 else False for a in rto]
    assert set(rto_check)=={True},'List Number plate generator for RTO not working properly'

def test_function_5_number_plate_generator_series_alpha_check():
    l=function_5_number_plate_generator()
    series_alpha1 = [a[4] for a in l]
    series_alpha2 = [a[5] for a in l]
    series_check=[True if a in cap_letters and b in cap_letters  else False for a,b in zip(series_alpha1,series_alpha2)]
    assert set(series_check)=={True},'List Number plate generator for Series not working properly'

def test_function_5_number_plate_generator_number_check():
    l=function_5_number_plate_generator()
    number=[a[6:] for a in l]
    number_check=[True if int(a)>=1000 and int(a)<=9999 else False for a in number]
    assert set(number_check)=={True},'List Number plate generator for number not working properly'


def test_function_6_number_plate_generator_special_state_check():
    start = 1000
    end = 9999
    l = function_6_number_plate_generator_special('DL', start, end)
    state=[a[0:2] for a  in l]
    assert set(state)=={'DL'},'List Number plate generator special for user defined state not working properly'

def test_function_6_number_plate_generator_special_rto_check():
    start=1000
    end=9999
    l=function_6_number_plate_generator_special('DL',start,end)
    rto=[a[2:4] for a in l]
    rto_check=[True if int(a)>=10 and int(a)<=99 else False for a in rto]
    assert set(rto_check)=={True},'List Number plate generator for RTO not working properly'

def test_function_6_number_plate_generator_special_alpha_check():
    start = 1000
    end = 9999
    l = function_6_number_plate_generator_special('DL', start, end)
    series_alpha1 = [a[4] for a in l]
    series_alpha2 = [a[5] for a in l]
    series_check=[True if a in cap_letters and b in cap_letters  else False for a,b in zip(series_alpha1,series_alpha2)]
    assert set(series_check)=={True},'List Number plate generator for Series not working properly'

def test_function_6_number_plate_generator_special_number_check():
    start = 1500
    end = 9000
    l = function_6_number_plate_generator_special('DL', start, end)
    number=[a[6:] for a in l]
    number_check=[True if int(a)>=start and int(a)<=end else False for a in number]
    assert set(number_check)=={True},'List Number plate generator for number not working properly'


def test_function_6_number_plate_generator_special_partial_state_check():
    l = function_6_number_plate_generator_special_partial('KA')
    state=[a[0:2] for a  in l]
    assert set(state)=={'KA'},'List Number plate generator special for user defined state not working properly'

def test_function_6_number_plate_generator_special_partial_rto_check():
    l = function_6_number_plate_generator_special_partial('KA')
    rto=[a[2:4] for a in l]
    rto_check=[True if int(a)>=10 and int(a)<=99 else False for a in rto]
    assert set(rto_check)=={True},'List Number plate generator for RTO not working properly'

def test_function_6_number_plate_generator_special_partial_alpha_check():
    l = function_6_number_plate_generator_special_partial('KA')
    series_alpha1 = [a[4] for a in l]
    series_alpha2 = [a[5] for a in l]
    series_check=[True if a in cap_letters and b in cap_letters  else False for a,b in zip(series_alpha1,series_alpha2)]
    assert set(series_check)=={True},'List Number plate generator for Series not working properly'

def test_function_6_number_plate_generator_special_partial_number_check():
    l = function_6_number_plate_generator_special_partial('KA')
    number=[a[6:] for a in l]
    number_check=[True if int(a)>=1000 and int(a)<=9999 else False for a in number]
    assert set(number_check)=={True},'List Number plate generator for number not working properly'

