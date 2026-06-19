import java.util.Scanner;

public class PascalsTriangle {
    public static void main(String[] args) {
        int rows = 6; 
        printTriangle(rows);
    }

    public static void printTriangle(int numRows) {
        for (int i = 0; i < numRows; i++) {
            for (int space = 0; space < numRows - i; space++) {
                System.out.print("  ");
            }
            
            int number = 1;
            for (int j = 0; j <= i; j++) {
                System.out.printf("%4d", number);
                number = number * (i - j) / (j + 1);
            }
            System.out.println();
        }
    }
}
