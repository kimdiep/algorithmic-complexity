from collections import Counter
# Given a list of words, find all words that appear more than once.

def find_duplicates(arr):
  arr = Counter(arr)
  duplicate_list = [i for i, x in arr.items() if x > 1]
  return duplicate_list
