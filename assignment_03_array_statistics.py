# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    """Return the sum of the list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of the list of numbers."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_max(numbers):
    """Return the maximum value in the list of numbers."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calculate_min(numbers):
    """Return the minimum value in the list of numbers."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


if __name__ == "__main__":
    try:
        n = int(input("How many numbers? "))
        if n <= 0:
            print("Error: You must enter a positive number of values.")
        else:
            numbers = []
            for i in range(1, n + 1):
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)

            print("\nResults:")
            print(f"Sum:     {calculate_sum(numbers)}")
            print(f"Average: {calculate_average(numbers)}")
            print(f"Maximum: {calculate_max(numbers)}")
            print(f"Minimum: {calculate_min(numbers)}")
    except ValueError:
        print("Error: Please enter valid numeric values.")

