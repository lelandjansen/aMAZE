# aMAZE
[![Analytics](https://ga-beacon.appspot.com/UA-46915227-3/aMAZE)](https://github.com/igrigorik/ga-beacon)

### Overview
aMAZE is a Python-based maze game designed by
[Leland Jansen](https://github.com/lelandjansen) and
[Michael Steer](https://github.com/michaelsteer). The objective of the game is
to navigate out of a maze while competing against a computer opponent. The game
has varying degrees of difficulty such as the maze size and "intelligence" of
the computer.

![Randomly generated maze and "smart" AI path](/demo/6040ai.png)


### AI Performance
An overview and demonstration of the AI's performance can be found at
[www.lelandjansen.com/project/amaze](http://www.lelandjansen.com/project/amaze)


### Controls
Key | Action
--- | ---
↑ | Move Up
↓ | Move Down
← | Move Left
→ | Move Right
0-9, Q | Menu navigation


### Score
One's score is calculated based on the AI difficulty, maze size, progress
through the maze, and number of mazes solved. A leaderboard containing this
information is available to track progress.


### Installation instructions
This game depends on the following resources:
- Python 3.4
- PyGame and its dependencies

To install pyGame and all of its dependencies, please run the following command.
Copy and paste the string below to install all necessary libraries
for this project. This assumes Python3 is already installed.


##### Linux
```bash
cd ~ && sudo apt-get install mercurial && hg clone \
https://bitbucket.org/pygame/pygame && cd pygame && sudo apt-get install \
python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev \
libjpeg-dev libfreetype6-dev && python3 setup.py build && sudo python3 \
setup.py install
```

##### Windows
- Installing Python: Go to [the python page](https://python.org/downloads) and
download version 3.5. This installation assumes you are using the 64 bit version
- Installing pyGame: Download the
[pyGame installer](http://www.lfd.uci.edu/~gohlke/pythonlibs/th4jbnf9/pygame-1.9.2a0-cp35-none-win_amd64.whl)
navigate to the download directory and run the following commands in a command prompt
```bash
python -m ensurepip
python -m ensurepip --upgrade
python -m pip install wheel
python -m pip install wheel --upgrade
python -m pip install pygame-1.9.2a0-cp35-none-win_amd64.whl
```

### Contributions
##### [Leland Jansen](https://github.com/lelandjansen)
- Maze generation
   - Modified depth-first search to create "perfect" maze
- AI Algorithm
   - Variable-difficulty using modified depth-first search and A\* search
   - Computation of A\* bias point
   - Shortest path using breadth-first search

##### [Michael Steer](https://github.com/michaelsteer)
- Rendering and exporting the maze
- Menu system and state machine (Terminal)
- Pygame implementation and the Game State
- Path following sprites
- Scoring system and leaderboards
- Installation instructions
