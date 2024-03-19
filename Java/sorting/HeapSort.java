// Heap Sort is a comparison based sorting technique.
// The unsorted array of numbers is compiled into a heap from which 
// the greatest element is extracted in succession until we have a new ordered array. 

import java.util.Arrays;

public class HeapSort {
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Build heap 
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // extract elements from heap
        for (int i = n - 1; i > 0; i--) {

            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }

    // heapify subtree 
    public static void heapify(int[] arr, int n, int i) {
        int largest = i; 
        int leftChild = 2 * i + 1; 
        int rightChild = 2 * i + 2; 

        if (leftChild < n && arr[leftChild] > arr[largest]) {
            largest = leftChild;
        }

        if (rightChild < n && arr[rightChild] > arr[largest]) {
            largest = rightChild;
        }

        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify
            heapify(arr, n, largest);
        }
    }

    // example instance of use
    public static void main(String[] args) {
        int[] arr = {12, 11, 1, 4, 12, 13, 5, 6, 7}; // Example array
        System.out.println("Array before sorting: " + Arrays.toString(arr));
        heapSort(arr);
        System.out.println("Array after sorting: " + Arrays.toString(arr));
    }
}
