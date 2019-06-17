from random import randint

# using Fisher–Yates shuffle Algorithm
# shuffles a list

def random_shuffle(arr):
  arr_range = range(0, len(arr))
  for i in arr_range:
    j = randint(arr_range[0], arr_range[-1])
    arr[i], arr[j] = arr[j], arr[i]
  return arr

