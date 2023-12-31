
#include <iostream>

using namespace std;

int main()
{
    string phrase = "Mayur Patil";
    cout << "World\n";
    cout << phrase << endl;
    
    cout << phrase[0] << endl;
    phrase[0] = 'B';
    cout << phrase << endl;
    
    cout << phrase.length() << endl;
    cout << "Patil starts at index: " << phrase.find("Patil", 0) << endl;
    cout << phrase.substr(4, 5) << endl;
    

    return 0;
}


// To run
// ./workingWithStrings.exe