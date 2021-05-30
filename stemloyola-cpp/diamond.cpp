/*
    Name: Alvin Chris Mrema
    Year: 2021
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    cout << "Enter the size for your Diamond: ";

    int SIZE;
    cin >> SIZE;

    // Display the top triangle
    for (int row = 0; row < SIZE; row++) {
        cout << endl; // Start a new line

        // Add space before the asterisks
        for (int col = SIZE-row-1; col > 0; col--) cout << " ";

        // Display the asterisks
        for (int col = 0; col < 2*row+1; col++) cout << "*";
    }

    // Display the bottom triangle
    for (int row = 0; row < SIZE-1; row++) {
        cout << endl; // Start a new line

        // Reduce space before the asterisks
        for (int col = 0; col < row+1; col++) cout << " ";

        // Display the asterisks
        for (int col = 2*(SIZE-row)-3; col > 0; col--) cout << "*";
    }

    return 0;
}
