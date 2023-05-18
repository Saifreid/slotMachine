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



def playSlot(slotMachine, balance, betAmount):
    populateSlot(slotMachine)
    printSlotScreen(slotMachine)
    if balance < betAmount or betAmount < 1:
        print("Bet amount is greater than balance reenter a bet amount or less than 1")
    while balance < betAmount or betAmount < 1:
        try:
            betAmount = int(input("Please enter new bet amount: "))
            if str(betAmount).__contains__("."):
                    print("Amount must be a whole number without a decimal")
                    betAmount = 0
        except(ValueError, TypeError):
            print("Invalid bet amount please enter a number greater than 0 but less than your balance Balance:", balance)
    for row in range(0,3):
        if slotChecker(slotMachine, row, 0, slotMachine[row][0]):
            return True
    return False    
                
                
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
print(slotmachine)
play = True
betAmount = 0
while betAmount < 1:
            try:
                betAmount = int(input("Please enter a whole number amount to bet greater than 0: "))
                if str(betAmount).__contains__("."):
                    print("Amount must be a whole number without a decimal")
                    betAmount = 0
            except(TypeError, ValueError):
                print("Please enter a valid whole number greater than 0")
while play == True:
    if playSlot(slotmachine, balance, betAmount):
        balance += betAmount
        print("You win")
        print("New Balance: ", str(balance))
    else:
        balance -= betAmount
        print("You lose")
        print("New Balance: ", str(balance))
    playAgain = input("Do you wish to play again? y/n ").lower()
    while not playAgain == "n" and not playAgain == "no" and not playAgain == "yes" and not playAgain == "y":
        playAgain = input("Please enter \'yes\', \'no\', \'n\', or \'y\'")
    if playAgain == "n" or playAgain == "no":
        play = False
    if playAgain == "y" or playAgain == "yes":
        betAmount = 0
        while betAmount < 1:
            try:
                betAmount = int(input("Please enter amount to bet greater than 0: "))
                if str(betAmount).__contains__("."):
                    print("Amount must be a whole number without a decimal")
                    betAmount = 0
            except(TypeError, ValueError):
                print("Please enter a valid number greater than 0")
print("Thank you for playing")