/*
    Name: Alvin Chris Mrema
    Year: 2021
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    cout << "Enter your Symbols e.g '{[()<>]}': ";

    string EXPRESSION;
    cin >> EXPRESSION;

    stack<char> symbols;
    bool isBalanced = true;

    // Process the expression from left to right
    for (auto ch : EXPRESSION) {
        // Push an opening symbol onto the stack
        if (ch == '{' || ch == '[' || ch == '(' || ch == '<') symbols.push(ch);

        // Process a closing symbol
        else if ((ch == '}' || ch == ']' || ch == ')' || ch == '>') && symbols.empty() != true) {
            // Check if the closing symbol matches what is on top of the stack
            if ((ch == '}' && symbols.top() == '{') ||
                (ch == ']' && symbols.top() == '[') ||
                (ch == ')' && symbols.top() == '(') ||
                (ch == '>' && symbols.top() == '<')) {
                // Remove the top opening symbol since they match
                symbols.pop();
            } else {
                // Mismatching symbols found
                isBalanced = false;
                break; // No need to continue since a mismatch is already found
            }
        }

        // Unknown symbol found
        else {
            cout << "Unknown symbol '" << ch << "' in the expression!" << endl;
            isBalanced = false;
            break;
        }
    }

    // A balanced stack leaves an empty stack at the end of the day
    if (symbols.size() > 0) isBalanced = false;

    // Display results
    if (isBalanced) cout << "\"" << EXPRESSION << "\" is balanced!" << endl;
    else cout << "\"" << EXPRESSION << "\" is NOT balanced!" << endl;

    return 0;
}
