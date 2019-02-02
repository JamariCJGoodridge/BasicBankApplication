import math
import sys

print("This is a banking example developed by Jamari, that stores data in other files.\n")
print("When asked to make a transaction, you have several options to start.")
print("clear -> reseting all data.")
print("yes -> start of main loop.")
print("no -> end program.")
print("you can exit after any transaction by typing QUIT.\n")

def addStartingBalance():
    print("RESET STARTING BALANCE?")
    addStart = str(input())
    addStart = addStart.lower()
    if addStart == "y" or addStart == "yes":
        file = open("Bank Data.txt", "w")
        file.write(str(100))
    print("RESET OLD LOGS?")
    erase = str(input())
    erase = erase.lower()
    if erase == "y" or erase == "yes":
        file = open("Transaction Log.txt", "w")
        file.write("START")
    prompt()

def prompt():
    print("Would you like to make a transaction?")
    transact = str(input())
    transact = transact.lower()
    startup(transact)

def startup(confirm):
    run = True
    while run:
      if confirm == "yes" or confirm == "y":
        transaction_option()
      elif confirm == "no" or confirm == "n" or confirm == "quit" or confirm == "q":
        print("Exiting...")
        sys.exit()
      elif confirm == "clear" or confirm == "c":
          addStartingBalance()
      else:
        print("Input invalid")
        prompt()

def transaction_option():
    print("\nWould you like to make a deposit or withdrawal")
    change = str(input(""))
    change = change.lower()
    if change == "deposit" or change == "d":
        deposit_money()
    elif change == "withdrawal" or change == "w":
        withdrawMoney()
    elif change == "quit" or change == "exit":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid input")
        
def checkBalance():
    file = open("Bank Data.txt", "r")
    print("Current balance")
    print(file.read())
    current = open("Bank Data.txt", "r").read()
    floatCurrent = float(current)
    file.close()
    
def deposit_money():
    checkBalance()
    depositAction()

def depositAction():
    try:
        file = open("Bank Data.txt", "r")
        current = open("Bank Data.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("How much would you like to deposit?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Bank Data.txt", "w")
        newAmount = floatCurrent + floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Bank Data.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "+"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")


def withdrawMoney():
    checkBalance()
    withdrawalAction()

def withdrawalAction():
    try:
        file = open("Bank Data.txt", "r")
        current = open("Bank Data.txt", "r").read()
        floatCurrent = float(current)
        file.close()
    
        print("How much would you like to withdraw?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Bank Data.txt", "w")
        newAmount = floatCurrent - floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Bank Data.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "-"
        transactionLogs(floatCurrent, transactionOccured, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")

    

def transactionLogs(floatCurrent, transactionOccured, floatAddedAmount,newAmount):
    LOG = open("Transaction Log.txt", "a")
    oldAmount = floatCurrent
    oldAmount = str(floatCurrent)
    transactionType = transactionOccured
    transactionAmount = floatAddedAmount
    transactionAmount = str(transactionAmount)
    updatedAmount = newAmount
    updatedAmount = str(newAmount)
    LOG.write("\n\nOld Balance: " + oldAmount)
    LOG.write("\nTransaction Occured: " + transactionType + transactionAmount)
    LOG.write("\nNew Balance: " + updatedAmount)
    

def main():
    prompt()
    

main()

    
