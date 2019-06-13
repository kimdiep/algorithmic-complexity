import pytest
import sys
sys.path.append('./')
from reverse_slicing import *

# assumption made that array input will not be empty []

def test_reverse_for_empty_string():
  arr = ['']
  assert reverse_slicing(arr) == ['']

def test_reverse_for_list_of_integers():
  arr = [1,2,3,4,5]
  assert reverse_slicing(arr) == [5,4,3,2,1]
  
def test_reverse_for_list_of_strings():
  arr = ['1','2','3','4','5']
  assert reverse_slicing(arr) == ['5','4','3','2','1']

def test_reverse_for_list_of_strings_and_integers():
  arr = ['2','1',6,5,'4',3]
  assert reverse_slicing(arr) == [3, '4', 5, 6, '1', '2']

def test_reverse_for_list_of_strings_and_integers_with_words():
  arr = ['car', 'truck', 8, 4, 'bus', 6, 1]
  assert reverse_slicing(arr) == [1, 6, 'bus', 4, 8, 'truck', 'car']
