#include <iostream>
using namespace std;

int main() {
    int row1, col1, row2, col2;

    cout << "Enter the number of rows and columns of the first matrix: ";
    cin >> row1 >> col1;

    cout << "Enter the number of rows and columns of the second matrix: ";
    cin >> row2 >> col2;

    
    if (col1 != row2) {
        cout << "Matrix multiplication is not possible. Columns of the first matrix must be equal to rows of the second matrix." << endl;
        return 1;
    }

    cout << "Enter elements of the first matrix:" << endl;
    int matrix1[row1][col1];
    for (int i = 0; i < row1; ++i) {
        for (int j = 0; j < col1; ++j) {
            cin >> matrix1[i][j];
        }
    }

    cout << "Enter elements of the second matrix:" << endl;
    int matrix2[row2][col2];
    for (int i = 0; i < row2; ++i) {
        for (int j = 0; j < col2; ++j) {
            cin >> matrix2[i][j];
        }
    }

    int result[row1][col2] = {{0}};

    for (int i = 0; i < row1; ++i) {
        for (int j = 0; j < col2; ++j) {
            for (int k = 0; k < col1; ++k) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    cout << "Result of matrix multiplication:" << endl;
    for (int i = 0; i < row1; ++i) {
        for (int j = 0; j < col2; ++j) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
