import random

from classes import HorsesRacing
from time import sleep


def random_contender():
        contender={
        "name":['Kind','Alex', 'Lilly','Sugar','Lady','Cash','Lucky','Kind','Chance','Rose',],
        "Breed":["american", "arabian", "thoroughbred",'gypsy','andalusian'],
        "Point":[50,60,70,80,90,100]
        }
        return [random.choice(contender['name']),random.choice(contender['Breed']),random.choice(contender['Point'])]


if __name__ == "__main__":

        

    



    

#     print(HorsesRacing.get_round_numbers())
#     j=f"{x} and {y} battled hard. It's a tie."

#     if (horse.racing(contender)) == g:
        # print(horse.racing(contender))
#     elif (horse.racing(contender)) == h:
        # print("do you want to play again ?")

#     elif (horse.racing(contender)) == j:
        # print(horse.racing(contender))
#     print(horse.racing(contender))

        horse = HorsesRacing()
        contender = HorsesRacing()
        horse.set_name(input("Enter your Horse name => "))
        lis=["american", "arabian", "thoroughbred", "gypsy", "andalusian"]
        e=input('choose his Breed : \n  american   arabian   thoroughbred    gypsy    andalusian \n => ')
        

        
        i=0
        while  i != 'q':
                if e not in lis :
                        print("!!!!!!!!!!!!!!!!!!!! WRONG CHOICE !!!!!!!!!!!!!!!!!!!!")
                        e=input('choose his Breed again : \n  american   arabian   thoroughbred    gypsy    andalusian \n => ')
                else:
                        horse.set_Breed(e)
                        x= horse.get_name()
                        lose=f"{x} fainted!"
                        contender.set_name(random_contender()[0])
                        contender.set_Breed(random_contender()[1])
                        contender.set_point(random_contender()[2])  
                        # print(horse.racing(contender))
                        rr=f"round {HorsesRacing.get_round_numbers()}"
                        # ''''

                        print(f"####################################################################### {rr} ###########################################")
                        def Loadbar(iteration, total,prefix='', suffix='', decimals=1, length=100, fill='>'   ):
                                percent = ('{0:.'+ str(decimals) + 'f}').format(100 * (iteration/float(total)))
                                filledLenength = int(length * iteration // total)
                                bar = fill * filledLenength + '_' * (length - filledLenength)
                                print(f'\r{prefix} | {bar} | {percent}% {suffix}', end='\r')
                                if iteration == total:
                                        print()

                        items = list(range(0, 50))
                        l = len(items)  
                        Loadbar(0,l,prefix=rr, suffix='Complete', length=l)
                        for i, item in enumerate(items):
                                sleep(0.03)
                                Loadbar(i + 1, l, prefix=rr, suffix='Complete', length=l)
                        print(f"####################################################################### {rr} ###########################################")

                        # '''
                        print(horse)
                        print(contender)
                        print(f"round {HorsesRacing.get_round_numbers()}")

                        if (horse.racing(contender)) == lose:
                                print(f"ooh no :( {horse.racing(contender)}")
                                w=input("do you need to play again? [y/n] ==> ")
                                if w == 'y' or w== 'Y' :
                                        i=0
                                elif w == 'n' or w== 'N' : 
                                        print(rr)
                                        print("***********************Thank you for playing*************************")
                                        i='q'    
                        else:
                                i=0


















'''

# ========================================================================================================
    def Loadbar(iteration, total,prefix='', suffix='', decimals=1, length=100, fill='>'   ):
            percent = ('{0:.'+ str(decimals) + 'f}').format(100 * (iteration/float(total)))
            filledLenength = int(length * iteration // total)
            bar = fill * filledLenength + '_' * (length - filledLenength)
            print(f'\r{prefix} | {bar} | {percent}% {suffix}', end='\r')
            if iteration == total:
                    print()
    
    items = list(range(0, 50))
    l = len(items)  
    Loadbar(0,l,prefix='progress:', suffix='Complete', length=l)
    for i, item in enumerate(items):
            sleep(0.05)
            Loadbar(i + 1, l, prefix='progress:', suffix='Complete', length=l)
    for i, item in enumerate(items):
            sleep(0.05)
            Loadbar(i + 1, l, prefix='progress:', suffix='Complete', length=l)
# ========================================================================================================

'''
