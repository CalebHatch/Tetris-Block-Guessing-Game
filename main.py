"""
Tetris Block Guesser
by: Caleb Hatch
"""
import numpy


# Keeps track of the amount of the player's points.
class Player:
    def __init__(self, points):
        self.points = points


player = Player(300)

game_loop = True


def game_intro():
    print("Welcome to Tetris Block Guesser!")
    tutorial_response = input("Would you like a brief tutorial on how the game works? [y/n] ")
    tutorial_response = tutorial_response.upper()

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


def print_blocks():
    print("""          
                []    [][]   
    [][][][], [][][],   [][]
    """)


# Contains conditions for all three game endings
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


def main():
    global player, game_loop, game_block, player_guess
    game_intro()

    print_blocks()
    blocks_array = ("line", "t block", "s block")

    while game_loop:
        game_block = numpy.random.choice(blocks_array)

        print(blocks_array)
        player_guess = input("What is the next block?: ")

        if game_block == player_guess:
            GameEndResults.win_result()
        elif game_block != player_guess:
            GameEndResults.loss_result()

        if player_guess == "intro":
            game_intro()

        if player.points <= 0:
            print("Your score reached below zero!")
            GameEndResults.player_end_state()

        print("Your score is: " + str(player.points) + ".")
        user_retry = input("Play again? [y/n]: ")
        user_retry = user_retry.upper()

        # make this loop if invalid
        if user_retry == "Y":  # Game will loop as long as the user keeps entering "y"
            game_loop = True
            continue
        elif user_retry == "N":
            GameEndResults.player_end_state()
        elif user_retry == "INTRO":
            game_intro()
        else:
            print("Invalid input. Please type either \"y\" or \"n\"")


if __name__ == "__main__":
    global game_block, player_guess
    main()
