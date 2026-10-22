# Password Generator

A command-line password generator built with Python. Users can choose whether to include special characters, set the desired password length, and generate a random password.

## Features

- Generate random passwords
- Choose the password length
- Choose whether to include special characters
- Choose whether to include numbers
- Choose whether to include uppercase letters
- Choose whether to include lowercase letters
- Interactive menu with an exit option
- Handle invalid menu choices

## Technologies Used

- Python
- `random` module
- `string` module
- `while` loops
- Conditional statements
- String operations and list comprehension

## Requirements

- Python 3

## How to Run

1. Save the Python script as `password_generator.py`.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python password_generator.py
   ```

   If your system uses `python3` to launch Python, run `python3 password_generator.py` instead.

## Security Note

This is a beginner learning project. The code uses Python's `random`ands `string` modules, which is not designed for generating cryptographically secure passwords. For real-world sensitive accounts, use a trusted password manager or a cryptographically secure generator.

## Future Improvements

- Use Python's `secrets` module for stronger randomness
- Validate the password length
- Ensure the generated password contains each character type the user selected
- Handle non-numeric length input gracefully

