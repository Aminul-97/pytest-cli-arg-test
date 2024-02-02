import pytest
from src.argparse_cli_calculator import arguments

from typer.testing import CliRunner
from src.typer_cli_calculator import app


# Fixture to get user inputs
@pytest.fixture
def get_user_input(request) -> tuple:
    a = str(request.config.getoption("--a"))
    b = str(request.config.getoption("--b"))
    opt = str(request.config.getoption("--opt"))
    return a, b, opt

# Fixture to calculate expected output
@pytest.fixture
def expected_output(get_user_input):
    a, b, opt = get_user_input
    a = eval(a)
    b = eval(b)

    if opt == "+":
        res = float(a+b)
    elif opt == "-":
        res = float(a-b)
    elif opt == "/":
        res = float(a/b)
    else :
        res = float(a*b)
    return res

# Function to test argparse_cli_calculator()
def test_argparse_cli_calculator(capsys, get_user_input, expected_output):
    a, b, opt = get_user_input
    arguments([a, opt, b])
    output = capsys.readouterr().out.rstrip()
    assert output == f"Result: {expected_output}"


runner = CliRunner()

# Function to test typer_cli_calculator()
def test_typer_cli_calculator(get_user_input, expected_output):
    a, b, opt = get_user_input
    result = runner.invoke(app, [a, opt, b])
    assert result.exit_code == 0
    assert f"Result: {expected_output}\n" in result.stdout


