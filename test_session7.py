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
#from  session7 import function_2_5_acii_shifting
#from  session7 import function_2_5_acii_shifting
#from  session7 import function_2_5_acii_shifting
#from  session7 import function_2_5_acii_shifting
import os
import inspect
import re
import math
import random
import decimal
from decimal import Decimal


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
