import typer

app = typer.Typer()


@app.command()
def main(a: float, opt: str, b: float) -> float:
    """
    Function to get and verify user inputs
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
    typer.run(main)
