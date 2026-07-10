
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def average(numbers):
    try:
        total = sum(numbers)
        return total / len(numbers)
    except ZeroDivisionError:
        return None


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def main():
    values = [10, 20, 30]

    print("Average:", average(values))

    # ai should fix this
    result = divide(100, 0)

    print("Result:", result)

    # demonstrate new functions
    print("Add:", add(2, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(3, 5))


if __name__ == "__main__":
    main()
