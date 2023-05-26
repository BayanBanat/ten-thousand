from game_logic import GameLogic
from sys import exit
from collections import Counter
import re

class Game:
    
    @staticmethod
    def welcoming_message():
        print( """Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
        
    @staticmethod
    def user_input():
        return input("> ")
    
    @staticmethod
    def dice_format(dices):
        dices_format = "*** "
        for space_holder in range(len(dices)):
            dices_format+="{} "
        dices_format+="***"
        print(dices_format.format(*dices))

    @staticmethod
    def get_dicees(size):
        print (f"Rolling {size} dice...")
        dices=GameLogic.roll_dice(size)
        Game.dice_format(dices)
        return list(dices)
    
    @staticmethod
    def Zilch(dices):
        zilch = GameLogic.calculate_score(dices)
        if zilch>0:
            return False
        else:
            return True

    @staticmethod
    def rounds(num):
        score=0
        print (f"Starting round {num}")
    
        dices = Game.get_dicees(6)
        print("Enter dice to keep, or (q)uit:")
        saved_dices = []
        Cheater = False
        while True:
            user_number=Game.user_input().replace(" ","")
            if user_number.lower()=="q":
                return False
            if user_number.lower()!= "b" and user_number.lower()!="r":
                dice_check = dices.copy()
                for element in user_number:
                    if int(element) in dice_check:
                        saved_dices.append(int(element))
                        dice_check.remove(int(element))
                    else:
                        saved_dices.clear()
                        print("Cheater!!! Or possibly made a typo...")
                        score=0
                        Game.dice_format(dices)
                        Cheater = True
                        break
                if Cheater:
                    Cheater = False
                    continue
                # print(saved_dices)
                score += GameLogic.calculate_score(tuple(saved_dices))
                lst_number=[element for element in dice_check]
                # print(lst_number)
                dices_count = Counter(saved_dices)
                # print(all(dice ==2 for dice in dices_count.values()))
                if len(saved_dices) == 6 and score>0:
                    lst_number=[0,0,0,0,0,0]
                    saved_dices.clear()
                dices=tuple(lst_number)
                print(f"You have {score} unbanked points and {len(lst_number)} dice remaining")
            elif user_number.lower()=="b":
                print(f"You banked {score} points in round {num}")
                return  score
            elif user_number.lower()=="r":
                dices = Game.get_dicees(len(dices))
                if Game.Zilch(dices):
                    score =0
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    print(f"You banked {score} points in round {num}")
                    return  score
                print("Enter dice to keep, or (q)uit:")
                continue
            
            print("(r)oll again, (b)ank your points or (q)uit:")

    @staticmethod       
    def end_game(string):
        exit(string)

    @staticmethod       
    def play():
        Game.welcoming_message()
        total_score=0
        round=1
        play_or_not=Game.user_input()
        while True:
            if play_or_not.lower() =="y":
                round_return=Game.rounds(round)
                if not round_return and isinstance(round_return,bool):
                    break
                total_score += round_return
                print(f"Total score is {total_score} points")
                round+=1

            else:
                Game.end_game("OK. Maybe another time")
                return
            
        Game.end_game(f"Thanks for playing. You earned {total_score} points")












if __name__=="__main__":
    # print(GameLogic.roll_dice(6))
    # print(GameLogic.calculate_score((1, 2, 3, 4, 5, 6)))

    # print (rounds(1))
    Game.play()

