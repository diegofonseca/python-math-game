def printInstructions():
    print("="*10)
    print("Instructions")
    print("="*10)

def getUserScore(username):
    retorno = "-1"
    try:
        file = open('userScores.txt','r')
        for line in file:
            user = line.split(',')
            if user[0] == username:
                retorno = user[1]
        file.close()
        return retorno
    except IOError:
        file = open('userScores.txt','w')
        file.close()
        return retorno

def updateUserScore(username, score, newUser = False):
    from os import rename, remove
    if newUser:
        file = open('userScores.txt', 'a')
        file.write("{},{}\n".format(username, score))
        file.close()
    else:
        new = open('userScores.tmp', 'w')
        old = open('userScores.txt', 'r')
        for line in old:
            user = line.split(',')
            if user[0] == username:
                new.write("{},{}\n".format(username, score))
            else:
                new.write(line)
        new.close()
        old.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
