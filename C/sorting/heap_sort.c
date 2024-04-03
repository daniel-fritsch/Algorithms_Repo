// Heap Sort implementation in C

// heap sort is a comparison sort algorithm that builds a heap 
// and then repeatedly extracts the maximum or minumum element 
// and adds it to the array, thereby sorting it. 

#include <stdio.h>

// Function to heapify a subtree 
void heapify(int arr[], int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1; 
    int right = 2 * i + 2; 

    // If child1 > root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // If child2 > previous largest
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest != root
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        // Recursively heapify
        heapify(arr, n, largest);
    }
}

// heap sort main
void heapSort(int arr[], int n) {
    // Build heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // sequentially extract elements from assembled heap
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        heapify(arr, i, 0);
    }
}

// Function to print array (for testing)
void printArray(int arr[], int n) {
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}

// Sample driver for potential use case. 
// Implement as needed for specific use case. 
int main() {
    int arr[] = {12, 11, 9, 7, 12, 1, 13, 5, 6, 7};
    int m = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: \n");
    printArray(arr, m);

    heapSort(arr, m);

    printf("Sorted array: \n");
    printArray(arr, m);
    return 0;
}
