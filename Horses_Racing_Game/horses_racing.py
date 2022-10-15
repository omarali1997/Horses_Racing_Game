import random
from time import sleep
from classes import HorsesRacing


def random_contender():

    '''
    A Function that will choose your contender randomly depends on contender dictionary. 
    '''

    contender={
    "name":['Kind','Alex', 'Lilly','Sugar','Lady','Cash','Lucky','Kind','Chance','Rose',],
    "Breed":["american", "arabian", "thoroughbred",'gypsy','andalusian'],
    "Point":[50,60,70,80,90,100]
    }
    return [random.choice(contender['name']),random.choice(contender['Breed']),random.choice(contender['Point'])]

                        # #################### Create Load Bar #################### #

def Loadbar(iteration, total,prefix='', suffix='', decimals=1, length=100, fill='>'   ):
                            percent = ('{0:.'+ str(decimals) + 'f}').format(100 * (iteration/float(total)))
                            filledLenength = int(length * iteration // total)
                            bar = fill * filledLenength + '_' * (length - filledLenength)
                            print(f'\r{prefix} | {bar} | {percent}% {suffix}', end='\r')
                            if iteration == total:
                                    print()


def draw_horse():
    a = """
    *************************************************************************************
            Welcome to                   O  ,--.
            Horse Racing Game         _ /|\/  /\|
                                 ,;( )__7,  )
                                 /  //  // '--.
                                 '    \,   ,' '
       ** Let's see how many rounds your horse will race before it faints.           ** 
       ** The game will start once you write your horse's name and choose his breed. **
       ** And your contender will be chosen randomly ...                             **
       ** Each round you win your points will increase by 10 and your contender      **
       ** will lose 10 points ...                                                    **
       ** If the result is tied your points will decrease by 10 and your contender   **
       ** will get 10 points...                                                      **
       ** If you fail your points will be zero and your horse will be fainted...     ** 
       **                                                                            **
       ** So here we are starting...                                                 **
    **************************************************************************************
    """

    b = """
    ************************************************
    Thank you for playing       O  ,--.
    Horse Racing Game        _ /|\/  /\|
                         ,;( )__7,  )
                         /  //  // '--.
                         '    \,   ,' '
    ************************************************
    Created By : 
                ************    ********************
                * Omar_Ali *    * Amani M AL-Zoubi *  
                ************    ********************
    *************************************************
    """
    return a,b
       
if __name__ == "__main__":

    print(draw_horse()[0])
    horse = HorsesRacing()
    contender = HorsesRacing()
    horse.set_name(input("Enter your Horse name => "))
    lis=["american", "arabian", "thoroughbred", "gypsy", "andalusian"]
    e=input('choose his Breed : \n  american   arabian   thoroughbred    gypsy    andalusian \n => ')     
    i=0

                        # #################### Start The Game #################### #

    while  i == 0 :
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
                    print("\n******************************************************************************")  
                    print(f"\n           {horse} ** VS ** {contender}  \n")
                    print("*******************************************************************************\n")
                    hr=horse.racing(contender)
                    rr=f"ROUND {HorsesRacing.get_round_numbers()}"
                    sleep(1)  


                    print(f"####################################################################### {rr} ###########################################\n")
                    
                    items = list(range(0, 50))
                    l = len(items)  
                    Loadbar(0,l,prefix=rr, suffix='Complete', length=l)
                    for i, item in enumerate(items):
                            sleep(0.04)
                            Loadbar(i + 1, l, prefix=rr, suffix='Complete', length=l)

                    print(f"\n {hr}")
                    print(f"\n####################################################################### {rr} ###########################################\n")
                    print(f" {horse} ")
                    print(f" {contender} ")
                    print(f" ROUND {HorsesRacing.get_round_numbers()} ")

                        # #################### check if user want to continue or not #################### #

                    if hr == lose:
                            print(f" \n OoOh NoOoO >_< {horse.get_name()} fainted \n\n ############################# \n")
                            w=input("Do You Want To Play Again ?! [y/n] ==> ")

                            while w not in ['y','Y','N','n']:
                               w=input(">>>> Please Choose [y/n] ==> ")  
                            if w == 'y' or w== 'Y' :
                                i=0
                            elif w == 'n' or w== 'N' : 
                                print(rr)
                                print(draw_horse()[1])
                                i=1  
                    else:
                            i=0