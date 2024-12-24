def main():
    # Define a list of numbers
    numbers = [5, 2, 8, 1, 6, 3, 9, 4]

    # Print the original list
    print("Original List:", numbers)

    # Find the length of the list
    print("Length of the list:", len(numbers))

    # Find the maximum and minimum elements in the list
    print("Maximum element:", max(numbers))
    print("Minimum element:", min(numbers))

    # Sum of all elements in the list
    print("Sum of elements:", sum(numbers))

    # Sorting the list in ascending order
    sorted_numbers = sorted(numbers)
    print("Sorted List (Ascending):", sorted_numbers)

    # Reversing the list
    reversed_numbers = list(reversed(numbers))
    print("Reversed List:", reversed_numbers)

    # Removing an element from the list
    numbers.remove(6)
    print("After Removing 6:", numbers)

    # Adding an element at a specific position
    numbers.insert(2, 10)
    print("After Adding 10 at index 2:", numbers)

    # Counting occurrences of an element
    count = numbers.count(5)
    print("Count of 5 in the list:", count

    # Clearing the entire list
    numbers.clear()
    print("After Clearing the List:", numbers)


if __name__ == "__main__":
    main()
