# CLI options
def pytest_addoption(parser):
    parser.addoption(
        "--a", action="store", default="10", help="Variable A"
    )
    parser.addoption(
        "--opt", action="store", default="+", help="Operation"
    )
    parser.addoption(
        "--b", action="store", default="5", help="Variable B"
    )
