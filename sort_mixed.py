#https://stackoverflow.com/questions/43854259/sort-mixed-python-list-in-cointaining-data-type-order/43854510
#sort v2: sort all words in alphabetical order and all integers in numerical order
# sort based on the positions in list of the strings and integers; it will sort based on those group types

def sort_mixed(arr):
  # Collect the values by type
  d = {}
  for x in arr:
    d.setdefault(type(x), []).append(x)
  # Sort each type
  d = {k: iter(sorted(v)) for k, v in d.items()}
  # The result list
  result = (next(d[type(x)]) for x in arr)
  return list(result)