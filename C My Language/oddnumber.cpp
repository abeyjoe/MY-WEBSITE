#include <iostream>
#include <string>
using namespace std;

int main()
{
    cout << "Program to print odd numbers between 20 and 1000" << endl;
    cout << "Using while loop" << endl;

    int min = 21;   /* minimum range */
    int max = 1000; /* maximum range */
    while (min <= max)
    {
        cout << min << ", ";
        min += 2;
    }
    return 0;
}
