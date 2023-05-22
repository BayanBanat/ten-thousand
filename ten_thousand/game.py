from game_logic import GameLogic

def welcoming_message():
    print( """Welcome to Ten Thousand
(y)es to play or (n)o to decline""")

def user_input():
    return input("> ")

def rounds(num,total_score):
    score=0
    print (f"Starting round {num}")
    print ("Rolling 6 dice...")
    dices=GameLogic.roll_dice(6)
    print("*** {} {} {} {} {} {} ***".format(*dices))
    print("Enter dice to keep, or (q)uit:")
    while True:

       
        user_number=user_input().replace(" ","")
        if user_number=="q":
            return False
        if user_number!= "b" and user_number!="r":
            # print("hello")
            lst_number=[int(element) for element in user_number if int(element) in dices]
            # print(lst_number)
            score+=GameLogic.calculate_score(tuple(lst_number))
            lst_number=[element for element in dices if element not in  lst_number]
            # print(lst_number)
            dices=tuple(lst_number)
            print(f"You have {score} unbanked points and {len(lst_number)} dice remaining")
        elif user_number=="b":
            print(f"You banked {score} points in round {num}")
            return  score
        # else:
            
        print("(r)oll again, (b)ank your points or (q)uit:")
           

            
def play():
    welcoming_message()
    total_score=0
    play_or_not=user_input()
    round=1
    while True:
        if play_or_not =="y":
            round_return=rounds(round,total_score)
            if not round_return and isinstance(round_return,bool):
                break
            total_score += round_return
            print(f"Total score is {total_score} points")
            round+=1

        else:
            print("OK. Maybe another time")
            return
    print(f"Thanks for playing. You earned {total_score} points")











if __name__=="__main__":
    # print(GameLogic.roll_dice(6))
    # print(GameLogic.calculate_score((1, 2, 3, 4, 5, 6)))

    # print (rounds(1))
    play()

