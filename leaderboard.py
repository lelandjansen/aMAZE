

class Leaderboard:

    def __init__(self):
        self.users = list()

    def readLeaderboard(self):
        self.users = list()
        with open("scores.txt") as f:
            for line in f:
                line = line.split()
                line = (line[0], line[1])
                self.users.append(line)


    def writeLeaderboard(self):
        with open("scores.txt", "w") as f:
            for user in self.users:
                line = str(user[0]) + " " + str(user[1]) + "\n"
                f.write(line)

    def addUser(self, name, score):
        length = len(self.users)
        if length > 10:
            length = 10
        for i in range(length):
            userScore = int(self.users[i][1])
            print(i)
            if userScore < score:
                print("ran")
                newUser = (name, str(score))
                self.users.insert(i, newUser)
                break
        if len(self.users) > 10:
            self.users.pop()

    def __str__(self):
        out = str()
        i = 1
        for user in self.users:
            a = str(user[0])
            b = str(user[1])
            out += "|%2i" % int(i) + "|%-11s|%-11s|" % (a, b) + '\n'
            i += 1
        return out
