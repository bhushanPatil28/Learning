#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int a = 10;
    float b = 20.32324234;
    double e = 20.32324234;
    char c = 'A';
    bool d = true ;  // 1 or 0 (for true false)
    
    // print
    cout << a <<endl;
    cout << fixed << setprecision(8) << b <<endl;
    cout << c <<endl;
    cout << d <<endl;
    cout << fixed << setprecision(8) << e <<endl;

    return 0;
}