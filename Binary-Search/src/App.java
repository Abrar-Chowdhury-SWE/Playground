import java.util.Scanner;
public class App {
    public static int recursive(Integer target, Integer[] a, int lo, int hi, String indent) {
    
        //System.out.print(indent + "search("+key+",a,"+lo+","+hi+"); ");
        if (hi <= lo) return -1; // key is not present in array a
   
        int mid = lo + (hi - lo) / 2;
        System.out.println(indent + "(" + lo + "," + mid + "," + hi + ")");
        
        int cmp = a[mid].compareTo(target); // count this comparison (one array access)
        if (cmp == 0 ){
            System.out.println(indent+"found at: " + mid);
        return mid;
        } else if (cmp > 0) {
            // target is smaller than a[mid]
            return recursive(target, a, lo, mid, indent+"\t");
        } else {
            // target is greater than a[mid]
            return recursive(target, a, mid+1, hi, indent+"\t");
        } 
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);  // Create a Scanner object for user input
        Integer[] array = {3, 5, 9, 12, 15, 17};

        System.out.print("Enter target key: ");
        int key = stdIn.nextInt();  // Read an integer from the user

        recursive(key, array, 0, array.length, "");
        // iterative(key, array);  // You might want to uncomment this line if the method is defined
    }
}

