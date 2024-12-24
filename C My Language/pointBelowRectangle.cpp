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
    // Get user input for rectangle coordinates
    Rectangle rectangle;
    std::cout << "Enter rectangle coordinates (left right top bottom): ";
    std::cin >> rectangle.left >> rectangle.right >> rectangle.top >> rectangle.bottom;

    // Get user input for point coordinates
    Point point;
    std::cout << "Enter point coordinates (x y): ";
    std::cin >> point.x >> point.y;

    // Check if the point is below the rectangle
    if (isPointBelowRectangle(point, rectangle)) {
        std::cout << "The point is below the rectangle.\n";
    } else {
        std::cout << "The point is not below the rectangle.\n";
    }
    return 0;
}
