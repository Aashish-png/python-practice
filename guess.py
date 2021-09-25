import random

min=1
max=9
number=random.randint(min,max)
guess= None
another=None
Try1=0
runnig = True

print ("Aright...")
try:
 while runnig:
    guess=input("what's your lucky number")
   
    if int(guess)<number:
        print("worng too low")
    elif int(guess)> number:
        print("worng too high")
    elif guess.lower()=="exit":
        print("better luck next time")
    elif int(guess)==number:
        print("yes this is the one,%s"%str(number))
        if Try1<2:
            print("great,only,%s"%str(Try1))
        elif Try1>2 and Try1<10:
            print("good %s tries."% str(Try1))
        else:
            print("bad %s tries "% str(Try1))
        runnig= False
    Try1+=1            
except:
        print("invaild entry")
        
