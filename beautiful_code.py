def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


def print_numbers(numbers):
    """
    Print each number in the list.
    """
    for number in numbers:
        print(number)


def main():
    """
    Main function to demonstrate the code.
    """
    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print("Average:", average)
    print_numbers(numbers)


if __name__ == "__main__":
    main()
