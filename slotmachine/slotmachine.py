import random

def populateSlot(slotMachine):
    for row in range(0, 3):
        for column in range(0, 5):
            slotMachine[row][column] = random.randint(0, 4)
    return slotMachine

def printSlotScreen(slotMachine):
    for row in range(0, 3):
        rowToPrint = "["
        for column in range(0, 5):
            rowToPrint += str(slotMachine[row][column])
            if column < 4:
                rowToPrint += " | "
        print(rowToPrint, "]")

def slotChecker(slotMachine, currentRow, currentColumn, checkNum):
    """
    [0, 2, 5, 6, 3 ]
    [3, 0, 6, 6, 5 ]
    [8, 6, 0, 0, 6 ]
    """

    if currentColumn == 5:
        print("You Win!")
        return True
    if currentRow < 0 or currentRow > 2 or currentColumn > 4 or currentColumn < 0 or slotMachine[currentRow][currentColumn] != checkNum:
        return False
    winner = slotChecker(slotMachine, currentRow - 1, currentColumn + 1, checkNum) or slotChecker(slotMachine, currentRow, currentColumn + 1, checkNum) or slotChecker(slotMachine, currentRow + 1, currentColumn + 1, checkNum) 
    return winner



def playSlot(slotMachine, balance):
    betAmount = 0
    while balance < betAmount or betAmount < 1:
        try:
            betAmount = int(input("Please enter new bet amount: "))
            if str(betAmount).__contains__("."):
                    print("Amount must be a whole number without a decimal")
                    betAmount = 0
            if betAmount < 1:
                    print("Bet amount is not high enough bet must be higher than 0 ")
            if betAmount > balance:
                    print("Bet amount exceeds total balance! ")
        except(ValueError, TypeError):
            print("Invalid bet amount please enter a number greater than 0 but less than or equal to your balance Balance:", balance)
    populateSlot(slotMachine)
    printSlotScreen(slotMachine)
    for row in range(0,3):
        if slotChecker(slotMachine, row, 0, slotMachine[row][0]):
            return [True, betAmount]
    return [False, betAmount]    
                
                
"""
Hello this is the beginning of running my code
"""

balance = 0
while balance <= 0:
    try:
        balance = float(input("Please enter an amount of money to add to your balance "))
        if balance <= 0:
            print("Please enter an amount greater than 0 ")
    except(TypeError, ValueError):
        print("Error not a number, please enter a valid number ")
print("Your Balance is", str(balance), " ")

slotmachine = [[0, 2, 5, 6, 0 ],[3, 0, 3, 0, 3 ],[8, 6, 0, 3, 6 ]]
play = True
while play == True:
    playResults = ["",""]
    playResults = playSlot(slotmachine, balance)
    betAmount = playResults[1]
    winresults = playResults[0]
    if winresults:
        print("You win")
        balance += (betAmount*5)
        print("New Balance: ", str(balance))
    else:
        print("You lose")
        balance -= betAmount
        print("New Balance: ", str(balance))
    playAgain = input("Do you wish to play again? y/n ").lower()
    while not playAgain == "n" and not playAgain == "no" and not playAgain == "yes" and not playAgain == "y":
        playAgain = input("Please enter \'yes\', \'no\', \'n\', or \'y\'")
    if playAgain == "n" or playAgain == "no":
        play = False
    if playAgain == "y" or playAgain == "yes":
        play = True
print("Thank you for playing")