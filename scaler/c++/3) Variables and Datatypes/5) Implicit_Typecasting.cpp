#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout << (5/3) << endl;   //(int/int = int)   
    
    // typecasting --> change of resulting datatype
    // Implicit Typecasting
    cout << (5/3.0) << endl;  // (int/float = float)

    // priority = float, int, char, bool
    
    // char + int = int 
    char letter = 'A'; // ASCII 65
    cout << letter + 1 << endl;
    letter = letter + 1; 
    cout << letter << endl;
    
    char ch = 78;
    cout << ch << endl;
    
    // boolean + int = int
    cout << (true + 7) << endl;
    return 0;
}