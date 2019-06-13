import pytest
import sys
sys.path.append('./')
from sort import *

# assumption made that array input will not be empty []
# for this sort algorithm - can only handle single type lists

def test_sort_for_empty_string():
  arr = ['']
  assert sort(arr) == ['']

def test_sort_for_list_of_integers():
  arr = [1,3,4,2,5]
  assert sort(arr) == [1,2,3,4,5]
  
def test_sort_for_list_of_strings():
  arr = ['1','3','4','2','5']
  assert sort(arr) == ['1','2','3','4','5']

def test_sort_for_list_of_words_in_alphabetical_order():
  arr = ['car', 'truck', 'cookies', 'roll', 'bus', 'apple']
  assert sort(arr) == ['apple', 'bus', 'car', 'cookies', 'roll', 'truck']
