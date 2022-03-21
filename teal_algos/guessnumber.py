import random, sys  #A funny luck game,if your number equals to random integer you gain otherwise vice versa
ycoin=100 
def guessnumber(k:int): #if you give a bigger integer for k you can try to guess more time in a tour but cost and risk increase.
   x=random.randint(1,254)
   if(k==x):
        print('found k in '+str(k)+' times')
        return True
   elif(k>0):   
       return guessnumber(k-1)
   else:
        print('could not find')
        return False
print("Your balance at 0 moment : "+str(ycoin))
while ycoin>0:
    number=int(input("Rules are simple you can play as much as you have y coin,if you guess correct number you gain number/10 ycoin otherwise vice-versa!So please give an integer bigger than 0 and less than 127 otherwise you will exit of the game\n"))
    if(ycoin>=number/10 and number<=127):#changing number<127 will affect your gaining possibility for example if you put 254 you will generaly gain.
        a=guessnumber(number)
        ycoin=ycoin+number/10 if a==True else  ycoin-number/10
        print("Your balance "+str(ycoin))
        
        if number<=0 or ycoin==0:
            if ycoin==0:
                print("Liquidated!")
                sys.exit()
            print("See you,gamer👋")
            sys.exit()
        elif ycoin>=200: #increase or decrease this number to change diffucilty of game to easy or hard. 
             print("You succed to gain "+str(ycoin)+" You did a great job gamer but unfortunately this game cannot continue until forever.Thanks for playing❤️👋")
             sys.exit()
    else:
        print("Exiting the game👋")
        sys.exit()
