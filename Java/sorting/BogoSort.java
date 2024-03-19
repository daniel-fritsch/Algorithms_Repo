// Simple implementation of bogo sort algorithm for highly inefficient sorting
// randomly shuffles an array of numbers and checks them until they are ordered. 

import java.util.Arrays;
import java.util.Random;

public class BogoSort {
    
    // check if sorted
    public static boolean Sorted(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return false;
            }
        }
        return true;
    }
    
    // randomly shuffle array
    public static void shuffle(int[] array) {
        Random rand = new Random();
        for (int i = 0; i < array.length; i++) {
            int randomIndexToSwap = rand.nextInt(array.length);
            int temp = array[randomIndexToSwap];
            array[randomIndexToSwap] = array[i];
            array[i] = temp;
        }
    }

    // Bogo Sort algorithm
    public static void bogoSort(int[] array) {
        while (!Sorted(array)) {
            shuffle(array);
        }
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}; // Example array
        System.out.println("Array before sorting: " + Arrays.toString(arr));
        
        bogoSort(arr);
        
        System.out.println("Array after sorting: " + Arrays.toString(arr));
    }
}
