# aMAZE
Overview:
  aMAZE is a game designed by Leland Jansen and Michael Steer. The
  objective of the game is to navigate your way out of a maze before
  an AI does. The game has varying degrees of difficulty, from the
  size of the maze, to the speed of the AI, to the intellegence of
  the AI.

Controls:
  W - Move Up
  A - Move Left
  S - Move Down
  D - Move Right
  0-9, Q - Keys used to navigate the menus

Score:
  A score is calculated based on the difficulty of the maze and AI,
  along with how far into the current maze you are and how many mazes
  you have successfully navigated. A leaderboard containing this
  information is available to track progress

Installation instructions:
  This game depends that the following resources are present.
  - Python 3.4
  - PyGame
  - Cairo

  To install python 3.4 on both Unix or windows, please refer to the instructions
  on https://www.python.org

  To install pyGame and all of its dependencies, please run the following set of
  commands. Copy and paste the below string to install all necessary libraries
  for this project. This assumes python3 is already installed

  cd ~ && sudo apt-get install mercurial && hg clone https://bitbucket.org/pygame/pygame \
  && cd pygame && sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev \
  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev && python3 setup.py build \
  && sudo python3 setup.py install

  Cairo/PyCairo should already be installed on Unix Operating systems if python
  is present. If using Windows, please do the following to install CairoCFFI <WRITE_ME_LATER>
