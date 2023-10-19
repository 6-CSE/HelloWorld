import java.security.SecureRandom;
import java.util.Scanner;

public class PasswordGenerator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get user preferences for the password
        System.out.print("Enter the length of the password: ");
        int length = scanner.nextInt();

        System.out.print("Include uppercase letters? (Y/N): ");
        boolean includeUppercase = scanner.next().equalsIgnoreCase("Y");

        System.out.print("Include lowercase letters? (Y/N): ");
        boolean includeLowercase = scanner.next().equalsIgnoreCase("Y");

        System.out.print("Include numbers? (Y/N): ");
        boolean includeNumbers = scanner.next().equalsIgnoreCase("Y");

        System.out.print("Include special characters? (Y/N): ");
        boolean includeSpecialChars = scanner.next().equalsIgnoreCase("Y");

        // Generate the password based on user preferences
        String password = generatePassword(length, includeUppercase, includeLowercase, includeNumbers, includeSpecialChars);

        // Display the generated password
        System.out.println("Generated Password: " + password);

        scanner.close();
    }

    private static String generatePassword(int length, boolean includeUppercase, boolean includeLowercase,
                                           boolean includeNumbers, boolean includeSpecialChars) {
        String uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
        String numberChars = "0123456789";
        String specialChars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?";

        StringBuilder validChars = new StringBuilder();
        if (includeUppercase) {
            validChars.append(uppercaseChars);
        }
        if (includeLowercase) {
            validChars.append(lowercaseChars);
        }
        if (includeNumbers) {
            validChars.append(numberChars);
        }
        if (includeSpecialChars) {
            validChars.append(specialChars);
        }

        if (validChars.length() == 0) {
            System.out.println("Error: You must include at least one type of character.");
            System.exit(1);
        }

        SecureRandom random = new SecureRandom();
        StringBuilder password = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(validChars.length());
            password.append(validChars.charAt(randomIndex));
        }

        return password.toString();
    }
}
