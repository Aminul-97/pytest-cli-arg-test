from typer.testing import CliRunner
from src.typer_cli_calculator import app
import pytest
import shlex

runner = CliRunner()

# List of test cases
test_cases = [
    ("10.0 / 5.0", "Result: 2.0\n"),
    ("10.0 * 5.0", "Result: 50.0\n"),
    ("10.0 - 5.0", "Result: 5.0\n"),
    ("10.0 + 5.0", "Result: 15.0\n"),
]


# Function to test typer_cli_calculator()
@pytest.mark.parametrize("command, expected_output", test_cases)
def test_typer_cli_calculator(command, expected_output):
    result = runner.invoke(app, shlex.split(command))
    assert result.exit_code == 0
    assert expected_output in result.stdout
