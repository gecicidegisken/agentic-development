
def divide(a, b):
    return a / b


def average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def main():
    values = [10, 20, 30]

    print("Average:", average(values))

    # ai should fix this
    result = divide(100, 0)

    print("Result:", result)


if __name__ == "__main__":
    main()
