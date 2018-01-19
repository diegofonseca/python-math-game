class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            value = 1
            print("Minimum Numer Of Questions = 1")
        print("Hence, number of questions will be set to {}".format(value))
        self._noOfQuestions = value

class BinaryGame(Game):
    def instructions(self):
        return """
            In this game, you will be given a number in base 10.
            Your taks is to convert this number to base 2.
            Each correct answer gives you one mark.
            No mark is deducted for wrong answers.
        """

    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(0,self.noOfQuestions):
            base10 = randint(1,1000)
            while True:
                try:
                    print("What's the base10 of the number: {}".format(base10))
                    userResult = input("Type the answer:")
                    if base10 == int(userResult, base=2):
                        score +=1
                        input("Congratulations. It's correct.\n\nType enter to continue...")
                    else:
                        print("Wrong answer. The correct answer is {:b}".format(base10))
                    break
                except:
                    print("-"*35,"You type a non base10 number. Try again.","-"*35,sep="\n")
        return score

class MathGame(Game):
    def instructions(self):
        return """
            In this game, you will be given a simple arithmetic question.
            Each correct answer gives you one mark.
            No mark is deducted for wrong answers.
        """

    def __generateString(self, numberList, symbolList):
        return ("{}".join(str(number) for number in numberList)).format(*symbolList)

    def __generateQuestion(self):
        from random import randint
        numberList = [randint(1,9) for i in range(1,6)]
        operatorDict = {1: '+', 2: '-', 3: "*", 4: "**"}
        symbolList = []
        sqrt = 0
        for symbol in [operatorDict[randint(1,4)] for i in range(1,6)]:
            if symbol == "**" and sqrt == 0: sqrt+=1
            if sqrt > 0: symbol = operatorDict[randint(1,3)]
            symbolList.append(symbol)

        return self.__generateString(numberList, symbolList)

    def generateQuestions(self):
        score = 0

        for i in range(0,self.noOfQuestions):
            question = self.__generateQuestion()
            while True:
                try:
                    print("Whats the answer for: {}".format(question.replace('**','^')))
                    userResult = input("Type the answer:")
                    if int(userResult) == eval(question):
                        score +=1
                        input("Congratulations. It's correct.\n\nType enter to continue...")
                    else:
                        print("Wrong answer. The correct answer is {}".format(eval(question)))
                    break
                except:
                    print("-"*35,"You type a non number. Try again.","-"*35,sep="\n")

        return score
