import random

class GameLogic:
    def __init__(self):
        # self.score=0
        # self.dice=[]
        pass

    @staticmethod
    def calculate_score(dic_tuple):
        score=0
        straight=0
        pairs=0 # count for pairs
        dupplicat_list=[0 for index in range(7)]
        for element in dic_tuple:
            dupplicat_list[element]+=1
        for element in dupplicat_list:
            if element==1:
                straight+=1
            if element == 2:
                pairs+=1  # increase the count of pairs
            if element>=3:
                if dupplicat_list.index(element)==1:
                   score+=(dupplicat_list.index(element)*1000)*(element-2)
                   
                else:
                    score+=(dupplicat_list.index(element)*100)*(element-2)
                # dupplicat_list[dupplicat_list.index(element)]=0
            else:
                if dupplicat_list.index(element)==1:
                    score+=100*element
                if dupplicat_list.index(element)==5:
                    score+=50*element

            dupplicat_list[dupplicat_list.index(element)]=0
        
        if straight==6 or pairs==3: # check for pairs and straight value
            score=1500
        return score
    
    @staticmethod
    def validate_keepers(roll, keepers):
        roll_list = list(roll)
        keepers_list = list(keepers)
        for element in keepers_list:
            if element in roll_list:
                roll_list.remove(int(element))
            else:
                return False
        return True

    
    @staticmethod
    def roll_dice(number):
        dice_list=[]
        for index in range(number):
            random_number = random.randint(1, 6)  #create a random number between 1 to 6 
            dice_list.append(random_number)

        return tuple(dice_list)
    



    
if __name__ == "__main__":
    print(GameLogic.roll_dice(6))
    print(GameLogic.calculate_score((1, 2, 3, 4, 5, 6)))




