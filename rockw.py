print=("please pick one rock paper or scissors")

while True:
    game_dict={'rock':1,'scissors':2,'paper':3}
    player_a= str(input("player_a"))
    player_b= str(input("player b"))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dit =a - b

    if dit in [-1,2]:
        print("player_a wins")
        if str(input("do you want to play another round yes or no\n"))=="yes":
            continue
        else:
            print("game is over ")
            break
    elif dit in [-2,1]:
        print("player_b wins") 
        if str(input("do you want to play another round yes or no\n"))=="yes":
            continue
        else:
            print("game over")
        break
    else:
        print("its a tie ")
        print(' :)')



