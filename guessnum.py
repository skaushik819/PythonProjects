print("WELCOME : GUESS THE NUMBER")
print("Enter your name")
n=input()
print("kindly guess the number(0-50)")
gnum=int(input())
import random
r=random.randint(0,50)
i=0
g=0
while(i<4):
        if(gnum==r):
            print("your guess is correct")
            print("you won at your %s attempt"%(i))
            g=1
            break
        elif(gnum<r):
            print("guessed number is smaller than the actual number")
            print("please guess the number again")
            gnum=int(input())
            i=i+1
        else:
            print("Guessed number is greater than the actual number")
            print("Please enter the value again")
            gnum=int(input())
            i=i+1
if(g==1):
    print("You won the game")
else:
    print("you lost")
