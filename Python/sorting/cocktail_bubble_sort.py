# cocktail shaker sort is a variation of bubble sort where 
# elements are sorted in both directions. First from the beginning
# to the end and then from the end to the beginning. 


def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False

        # bubble sort from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # bubble sort from right to left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1


# Sample 
arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_shaker_sort(arr)
print("Sorted array is:", arr)
