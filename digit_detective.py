
import random

def hilo():
    """
    This function plays a guessing game where the player guesses a random number between 1 and 100.
   
    Returns:
    guesses (int): The number of guesses made to find the correct number.
    guessed_numbers (list): A list containing all the guessed numbers.
    quit_game (bool): True if the user quits the game; False otherwise.
    """
    # Generate a random number between 1 and 100.
    random_number = random.randint(1, 100)
   
    # Initialize variables to keep track of guesses and guessed numbers.
    guesses, guessed_numbers = 0, []
   
    # Main game loop
    while True:
        try:
            # Prompt the user to input a guess or 'quit' to exit.
            guess_input = input("Take a guess between 1-100 (type 'quit' to exit): ")
           
            # Check if the user wants to quit the game.
            if guess_input.lower() == 'quit':
                print("You quit the game. The number was " + str(random_number) + "\nYour guessed numbers:", guessed_numbers)
                return guesses, guessed_numbers, True  # Flag set to True to indicate quitting
               
            # Convert the user's input to an integer (assuming it's a valid number).
            guess = int(guess_input)
        except ValueError:
            # Handle invalid input (non-integer).
            print("Invalid input. Please enter a valid number or 'quit'.")
            continue
       
        # Add the guess to the list of guessed numbers and increment the guess count.
        guessed_numbers.append(guess)
        guesses += 1
       
        # Check if the guess is correct, too low, or too high.
        if guess == random_number:
            print("You guessed it! The number was " + str(random_number) + ". You guessed it in " + str(guesses) + " attempts.\nYour guessed numbers:" + str(guessed_numbers))
            break
        elif guess < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
   
    return guesses, guessed_numbers, False  # Flag set to False when not quitting

def main():
    """
    This is the main function to manage the game and user interaction.
    """
    # Initialize variables to keep track of the total number of guesses and games played.
    total_guesses = 0
    total_games = 0
   
    while True:
        # Play a game and store the number of guesses, guessed numbers, and quit status.
        guesses, guessed_numbers, quit_game = hilo()
       
        # Add the total number of guesses and games played.
        total_guesses += guesses
        total_games += 1
       
        # Check if the user wants to quit the program.
        if quit_game:
            print("Thanks for playing!")
            break
        else:
            response = input("Do you want to play again? (yes/no): ")
            if response.lower() not in ["yes", "y"]:
                print("Thanks for playing!\nYour guessed numbers:", guessed_numbers)
                print("Average guesses per game: {:.2f}".format(total_guesses / total_games))
                break

# Start the game
main()
