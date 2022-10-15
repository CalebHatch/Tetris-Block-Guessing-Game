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

    blocks_array = ("line", "t block", "s block", "L block", "square block")

    while game_loop:
        game_block = numpy.random.choice(blocks_array)
        print(game_block)  # for debug

        print(blocks_array)
        player_guess = input("What is the next block?: ")

        if game_block == player_guess:
            GameEndResults.win_result()
        elif game_block != player_guess:
            GameEndResults.loss_result()

        if player.points <= 0:
            print("Your score reached below zero!")
            GameEndResults.player_end_state()

        print("Your score is: " + str(player.points) + ".")
        user_retry = input("Play again? [y/n]: ")
        user_retry = user_retry.upper()

        if user_retry == "Y":  # Game will loop as long as the user keeps entering "y"
            game_loop = True
            continue
        elif user_retry == "N":
            GameEndResults.player_end_state()
        else:
            print("Invalid input. Please type either \"y\" or \"n\"")


if __name__ == "__main__":
    global game_block, player_guess
    main()
