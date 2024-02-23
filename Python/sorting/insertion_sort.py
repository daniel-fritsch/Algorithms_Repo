# simple and efficient insertion sort algorithm implemented in python


# insertion sort works by checking each element against the sorted portion before it
# and moving that element to where it belongs within the sorted portion if it is smaller 
# than elements within the sorted portion

# in one pass (1 is smaller than 5 so we move it back until it is in the right place):
# 4 5 1 9 10
# 4 1 5 9 10
# 1 4 5 9 10

def insertionSort(arr):
    length = len(arr) 
      
    if length <= 1:
        return  # if true the array must already be sorted 
    
    for i in range(1, length): 
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  
  
# Sorting example using the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
