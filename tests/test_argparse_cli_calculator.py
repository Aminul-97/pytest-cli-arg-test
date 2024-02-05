from src.argparse_cli_calculator import arguments
import pytest
import shlex

# List of test cases
test_cases = [
    ("10.0 / 5.0", "Result: 2.0"),
    ("10.0 * 5.0", "Result: 50.0"),
    ("10.0 - 5.0", "Result: 5.0"),
    ("10.0 + 5.0", "Result: 15.0"),
]


# Function to test argparse_cli_calculator()
@pytest.mark.parametrize("command, expected_output", test_cases)
def test_argparse_cli_calculator(capsys, command, expected_output):
    response = arguments(shlex.split(command))
    print(response)
    # output = capsys.readouterr().out.rstrip()
    # assert output == expected_output
