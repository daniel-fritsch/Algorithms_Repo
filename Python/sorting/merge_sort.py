# Python program for implementation of MergeSort
 
# merge sort works by dividing an array into two halves, sorting each of 
# those halves, and then putting the array back together. This process is repeated
# until the entire ray has been sorted successfully. 

# merge_sort main
def merge_sort(arr):
    if len(arr) < 2:
        print ("Array is already sorted")
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)


# merge function for knitting the arrays back together
def merge(left, right):
    merged = []
    i = j = 0
    
    # put the two arrays back together
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append remaining elements from left and right arrays
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Sample array example
arr = [5, 2, 8, 4, 1, 9, 3, 6, 7]
print(arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
