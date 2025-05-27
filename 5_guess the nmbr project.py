# Guess the number game in python project
# computer memeory te 1ta random number select korbee , tarpor computer user ke bolbe tmi nmbr ta guess korte parbe kina?


import random
myNum = random.randint(0, 9)#computer guess number
print("I have a number in My mind, can you guess it?")


while True:
  
    userNum = int(input("Enter your number: "))


    if userNum == myNum:
       print("You are right\n")
       break 

    elif userNum > myNum:
       print("My number is greater than your entered number,\n Try Agian!")

    else:
       print("My number is less than your entered number,\n Try Again!")

