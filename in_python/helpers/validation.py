import sys


def validate_input(args: str, error_message: str, expected_length: int = 2, should_exit=True) -> None:
    if len(args) != expected_length:
        print(error_message)
        if should_exit:
            sys.exit(1)


def validate_file_input(args: str, expected_length: int = 2, should_exit=True) -> None:
    message = "Missing required parameted: input file."
    validate_input(args, message, expected_length, should_exit)


def handle_file_not_found(file_path, should_exit=True):
    print(f"Couldn't find specified file: {file_path}")
    if should_exit:
        sys.exit(1)
