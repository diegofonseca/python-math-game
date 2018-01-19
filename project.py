try:
    from gameclasses import BinaryGame, MathGame
    from gametasks import getUserScore, printInstructions, updateUserScore
    nickname = input("Give your nickname:")
    oldScore = getUserScore(nickname)
    if oldScore == "-1":
        updateUserScore(nickname, 0, True)
    else:
        print("*"*10,"Higher score: {}".format(oldScore), "*"*10, sep="\n")

    while True:
        print("="*40)
        print("Choose a game:")
        print("1. Binary Game")
        print("2. Math Game")
        print("3. Exit")
        print("="*40)
        opt = input("Game: ")
        if opt == "3": exit()

        qtd = int(input("How many questions?"))
        game = BinaryGame(qtd) if opt == 1 else MathGame(qtd)
        print(game.instructions())
        score = game.generateQuestions()
        print(score, oldScore)
        if score > int(oldScore):
            updateUserScore(nickname, score)
            print("*"*10,"New higher score: {}".format(score), "*"*10, sep="\n")
        print("YOUR SCORE: {}".format(score))
except:
    print('Is there a problem. The Game will exit. Press enter to continue.')
