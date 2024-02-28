// merge sort implementation in Java. 

// This algorithm works by recursively dividing an array, 
// sorting each half, and then putting them back together

// necessary imports
import java.util.Arrays;

public class MergeSort {
    public static void mergeSort(int[] arr) {
        if (arr == null || arr.length < 2) {
            return; 
        }
        int n = arr.length;
        int[] temp = new int[n]; 

        // main merge sort operations
        mergeSortMain(arr, 0, n - 1, temp);
    }

    // finds the middle of the array and uses recursion to sort the right and left halves
    private static void mergeSortMain(int[] arr, int low, int high, int[] temp) {
        if (low < high) {
            int mid = low + (high - low) / 2; 
            mergeSortMain(arr, low, mid, temp);
            mergeSortMain(arr, mid + 1, high, temp);

            // Merge the sorted halves
            merge(arr, low, mid, high, temp);
        }
    }

    // function responsible for merging the pieces back together 
    private static void merge(int[] arr, int lower, int middle, int high, int[] temp) {
        int i = lower; 
        int j = middle + 1; 
        int k = lower; 

        // Merge two subarrays
        while (i <= middle && j <= high) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        // Copy left subarray
        while (i <= middle) {
            temp[k++] = arr[i++];
        }

        // Copy right subarray
        while (j <= high) {
            temp[k++] = arr[j++];
        }

        // Copy elements back to original array
        for (k = lower; k <= high; k++) {
            arr[k] = temp[k];
        }
    }

    // sample situation. Sorts array arr
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        System.out.println("Original array: " + Arrays.toString(arr));
        mergeSort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}
