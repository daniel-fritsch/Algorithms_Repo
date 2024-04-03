// Bubble Sort Algorithm

// This is a simple implementation of the bubble sort algorithm. Bubble sort 
// goes though a list comparing two elements and swapping them if necessary. It 
// iterates until the list is sorted. 

#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    // repeatedly compare two items within list
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            // flip if necessary
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// sample functions for using the sorting algorithm in practice. 
void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// main function to sort a given sample array. 
int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Array before sorting: \n");
    printArray(arr, n);
    bubbleSort(arr, n);
    printf("Array after sorting: \n");
    printArray(arr, n);
    return 0;
}
