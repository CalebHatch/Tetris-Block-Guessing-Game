"""
Tetris Block Guesser
by: Caleb Hatch
"""
import numpy
from termcolor import colored


# Class to keep track of player points
class Player:
    def __init__(self, points):
        self.points = points


player = Player(300)  # Player score initializer

game_loop = True  # Allows the while loop for the game to run


# Function to play the game's intro. Can be repeated at any time.
def game_intro():
    print("Welcome to Tetris Block Guesser!")
    tutorial_response = input("Would you like a brief tutorial on how the game works? [y/n] ")
    tutorial_response = tutorial_response.upper()  # Player can type "y" or "n" in either upper or lower case

    if tutorial_response == "Y":
        print("This game is a representation of the preview window for the next block that comes up in the game "
              "\"Tetris\". A board of Tetris blocks will be shown to you, along with the corresponding names. You must "
              "guess which of the four blocks will come next!\n")
        print("The blocks and their names will be shown below: \n")
        print("""
        [][][][]
        This is the \"line block\"\n
        """)
        print("""
          []
        [][][]
        This is the \"t block\"\n
        """)
        print("""
        [][]
          [][]
        This is the \"s block\"\n
        """)
        print("To see the intro again, simply type \"intro\" at any time.\n")
    else:
        print("To see the intro, simply type \"intro\" at any time.\n")


# Prints the blocks that the player can choose from.
def print_blocks():
    print("""          
                []    [][]   
    [][][][], [][][],   [][]
    """)


# Class to handle the conditions for ending the game for the player.
class GameEndResults:
    global game_block, player_guess

    # For when the player guesses correctly. Adds 100 to score
    @staticmethod
    def win_result():
        print("Next block was " + str(game_block) + ", and you guessed \"" + str(
            player_guess) + "\". You got it!\n")
        player.points = (player.points + 100)

    # For when the player guesses incorrectly. Takes 25 from sore
    @staticmethod
    def loss_result():
        print("Next block was " + str(game_block) + ", and you guessed \"" + str(player_guess) +
              "\". Better luck next time!\n")
        player.points = (player.points - 25)

    # For whenever the game should be ended. Outputs a "game over" message to the user and uses the "quit()"
    # command to end the program.
    @staticmethod
    def player_end_state():
        global game_loop
        print("Game over!\nGoodbye.")
        quit()


# Drives the program. Handles the whole game loop
def main():
    global player, game_loop, game_block, player_guess
    debug_mode = False  # debug mode turned off by default

    game_intro()  # Plays the game's intro for the first time

    # Sets up debug mode for the player, if wanted
    user_debug = input("Would you like to activate debug mode? [y/n]: ")
    user_debug = user_debug.upper()

    # Conditional to make debug boolean true or false
    if user_debug == "Y":
        debug_mode = True
    elif user_debug == "N":
        debug_mode = False

    print_blocks()
    blocks_array = ("line", "t block", "s block")  # Player types these to guess the next block

    while game_loop:
        game_block = numpy.random.choice(blocks_array)  # Chooses random block from array

        print(blocks_array)

        # Adds debug message that tells player what the answer is.
        if debug_mode:
            print(colored("[DEBUG MESSAGE]", "red"))
            print("The answer is: " + game_block)

        player_guess = input("What is the next block?: ")

        # Conditional for if the player's guess is right or wrong
        if game_block == player_guess:
            GameEndResults.win_result()
        elif game_block != player_guess:
            GameEndResults.loss_result()

        # Allows the game's intro to be replayed
        if player_guess == "intro":
            game_intro()

        # Lose condition. Game ends if the player's score reaches zero
        if player.points <= 0:
            print("Your score reached zero!")
            GameEndResults.player_end_state()

        if player.points >= 500:
            print("Your score reached " + str(player.points) + ". You win!")
            GameEndResults.player_end_state()

        # Prints the player's score and asks if they would like to play again
        print("Your score is: " + str(player.points) + ".")
        user_retry = input("Play again? [y/n]: ")
        user_retry = user_retry.upper()  # Allows the user to type "y" or "n" in caps or lower

        # make this loop if invalid
        if user_retry == "Y":  # Game will loop as long as the user keeps entering "y"
            game_loop = True
            continue
        elif user_retry == "N":  # Game ends if player selects "N"
            GameEndResults.player_end_state()
        elif user_retry == "INTRO":  # Allows the intro to be replayed
            game_intro()
        else:
            print("Invalid input. Please type either \"y\" or \"n\"")


# Main to start the program
if __name__ == "__main__":
    global game_block, player_guess
    main()
