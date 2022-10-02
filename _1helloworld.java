import java.util.*;

// import java.util.Scanner;
public class _1helloworld {

	public static void main(String[] args) {

		// Creates a reader instance which takes
		// input form standard input - keyboard
		Scanner reader = new Scanner(System.in);
		System.out.print("Enter a number: ");

		// nextInt() reads the next integer from the keyboard
		int number = reader.nextInt();

		// println() prints the following line to the output screen
		System.out.println("You entered: " + number);

		reader.close();
	}
}
