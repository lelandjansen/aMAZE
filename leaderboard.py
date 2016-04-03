

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
        if name == '':
            name = ""
        inserted = False
        length = len(self.users)
        if length > 10:
            length = 10
        if length == 0:
            self.users.append((name, str(score)))
        for i in range(length):
            userScore = int(float(self.users[i][1]))
            if userScore < score:
                inserted = True
                newUser = (name, str(score))
                self.users.insert(i, newUser)
                break
        if not inserted:
            self.users.append((name,str(score)))
        if len(self.users) > 10:
            self.users.pop()

    def __str__(self):
        out = str()
        i = 1
        for user in self.users:
            a = str(user[0])
            b = str(int(float(user[1])))
            out += "|%2i" % int(i) + "|%-11s|%-11s|" % (a, b) + '\n'
            i += 1
        return out
