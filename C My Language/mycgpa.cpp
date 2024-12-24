#include <iostream>
#include <string>
using namespace std;

int main() {
    int numCourses;

    cout << "Enter the number of courses: ";
    cin >> numCourses;

    double totalGradePoints = 0.0;
    int totalCreditHours = 0;

    for (int i = 1; i <= numCourses; ++i) {
        char grade;
        int creditHours;

        cout << "Enter grade for Course " << i << " (A, B, C, D, F): ";
        cin >> grade;

        cout << "Enter course unit for Course " << i << ": ";
        cin >> creditHours;

        double gradePoints;

        // Convert the grade to grade points
        switch (grade) {
            case 'A':
                gradePoints = 4.0;
                break;
            case 'B':
                gradePoints = 3.0;
                break;
            case 'C':
                gradePoints = 2.0;
                break;
            case 'D':
                gradePoints = 1.0;
                break;
            case 'F':
                gradePoints = 0.0;
                break;
            default:
                cout << "Invalid grade entered. Please enter A, B, C, D, or F.\n";
                i--; // To repeat the current iteration
                continue;
        }

        // Calculate grade points earned for the course
        double gradePointsEarned = gradePoints * creditHours;

        // Accumulate total grade points and credit hours
        totalGradePoints += gradePointsEarned;
        totalCreditHours += creditHours;
    }

    // Calculate CGPA
    double cgpa = totalGradePoints / totalCreditHours;

    cout << "CGPA: " << cgpa << endl;

    return 0;
}
