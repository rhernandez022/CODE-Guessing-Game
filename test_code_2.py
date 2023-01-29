import pytest
import random
import os,sys
from mock_input_tests import *

from code_2 import main

def check_if_file_exists():
    try:
        exists = os.path.exists("code_2.py")
        assert exists == True
    except:
        sys.exit()

def test_lower_number():
    random_number = random.randint(1,7)
    guess = random_number+2

    set_keyboard_input([guess,guess-1,guess-2])
    main(random_number)
    output = get_display_output()

    assert output == [
        "\nWelcome to the Guessing Game",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({guess}) was a little too high. Try lower.",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({guess-1}) was a little too high. Try lower.",
        "\nEnter your guess from one to ten: ",
        f"Hooray! You guessed the number: {guess-2}"
    ]

def test_higher_number():
    random_number = random.randint(3,10)
    guess = random_number-2

    set_keyboard_input([guess,guess+1,guess+2])
    main(random_number)
    output = get_display_output()

    assert output == [
        "\nWelcome to the Guessing Game",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({guess}) was a little too low. Try higher.",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({guess+1}) was a little too low. Try higher.",
        "\nEnter your guess from one to ten: ",
        f"Hooray! You guessed the number: {guess+2}"
    ]

def test_attempts():
    random_number = random.randint(2,9)

    set_keyboard_input([random_number-1,random_number+1,random_number+1])
    main(random_number)
    output = get_display_output()
    assert output == [
        "\nWelcome to the Guessing Game",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({random_number-1}) was a little too low. Try higher.",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({random_number+1}) was a little too high. Try lower.",
        "\nEnter your guess from one to ten: ",
        f"Your guess ({random_number+1}) was a little too high. Try lower.",
        f"Your failed to guess the number ({random_number}) in three attempts."

    ]    