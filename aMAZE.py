# aMAZE.py
# By: Michael Steer
# The entry point for the program. Contains all the menu code

# Imports
import os
import time
import getch
from generateMaze import Maze
import gamestate
from leaderboard import Leaderboard

# Enumeration for menu states
MENU_MAIN = '0'
MENU_NEW_GAME_MAPSIZE = '1'
MENU_NEW_GAME_AIDIFF = '4'
MENU_NEW_GAME_AISPEED = '5'
MENU_LEADERBOARDS = '2'
MENU_ABOUT = '3'
MENU_QUIT = 'q'
MENU_START_GAME = '6'
MENU_EXECUTE_GAME = '7'
MENU_GAME_OVER = '8'
MAP_SMALL = 8               # Small map. 8x8 tiles (64 total)
MAP_MEDIUM = 16             # Medium map. 16x16 tiles (256 total)
MAP_LARGE = 32              # Large map. 32 x 32 tiles ()

AI_SLOW = 2                 # Slow AI speed. Two tiles per second
AI_FAST = 4                 # Fast AI Speed. Four tiles per second, same as
                            # the player

# Globals
mapSize = None              # The size of the map to be generated
aiDifficulty = None         # The Intellegence flag of the AI
aiSpeed = None              # The speed of the ai

# Pointer to function that pulls a single character from
# the console (see getch.py)
get_ch = getch._Getch()

# Game over menu
def game_over(score):
    os.system("clear")

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("=       GAME OVER :(      =")
    print("===========================")
    print("= Enter your Name         =")
    print("=       10 Characters max =")
    print("===========================")

    # Get the users name
    name = input()

    # Update the leaderboard with the user that just played
    leaderboard = Leaderboard()
    leaderboard.readLeaderboard()
    leaderboard.addUser(name, score)
    leaderboard.writeLeaderboard()

# Starts Pygame and all that fun stuff
def start_game():
    os.system("clear")
    return MENU_EXECUTE_GAME

# Menu for selecting the ai Speed
def newGame_aiSpeed():

    global aiSpeed

    os.system("clear")

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("=    Pick an AI Speed     =")
    print("===========================")
    print()
    print()
    print("1) Slow. 2 Nodes / Second ( slower then you)")
    print("2) Fast. 4 Nodes / Second (   same as you  )")
    print("3) Back")

    next_Menu = None

    # Get the next menu from the user
    while next_Menu == None:
        next_Menu = get_ch().lower()

        if next_Menu == '1':
            aiSpeed = AI_SLOW
            os.system("clear")
            return MENU_START_GAME
        elif next_Menu == '2':
            aiSpeed = AI_FAST
            os.system("clear")
            return MENU_START_GAME
        elif next_Menu == '3':
            os.system("clear")
            return MENU_NEW_GAME_AIDIFF
        else:
            next_Menu = None

# Menu for selecting the ai Difficulty
def newGame_aiDifficulty():

    global aiDifficulty

    os.system("clear")

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("=  Pick an AI Difficulty  =")
    print("===========================")
    print()
    print()
    print("1) 0/100    Very Easy ")
    print("2) 20/100   Easy")
    print("3) 40/100   Medium")
    print("4) 60/100   Hard")
    print("5) 80/100   Very Hard")
    print("6) 100/100  Advanced")
    print("7) 101/100  Expert")
    print("8) ???/100  Random")
    print("9) !!!/100  Chuck Norris")
    print("0)          Back")

    next_Menu = None

    # Get the next menu from the user
    while next_Menu == None:
        next_Menu = get_ch().lower()

        if next_Menu == '1':
            aiDifficulty = 0
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '2':
            aiDifficulty = 20
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '3':
            aiDifficulty = 40
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '4':
            aiDifficulty = 60
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '5':
            aiDifficulty = 80
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '6':
            aiDifficulty = 100
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '7':
            aiDifficulty = 101
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '8':
            aiDifficulty = -1
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '9':
            aiDifficulty = -2
            os.system("clear")
            return MENU_NEW_GAME_AISPEED
        elif next_Menu == '0':
            os.system("clear")
            return MENU_NEW_GAME_MAPSIZE
        else:
            next_Menu = None

# Menu for selecting the map size
def newGame_MapSize():

    global mapSize

    os.system("clear")

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("=   Pick a map size       =")
    print("===========================")
    print()
    print()
    print("1) Small.  8x8 Tiles")
    print("2) Medium. 16x16 Tiles")
    print("3) Large.  32x32 Tiles")
    print("4) Back")

    next_Menu = None

    # Get the next menu from the user
    while next_Menu == None:
        next_Menu = get_ch().lower()

        if next_Menu == '1':
            mapSize = MAP_SMALL
            os.system("clear")
            return MENU_NEW_GAME_AIDIFF
        elif next_Menu == '2':
            mapSize = MAP_MEDIUM
            os.system("clear")
            return MENU_NEW_GAME_AIDIFF
        elif next_Menu == '3':
            mapSize = MAP_LARGE
            os.system("clear")
            return MENU_NEW_GAME_AIDIFF
        elif next_Menu == '4':
            os.system("clear")
            return MENU_MAIN
        else:
            next_Menu = None

# Menu for displaying the leaderboards
def leaderboards():

    os.system("clear")

    # Load the leaderboard
    users = Leaderboard()
    users.readLeaderboard()

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("=      Leaderboards       =")
    print("===========================")
    print()
    print()
    print("|# |   Name    |  Score   |")
    print("===========================")

    # Print the leaderboard
    print(users)

    print("1) Back ")

    next_Menu = None

    # Get the next menu from the user
    while next_Menu == None:
        next_Menu = get_ch().lower()

        if next_Menu == '1':
            os.system("clear")
            return MENU_MAIN
        else:
            next_Menu = None

# Menu for displaying information about the game
def about():

    os.system("clear")

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("= A game By Leland Jansen =")
    print("=     and Michael Steer   =")
    print("===========================")
    print("=          About          =")
    print("===========================")
    print()
    print()
    print("Overview: ")
    print("  aMAZE is a game designed by Leland Jansen and Michael Steer. The")
    print("  objective of the game is to navigate your way out of a maze before")
    print("  an AI does. The game has varying degrees of difficulty, from the")
    print("  size of the maze, to the speed of the AI, to the intellegence of ")
    print("  the AI.")
    print("Controls:")
    print("  W - Move Up  ")
    print("  A - Move Left")
    print("  S - Move Down")
    print("  D - Move Right")
    print("  0-9, Q - Keys used to navigate the menus")
    print("Score:")
    print("  A score is calculated based on the difficulty of the maze and AI,")
    print("  along with how far into the current maze you are and how many mazes")
    print("  you have successfully navigated. A leaderboard containing this ")
    print("  information is available to track progress")
    print()
    print()
    print("1) Back")

    next_Menu = None

    # Get the next menu
    while next_Menu == None:
        next_Menu = get_ch().lower()

        if next_Menu == '1':
            os.system("clear")
            return MENU_MAIN
        else:
            next_Menu = None

# The main menu
def main_Menu():

    next_Menu = None

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("=        Main Menu        =")
    print("===========================")
    print()
    print()
    print("1) New Game")
    print("2) Leaderboards")
    print("3) About")
    print("Q) Quit")

    # Get the next menu
    while next_Menu == None:
        next_Menu = get_ch().lower()
        if next_Menu in ['1','2','3','q']:
            return next_Menu
        else:
            next_Menu = None

# Main Function (Entry Point)
if __name__ == "__main__":

    global get_ch
    get_ch = getch._Getch()
    next_Menu = None
    os.system("clear")

    next_Menu = main_Menu()

    # Continue looping through menus and gamestates forever, or until the user
    # chooses to quit
    while True:
        if next_Menu == MENU_MAIN:
            next_Menu = main_Menu()
        elif next_Menu == MENU_NEW_GAME_MAPSIZE:
            next_Menu = newGame_MapSize()
        elif next_Menu == MENU_NEW_GAME_AIDIFF:
            next_Menu = newGame_aiDifficulty()
        elif next_Menu == MENU_NEW_GAME_AISPEED:
            next_Menu = newGame_aiSpeed()
        elif next_Menu == MENU_LEADERBOARDS:
            next_Menu = leaderboards()
        elif next_Menu == MENU_ABOUT:
            next_Menu = about()
        elif next_Menu == MENU_START_GAME:
            next_Menu = start_game()
        elif next_Menu == MENU_EXECUTE_GAME:
            next_Menu = gamestate.game_state(mapSize, aiSpeed, aiDifficulty)
        elif next_Menu == MENU_QUIT:
            os.system("clear")
            break
    #os.system("clear")

# That's all folks!