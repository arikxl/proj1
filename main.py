
def deposit():
    while True:
        amount = input("How much to deposit? $")
        if amount.isdigit():
           amount = int(amount)
           if amount > 0: 
              break
           else:
              print("Amount need to be greater than 0")
        else:
            print("please enter a number")
    return amount

def main():
    balance = deposit()




main()