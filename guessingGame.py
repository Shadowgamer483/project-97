import random
print("HEY U YESS U GUESS THAT NUMBER !! ")

name=input("what is ur name")
number=random.randint(1,10)
chances=0
print("so heres the game guess a number from 1-10 i think off u get 3 chances if u dont get it u die(not irl) R.I.P if u do UR A WIZARD HARRY .GOOD LUCK YOU WILL I MEAN WILL NEED IT"+name)
while chances < 3:
    geuss=int(input("ENTER UR GUESS NOW "+name))
    if geuss==number: 
        print("CONGRATS U WON U DIDNT DIE WANNA PLAY AGAIN  "+name)
        break
    elif geuss < number:
        print("HAHAH UR GUESS WAS 2 LOW UR GONA LOSE :)  "+name)
    else :
        print("UR GUESS WAS 2 HIGH UR GONA LOSE :)  "+name)
    chances=chances+1
    if not chances <3:
        print("U LOSE THE NUMBER IS................  "+number)    






