
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


# Reuse the existing multiply and subtract implementations above which
# include some type-safety and error handling. Provide simple aliases
# for the same operations requested by the feature branch.
def multiplier(a, b):
    """Alias for multiplication (keeps behavior consistent)."""
    return multiply(a, b)


def substracter(a, b):
    """Alias for subtraction (keeps behavior consistent)."""
    return subtract(a, b)


def main():
    values = [10, 20, 30]

    print("Average:", average(values))

    # ai should fix this
    result = divide(100, 0)

    print("Result:", result)


if __name__ == "__main__":
    main()
