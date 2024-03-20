# linear search implementation

# very simple search algorithm that looks through an array until an element is found. 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

# Example usage:
arr = [5, 8, 2, 10, 23, 15]
target = 10
result_index = linear_search(arr, target)

if result_index != -1:
    print(f"Element {target} found at index {result_index}.")
else:
    print(f"Element {target} not found in the array.")
