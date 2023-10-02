#include <stdio.h>

void printHelloWorld(int n) {
    if (n > 0) {
        printHelloWorld(n - 1); // Recursive call with n-1
    }
    if (n > 0) {
        printf("Hello, World!\n"); // Print "Hello, World!" n times
    }
}

int main() {
    int n;
    printf("Enter the number of times to print 'Hello, World!': ");
    scanf("%d", &n);

    if (n > 0) {
        printHelloWorld(n);
    } else {
        printf("Invalid input. Please enter a positive integer.\n");
    }

    return 0;
}
