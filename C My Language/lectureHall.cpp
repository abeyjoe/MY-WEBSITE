#include<iostream>
#include<string>
using namespace std;

int main()
{
    float length;
    float bredth;

    cout << "Program to calculate area of Computer Science HND1 lecture room"<<endl;
    cout << " "<<endl;

    cout << "Enter length of lecture hall in metres : ";
    cin >> length;
    cout << "Enter bredth of lecture hall in metres : ";
    cin >> bredth;

    float area = length * bredth; // Formular to calculate area of a Lecture Hall

    cout << " " << endl;
    cout << "The area of lecture hall is ";
    cout << area;
    cout << "m";

    return 0;
}
