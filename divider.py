
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


def main():
    values = [10, 20, 30]

    print("Average:", average(values))

    # ai should fix this
    result = divide(100, 0)

    print("Result:", result)


if __name__ == "__main__":
    main()
