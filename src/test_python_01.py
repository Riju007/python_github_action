def simple_decorator(input_function):
    def inner(*args, **kwargs):
        print("Decorating the function start-------")
        result = input_function(*args, **kwargs)
        print("Decorating function end----")
        return result

    return inner


@simple_decorator
def add_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total


if __name__ == "__main__":
    result = add_numbers(1, 2, 3)
    print(f"Total sum is: {result}")
