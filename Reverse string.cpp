#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;

    // Input a string
    cout << "Enter a string: ";
    cin >> str;

    // Initialize an empty string to store the reversed string
    string reversedStr = "";

    // Reverse the string
    for (int i = str.length() - 1; i >= 0; i--) {
        reversedStr += str[i];
    }

    // Display the reversed string
    cout << "Reversed string: " << reversedStr << endl;

    return 0;
}
