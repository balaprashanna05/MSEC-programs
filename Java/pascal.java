import java.util.Scanner;

public class PascalsTriangle {
    public static void main(String[] args) {
        int rows = 6; // Change this value to print more rows
        printTriangle(rows);
    }

    public static void printTriangle(int numRows) {
        for (int i = 0; i < numRows; i++) {
            // Print formatting spaces for the pyramid shape
            for (int space = 0; space < numRows - i; space++) {
                System.out.print("  ");
            }
            
            int number = 1;
            for (int j = 0; j <= i; j++) {
                System.out.printf("%4d", number);
                // Calculate the next number using the current row ratio
                number = number * (i - j) / (j + 1);
            }
            System.out.println();
        }
    }
}
