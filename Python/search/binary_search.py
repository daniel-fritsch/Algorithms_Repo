# simple binary search implementation
# search algorithm for a sorted array

# binary search repeatedly divides the array in half until the target element is found. 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # division
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target found, return ind
        elif mid_val < target:
            low = mid + 1  # Target in right half
        else:
            high = mid - 1  # Target in  left half

    return -1  

# Sample:
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
result_index = binary_search(arr, target)

if result_index != -1:
    print(f"Element {target} found at index {result_index}.")
else:
    print(f"Element {target} not found in the array.")
