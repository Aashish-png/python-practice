import sys

user1=input("whats your name ")
user2=input("and your name")

user1ans=input("%s do you want to choose rock paper or scissors "% user1)
user2ans=input("%s do you want to choose rock paper or scissors "% user2)

def compare(u1,u2):
    if u1==u2:
        return("its a tie")
    if u1=='rock':
        if u2=='scissors':
            return("rock wins")
        else:
            return("paper wins")
    elif u1=='scissors':
        if u2=='paper':
            return("scissors wins")
        else:
            return("rock wins")
    elif u1=='paper':
        if u2=='rock':
            return("paper wins")
        else:
            return("scossors")
    else:
        return("you have seleted the invaild value")
        sys(exit)

print(compare(user1ans,user2ans))
              


