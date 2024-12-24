#include <iostream>

struct Point {
    double x, y;
};

struct Rectangle {
    double left, right, top, bottom;
};

bool isPointBelowRectangle(const Point& point, const Rectangle& rectangle) {
    return point.y < rectangle.bottom;
}

int main() {
    // Example: Define a rectangle and a point
    Rectangle rectangle = {0.0, 5.0, 4.0, 1.0};
    Point point = {2.5, 0.5};

    // Check if the point is below the rectangle
    if (isPointBelowRectangle(point, rectangle)) {
        std::cout << "The point is below the rectangle.\n";
    } else {
        std::cout << "The point is not below the rectangle.\n";
    }

    return 0;
}
