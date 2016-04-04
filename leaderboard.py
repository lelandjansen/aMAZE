# Leaderboard.py
# By: Michael Steer

# Conains a simple leaderboard class for keeping track of the top ten
# Players

# Leaderboard class
class Leaderboard:

    # Initialization
    def __init__(self):
        self.users = list()

    # Reads a text file containing names and scores into a list of tuples
    def readLeaderboard(self):

        # Reset the list of users back to none, if there was already information
        # present
        self.users = list()

        # Go through each line of the scores file and conver the information
        # into a tuple
        with open("scores.txt") as f:
            for line in f:
                line = line.split()
                line = (line[0], line[1])
                self.users.append(line)

    # Write a list of tuples to a text file as a space seperated string
    def writeLeaderboard(self):
        with open("scores.txt", "w") as f:
            for user in self.users:
                line = str(user[0]) + " " + str(user[1]) + "\n"
                f.write(line)

    # Add a user to the top ten users, if the users score is high enough
    def addUser(self, name, score):

        inserted = False

        # If there is no name for some reason add a placeholder
        if name == '':
            name = "#NAME"

        # Get the number of users to add
        length = len(self.users)

        # If there are no users, just add the user to the list
        if length == 0:
            self.users.append((name, str(score)))

        # Otherwise determine if the user goes in the list
        else:
            # Iterate through the users
            for i in range(length):
                userScore = int(float(self.users[i][1]))

                # If the current user is now larger than the user in the list
                if userScore < score:
                    inserted = True

                    # Insert the user into the list
                    newUser = (name, str(score))
                    self.users.insert(i, newUser)
                    break

            # If the user did not need to be inserted somewhere, append them to
            # the end
            if not inserted:
                self.users.append((name,str(score)))

            # If the list is now too large, pop the last user from the list
            if len(self.users) > 10:
                self.users.pop()

    # String output
    def __str__(self):
        out = str()
        i = 1

        # Convert each
        for user in self.users:
            a = str(user[0])
            b = str(int(float(user[1])))
            out += "|%2i" % int(i) + "|%-11s|%-11s|" % (a, b) + '\n'
            i += 1
        return out
