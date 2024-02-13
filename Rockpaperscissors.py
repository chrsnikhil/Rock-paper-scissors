import random
lst=["rock","paper","scissors"]
x=random.choice(lst)
play=input("Rock,Paper or scissors?")
print("The computer chose",x)
if play==x:
    print("It is a draw")
elif play=="rock" and x=="scissors":
    print("You win!!")
elif play=="rock" and x=="paper":
    print("You lose!!")
elif play=="paper" and x=="scissors":
    print("You lose")
elif play=="paper" and x=="rock":
    print("You win")
elif play=="scissors" and x=="paper":
    print("You win")
elif play=="scissors" and x=="rock":
    print("You lose!!")

