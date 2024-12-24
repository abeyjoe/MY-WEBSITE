#include <iostream>
#include <string>
using namespace std;

int main()
{
    cout << "Program to determine my shoe size" << endl;

    string shoesize; // Declearation of variable

    cout << "Enter you shoe size : ";
    cin >> shoesize;

    string msg = "Your shoe size is " + shoesize; // Concatination of string and variable

    cout << msg;

    return 0;
}
