/*
 * 
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.


countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1

 */
public class countHi {
    public int counthi(String str) {
        // Base case: If the string is empty or too short to contain "hi", return 0
        if (str.length() < 2) {
            return 0;
        }

        // Check if the current substring starts with "hi"
        if (str.charAt(0) == 'h' && str.charAt(1) == 'i') {
            // If "hi" is found, add 1 and recurse with the rest of the string after "hi"
            return 1 + counthi(str.substring(2));
        } else {
            // If not "hi", just make a recursive call on the rest of the string
            return counthi(str.substring(1));
        }
    }

    public static void main(String[] args) {
        countHi counter = new countHi();
        
        // Test cases
        System.out.println(counter.counthi("xxhixx"));  // Output: 1
        System.out.println(counter.counthi("xhixhix")); // Output: 2
        System.out.println(counter.counthi("hi"));      // Output: 1
        System.out.println(counter.counthi("hihihi"));  // Output: 3
        System.out.println(counter.counthi("hixx"));    // Output: 1
        System.out.println(counter.counthi("x"));       // Output: 0
        System.out.println(counter.counthi(""));        // Output: 0
    }
}
