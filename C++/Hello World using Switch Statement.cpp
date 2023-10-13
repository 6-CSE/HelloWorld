#include <iostream>

int main() {
    int option = 1; // We use a variable to create a condition for the switch statement
    
    switch (option) {
        case 1:
            std::cout << "Hello, World!" << std::endl;
            break;
        default:
            std::cout << "Invalid option!" << std::endl;
            break;
    }
    
    return 0;
}
