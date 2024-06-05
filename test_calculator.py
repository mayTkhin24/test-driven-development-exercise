"""
Test Module for String Calculator
----------------------------------
    @author: [student's name] - [student's email]
    @date: [date of creation]
    @description: This test module is designed to test the functionality of the string calculator
             defined in the calculator.py module. Using pytest for testing allows for more
             concise and powerful test capabilities, which is integrated into the GitHub
             workflow for continuous integration and testing.
"""

import pytest
from calculator import add



def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5,2") == "7", "Failed on 5+2==7"
    assert add("2,3") == "5", "Failed on 2+3==5"

def test_zero_case():
    assert add("") == "0" , "Failed on empty string"

def test_malformed_input():
    assert add("1,a") == "Error: Input string is malformed or contains invalid characters.", "Failed on malformed input '1,a'"
    assert add("1,2,b") == "Error: Input string is malformed or contains invalid characters.", "Failed on malformed input '1,2,b'"

def test_non_numeric_input():
    assert add("one,two,three") == "Error: Input string is malformed or contains invalid characters.", "Failed on non-numeric input 'one,two,three'"

def test_only_delimiters():
    """
    Tests addition with input strings that contain only delimiters.
    """
    assert add(",") == "Error: Input string is malformed or contains invalid characters.", "Failed on only delimiters ','"
    assert add(",,,") == "Error: Input string is malformed or contains invalid characters.", "Failed on only delimiters ',,,'"

def test_hyphen_as_separator():
    """
    Tests addition with hyphen as a separator.
    """
    assert add("1-2-3") == "6", "Failed on hyphen separator '1-2-3'"
    assert add("1,2-3") == "6", "Failed on mixed separators '1,2-3'"

def test_single_number():
    """
    Tests addition with a single number.
    """
    assert add("5") == "5", "Failed on single number '5'"
    assert add("-5") == "-5", "Failed on single negative number '-5'"