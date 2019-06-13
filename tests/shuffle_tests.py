import pytest
import sys
sys.path.append('./')
from shuffle import *

# assumption made that array (list) input will not be empty []

def test_shuffle_for_empty_string():
  arr = ['']
  assert type(random_shuffle(arr)) is list

def test_shuffle_for_list_of_integers():
  arr = [1,2,3,4,5]
  assert type(random_shuffle(arr)) is list
  
def test_shuffle_for_list_of_strings():
  arr = ['1','2','3','4','5']
  assert type(random_shuffle(arr)) is list

def test_shuffle_for_list_of_strings_and_integers():
  arr = ['1',2,'3',4,5]
  assert type(random_shuffle(arr)) is list

def test_shuffle_for_list_of_strings_and_integers_with_words():
  arr = ['car', 'truck', 8, 4, 'bus', 6, 1]
  assert type(random_shuffle(arr)) is list
