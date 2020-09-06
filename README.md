# Readme File for Assignment for Session 7 Covering below mentioned concepts
### Created by Sriram Iyengar
## Session 7 - First Class Functions Part 2
- Map,Filter & Zip
- Reducing Function
- Partial Function
- The Operator Module
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### function_1_fibonacci_list (l1: 'List1') -> 'Returns List with only fibonaci number'
    """
    This function only returns only fibonacci numbers from a given list
    """

### function_2_1_sum_list (l1: 'List1', l2: 'List2') -> 'Returns List after sum'
    """
    This function adds element of 2 lists only when  element of list1 is even and element of list2 is odd.
    """
### function_2_2_vowels_list (l1: 'string for checking') -> 'Return string after striping vowels'
    """
    This function strips the given string of all vowels.
    """
### function_2_3_1d_relu_list (l1: 'List of numbers') -> 'Relu output'
    """
    This function returns Relu function output for given List of numbers
    """
### function_2_4_1d_sigmoid_list (l1: 'List of numbers') -> 'Relu output'
    """
    This function returns Sigmoid function output for given List of numbers
    """
### function_2_5_acii_shifting (l1: 'string for shifting characters') -> 'shifted string'
    """
    This function returns List of string shifted by 5 character towards right for all small letters only
    """
### function_3_paragraph_profanity_check (para:'Paragraph of text to be check')
    """
    This Function checks for input paragraph does not contain any profanity
    """
### function_4_1_even_addition (l1: 'list of number for addition') -> 'sum of even numbers'
    """
    This function returns sum of even number in given list
    """
### function_4_2_biggest_acii_char (l1: 'string') -> 'largest printable printable ascii characters'
    """
    This function  returns largest printable printable ascii characters from a given string
    """
### function_4_3_third_element_addition (l1: 'List of Number') -> 'sum of every 3rd element in list'
    """
    This function returns sum of every 3rd element in list
    """
### function_5_number_plate_generator () -> 'Number Plate'
    """
    This function Generates Random plates for KA state  with RTO Location between 10 and 99 and series between AA and ZZ
    and series sub number between 1000 and 9999
    """
### function_6_number_plate_generator_special (state:'State of registration',start:'start range',end :'end range') -> 'Number Plate':
    """
    This function Generates Random plates for Userdefined state state  with RTO Location between 10 and 99 and series between AA and ZZ
    and series sub number between user defined ranges
    """

### function_6_number_plate_generator_special_partial =partial(function_6_number_plate_generator_special,start=1000,end=9999)
    """
    This partial function Generates Random plates for Userdefined state state  with RTO Location between 10 and 99 and series between AA and ZZ
    and series sub number between 1000 and 9999.
    """

## Functions used in Test File
### test_readme_exists 
- checks if Readme files exists

### test_readme_contents length 
- checks the content length of  Readme file
### test_readme_proper_description 
- checks the content length of  Readme file

### test_readme_file_for_formatting 
- checks the formatting of  Readme file

### test_indentations 
- checks if the Assignment code is properly formated

### test_function_name_had_cap_letter 
- checks if the Assignment code is function has capital letters

### test_function_1_fibonacci_list 
- Checks if the fibonaci Function works properly or not

### test_function_2_1_sum_list 
- Checks the function  sum of two element list of for even number of List number and odd number of list 2.

### test_function_2_2_vowels_list 
- Checks the function if it strips vowels from given string.

### test_function_2_3_1d_relu_list 
- Checks the relu function works on given list

### test_function_2_4_1d_sigmoid_list 
- Checks the sigmoid function works on given list

### test_function_2_5_acii_shifting 
- checks the acii shifting function for small alphabets

### test_function_3_paragraph_profanity_check_True
- checks the profanity check if it can detect if paragraph is true

### test_function_3_paragraph_profanity_check_False
- checks the profanity check if it can detect if paragraph is False

### test_function_4_1_even_addition_check 
- checks the function of sum  even element from one list1 and odd element of list2 in sequence

### test_function_4_2_biggest_acii_char_check 
- checks the function biggest acii charter is working

### test_function_4_3_third_element_addition_check 
- checks the function for sum of  every third element of list is working

### test_function_5_number_plate_generator_state_check 
- Checks if  number plate  function returns correct state as KA for all element of list

### test_function_5_number_plate_generator_rto_check 
- Checks if  number plate  function returns correct RTO range of 10 to 99 for all element of list

### test_function_5_number_plate_generator_series_alpha_check 
- Checks if  number plate  function returns correct series in range of AA to ZZ for all element of list

### test_function_5_number_plate_generator_number_check 
- Checks if  number plate  function returns correct number series in range of 1000 to 9999 for all element of list


### test_function_6_number_plate_generator_special_state_check 
- Checks if  number plate  function returns correct user defined state as 'DL' for all element of list- Checks if  number plate  function returns correct state as KA for all element of list

### test_function_6_number_plate_generator_special_rto_check 
- Checks if  number plate  function returns correct RTO range of 10 to 99 for all element of list

### test_function_6_number_plate_generator_special_alpha_check 
- Checks if  number plate  function returns correct series in range of AA to ZZ for all element of list


### test_function_6_number_plate_generator_special_number_check 
- Checks if  number plate  function returns correct number series in user defined range between 1000 to 9999 for all element of list

### test_function_6_number_plate_generator_special_partial_state_check 
- Checks if  number plate  function returns correct user defined state as 'DL' for all element of list- Checks if  number plate  function returns correct state as KA for all element of list

### test_function_6_number_plate_generator_special_partial_rto_check 
- Checks if  number plate  function returns correct RTO range of 10 to 99 for all element of list

### test_function_6_number_plate_generator_special_partial_alpha_check 
- Checks if  number plate  function returns correct series in range of AA to ZZ for all element of list

### test_function_6_number_plate_generator_special_partial_number_check 
- Checks if  number plate  function returns correct number series locked of range between 1000 to 9999 for all element of list


***
> ![My Image](https://github.com/rsriramiyengar/EPAi-session7-rsriramiyengar/blob/master/images/Image01.JPG)
***

We are using python >3.8.3

The assignment is  tested by executing 'pytest -vv' , from python shell in same folder
