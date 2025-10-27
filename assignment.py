import random
# Do not remove the parameter from the main function


def main(random_number=None):
    # Do not remove line 4, 5, or 6
    if random_number is None:
        random_number = random.randint(1, 10)

    print("\nWelcome to the Guessing Game")

   
    for i in range(3):
       guess_number = int(input("\nEnter your guess from one to ten: "))
    
       if guess_number == random_number:
         print(f"Hooray! You guessed the number: {guess_number}")
    
       elif guess_number > random_number:
         print(f"Your guess {guess_number} was a little too high. Try lower.")

       else:
         print(f"Your guess {guess_number} was a little too low. Try higher.")
    
    print(f"You failed to guess the number {random_number} in three attempts.")

if __name__ == "__main__":
    main()
