from pyfiglet import Figlet  # Importing the Figlet class from the pyfiglet module
import argparse  # Importing argparse for handling command-line arguments
import sys  # Importing sys for handling system-level operations (e.g., exiting the program)

try:
    # Set up the argument parser to handle input arguments from the command line
    parser = argparse.ArgumentParser()

    # Add the "--font" and "--f" argument for the font choice
    parser.add_argument("--font", "--f")

    # Parse the argument and get the font choice
    font_choice = parser.parse_args().font

    # Initialize Figlet with the selected font
    f = Figlet(font=font_choice)

    # Prompt the user to enter the text for ASCII art generation
    text = input("Input: ")

    # Generate and print the ASCII art using the specified font
    print(f"Output: {f.renderText(text)}")

except:
    # If any error occurs, exit the program
    sys.exit()
