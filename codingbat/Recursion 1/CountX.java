public class CountX {

    // Method to count the number of 'x' characters in a string recursively
    public int countX(String str) {
        // Base case: If the string is empty, return 0
        if (str.isEmpty()) {
            return 0;
        }
        
        // Check the first character
        if (str.charAt(0) == 'x') {
            // If it's 'x', add 1 to the result of the recursive call on the rest of the string
            return 1 + countX(str.substring(1));
        } else {
            // If it's not 'x', just make a recursive call on the rest of the string
            return countX(str.substring(1));
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        CountX counter = new CountX();
        
        // Test cases
        System.out.println(counter.countX("xxhixx")); // Output: 4
        System.out.println(counter.countX("xhixhix")); // Output: 3
        System.out.println(counter.countX("hi")); // Output: 0
    }
}
