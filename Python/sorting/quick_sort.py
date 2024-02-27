# python quicksort

# QuickSort is a recursive algorithm that partions an array to be
# sorted into two arrays, and sorts them independently in a recursive fashion. 


# partiotion function used to select the pivot and divide the function 
def partition(arr, low, high): 
    pivot = arr[high]  
    i = low - 1  

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# quick sort implementation
def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Sample use: 
arr = [10, 7, 8, 9, 1, 5]
length = len(arr)
quick_sort(arr, 0, length - 1)
print("Sorted array:", arr)
