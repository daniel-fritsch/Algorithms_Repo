# necessary import
import random

# check if array is sorted
def sorted(arr):

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# bogo sort function
def bogo_sort(arr):
    while not sorted(arr):
        random.shuffle(arr)

# Sample use: 
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bogo_sort(arr)
print("Sorted array:", arr)
