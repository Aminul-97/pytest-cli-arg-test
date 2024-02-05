from argparse import ArgumentParser


def arguments(arg_list: list[str] | None = None):
    """
    Function to get user inputs
    """
    parser = ArgumentParser()

    parser.add_argument("-a", "--a", type=float, help="First value.")
    parser.add_argument("-opt", "--opt", type=str, help="Operation")
    parser.add_argument("-b", "--b", type=float, help="Second value.")

    # Get the value of the args
    args = parser.parse_args(args=arg_list)

    return user_input(a=args.a, opt=args.opt, b=args.b)


def user_input(a: float, opt: str, b: float) -> float:
    """
    Function to verify user inputs
    """
    if opt == "+":
        res = plus(a, b)
    elif opt == "-":
        res = minus(a, b)
    elif opt == "/":
        res = divide(a, b)
    else:
        res = multiply(a, b)

    print(f"Result: {res}")
    return res


def plus(a: float, b: float) -> float:
    """
    Function to add two numbers
    """
    return a + b


def minus(a: float, b: float) -> float:
    """
    Function to subtract two numbers
    """
    return a - b


def divide(a: float, b: float) -> float:
    """
    Function to divide two numbers
    """
    return a / b


def multiply(a: float, b: float) -> float:
    """
    Function to multiply two numbers
    """
    return a * b


if __name__ == "__main__":
    arguments()
