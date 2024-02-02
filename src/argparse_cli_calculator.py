from argparse import ArgumentParser

def arguments(arg_list: list[str] | None):
    """
    Function to get user inputs
    """
    parser = ArgumentParser()

    parser.add_argument("a", help="First value.")
    parser.add_argument("opt", help="Operation")
    parser.add_argument("b", help="Second value.")
    args = parser.parse_args(arg_list)

    return user_input(eval(args.a), args.opt, eval(args.b))

def user_input(a:float, opt: str, b:float) -> float:
    """
    Function to verify user inputs
    """
    if opt == "+":
        res = plus(a ,b)
    elif opt == "-":
        res = minus(a ,b)
    elif opt == "/":
        res = divide(a ,b)
    else :
        res = multiply(a ,b)

    print(f"Result: {res}")
    return res

def plus(a:float , b:float) -> float:
    """
    Function to add two numbers
    """
    return a + b

def minus(a:float , b:float) -> float:
    """
    Function to subtract two numbers
    """
    return a-b

def divide(a:float , b:float) -> float:
    """
    Function to divide two numbers
    """
    return a/b

def multiply(a:float , b:float) -> float:
    """
    Function to multiply two numbers
    """
    return a*b

if __name__ == "__main__":
    arguments()
