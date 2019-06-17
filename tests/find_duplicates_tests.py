import pytest
import sys
sys.path.append('./')
from find_duplicates import *

# assumption made that array input will not be empty []
# Assumption input type is list of strings
# Given a list of words, find all words that appear more than once.

def test_find_duplicates_no_duplicates():
  arr = ['']
  assert find_duplicates(arr) == []

def test_find_duplicates_no_duplicates_list():
  arr = ['a','b','c','d','e','f','g']
  assert find_duplicates(arr) == []

def test_find_duplicates_for_empty_strings():
  arr = ['','a','b','c','d','','e','f','g','']
  assert find_duplicates(arr) == ['']
  
def test_find_duplicates_for_list_of_strings():
  arr = ['1','3','4','2','5','2','5','4']
  assert find_duplicates(arr) == ['4','2','5']

def test_find_duplicates_for_list_of_words():
  arr = ['car', 'cookies', 'cookies', 'roll', 'bus', 'bus']
  assert find_duplicates(arr) == ['cookies', 'bus']
