# getch.py
# Gets a single character from the command line without the need for the
# User hitting enter
# Source: http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:

            self.impl = _GetchWindows()
        except ImportError:

            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt

        # Strip all of the stuff that surrounds the byte class
        a = msvcrt.getch()
        a = str(a)
        a = a[2:]
        a = a[:-1]

        return a
