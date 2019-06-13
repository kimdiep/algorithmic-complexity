import pytest
import sys
sys.path.append('./')
from sort_mixed import *

# assumption made that array input will not be empty []

def test_sort_for_empty_string():
  arr = ['']
  assert sort(arr) == ['']

def test_sort_for_list_of_integers():
  arr = [1,3,4,2,5]
  assert sort(arr) == [1,2,3,4,5]
  
def test_sort_for_list_of_strings():
  arr = ['1','3','4','2','5']
  assert sort(arr) == ['1','2','3','4','5']

def test_sort_for_list_of_strings_and_integers():
  arr = ['2','1',6,5,'4',3]
  assert sort(arr) == ['1', '2', 3, 5, '4', 6]

def test_sort_for_list_of_strings_and_integers_with_words():
  arr = ['car', 'truck', 8, 4, 'bus', 6, 1]
  assert sort(arr) == ['bus', 'car', 1, 4, 'truck', 6, 8]
