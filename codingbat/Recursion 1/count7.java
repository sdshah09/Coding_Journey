/*Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


count7(717) → 2
count7(7) → 1
count7(123) → 0
 */


 public class count7 {

    // Method to count the occurrences of digit 7
    public static int count7(int n) {
        // Base case: when n is 0
        if (n == 0) {
            return 0;
        }

        // Get the rightmost digit
        int x = n % 10;

        // If the rightmost digit is 7, add 1 and recurse on the remaining number
        if (x == 7) {
            return 1 + count7(n / 10);
        }

        // If the rightmost digit is not 7, just recurse on the remaining number
        return count7(n / 10);
    }

    // Main method to test the count7 function
    public static void main(String[] args) {
        // Test cases
        System.out.println(count7(717));  // Output: 2
        System.out.println(count7(7));    // Output: 1
        System.out.println(count7(123));  // Output: 0
        System.out.println(count7(777));  // Output: 3
    }
}
