
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def multiply(a, b):
    # Only allow numeric multiplication; guard against cases like 'a' * 3 -> 'aaa'
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return None
    try:
        return a * b
    except TypeError:
        return None


def subtract(a, b):
    try:
        return a - b
    except TypeError:
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


if __name__ == "__main__":
    main()
