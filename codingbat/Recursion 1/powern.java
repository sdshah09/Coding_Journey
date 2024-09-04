/*Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27
 */
public class powern {
    public static int powerN(int base, int n) {
        if(n==0){
          return 1;
        }
        return base*powerN(base,n-1);
      }
      public static void main(String[] args) {
        // Test cases
        System.out.println("3^4 = " + powerN(3, 4));  // Output: 81
        System.out.println("2^5 = " + powerN(2, 5));  // Output: 32
        System.out.println("5^0 = " + powerN(5, 0));  // Output: 1
        System.out.println("7^3 = " + powerN(7, 3));  // Output: 343
    }
      
}
