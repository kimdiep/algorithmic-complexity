import pytest
import sys
sys.path.append('./')
from get_last import *

# assumption made that array input will not be empty []

def test_last_for_empty_string():
  arr = ['']
  assert last(arr) == ''

def test_last_for_list_of_integers():
  arr = [1,2,3,4,5]
  assert last(arr) == 5
  
def test_last_for_list_of_strings():
  arr = ['1','2','3','4','5']
  assert last(arr) == '5'

def test_last_for_list_of_strings_and_integers():
  arr = ['1',2,'3',4,5]
  assert last(arr) == 5
