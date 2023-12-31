#include <iostream>

using namespace std;

int main(){
    // Create variables
    int num1, num2, num3;

    // Get inputs
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;
    cout << "Enter third number: ";
    cin >> num3;

    // print sum
    cout << "Sum of " << num1 <<", "<< num2 << ", "<< "and " << num3 << " is " << num1+num2+num3 << endl;
    return 0;
}