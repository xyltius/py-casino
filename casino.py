
import random as rn
import time as t
import copy as c


def blackjack(tot):
    #takes total seed money as argument 
    #if seed money is less than equal to zero, exits function  
    if tot<=0:
        print("Out of Money. Please restart.")
        return
    
    
    #blackjack functions:    
    def hit(lst,deck):
        #append new card to dealer or player hand
        card=deck.pop()
        if card==1:
            card="A"
        elif card==11:
            card="J"
        elif card==12:
            card="Q"
        elif card==13:
            card="K"
        lst.append(card)
        return card
    
    
    def sum_hand(lst):
        #sum of card value of dealer or player hand
        cnt=lst.count('A')
        lst=[x for x in lst if x!='A']
        lst.extend(['A' for x in range(cnt)])
        total=0
        for i in lst:
            if i=="J" or i=="Q" or i=="K":
                total+=10
            elif i in [2,3,4,5,6,7,8,9,10]:
                total+=i
            else:
                total+=11
                if total>21:
                    total-=11
                    total+=1
        return total
    
    
    def show(lst1,lst2):
        #show dealer and player hand
        print("Dealer's Hand: ",end="")
        [print(lst1[i],end=" ") for i in range(len(lst1))]
        print("\nTotal:",sum_hand(lst1))
        t.sleep(1.7)
        print("\nPlayer's Hand: ",end="")
        [print(lst2[i],end=" ") for i in range(len(lst2))]
        print("\nTotal:",sum_hand(lst2),"\n")
        t.sleep(1.7)
    
    
    def check(lst1,lst2,deck,amt):
        #win check and if dealer card sum is less than or equal to 16, then hits
        #returns a tuple of amount won and amount bet
        while sum_hand(lst1)<21:
            if sum_hand(lst1)<=16:
                hit(lst1,deck)
                show(lst1,lst2)
            else:
                break
        if sum_hand(lst1)==21 or sum_hand(lst2)==21:
            if sum_hand(lst1)==21:
                print("Dealer got blackjack. Dealer wins.\nPayout:",amt-amt)
                return amt-amt,amt
            elif sum_hand(lst2)==21:
                print("Player got blackjack. Player wins.\nPayout:",amt*(3.0))
                return amt*(3.0),amt
            elif sum_hand(lst1)==sum_hand(lst2):
                print("Equal value. Draw.\nPayout:",amt)  
                return amt,amt
        elif sum_hand(lst1)>21 and sum_hand(lst2)<21:
            print("Dealer busted. Player wins.\nPayout:",amt*(2.0))    
            return amt*(2.0),amt
        elif sum_hand(lst1)<21 and sum_hand(lst2)>21:
            print("Player busted. Dealer wins.\nPayout: ",amt-amt)
            return amt-amt,amt
        elif sum_hand(lst1)==sum_hand(lst2):
            print("Equal value. Draw.\nPayout:",amt)
            return amt,amt
        elif sum_hand(lst1)>sum_hand(lst2):
            print("Dealer has higher value. Dealer wins.\nPayout:",amt-amt)
            return amt-amt,amt
        elif sum_hand(lst1)<sum_hand(lst2):
            print("Player has higher value. Player wins.\nPayout:",amt*(2.5))
            return amt*(2.5),amt
            
    
    #the main blackjack game:
    current_deck=[i for i in range(1,14)]*4
    #creates deck of cards excluding joker and suits don't matter
    rn.shuffle(current_deck)
    #shuffles deck created in function
    bet=float(input("Enter bet amount from seed money: "))
    #bet entered by player is taken from seed money
    if bet>tot:
        print("Bet exceeded seed amount.")
        return 0,0
    elif bet<=0:
        print("Bet amount invalid.")
        return 0,0
    t.sleep(0.6)
    #if bet exceeds seed money or is less than equal to zero, exits function
    print()
    dealer=[]
    player=[]
    dealer=[hit(dealer,current_deck) for i in range(2)]
    #creates dealer's hand from current deck and removes cards chosen 
    player=[hit(player,current_deck) for i in range(2)]
    #creates player's hand from current deck and removes cards chosen
    print("Dealer's Hand: ",end="")
    [print(dealer[i],end=" ") for i in range(len(dealer)-1)]
    print("HIDDEN")
    print("Total:",sum_hand(dealer[:-1]),"+ HIDDEN")
    t.sleep(1.7)
    print("\nPlayer's Hand: ",end="")
    [print(player[i],end=" ") for i in range(len(player))]
    print("\nTotal:",sum_hand(player),)
    #shows dealer's and player's hand but hides dealer's second card 
    t.sleep(1.7)

    if sum_hand(dealer)==21 or sum_hand(player)==21:
        print()
        show(dealer,player)
        if sum_hand(dealer)==21:
            print("Dealer got blackjack. Dealer wins.\nPayout:",bet-bet)
            return bet-bet,bet
        elif sum_hand(player)==21:
            print("Player got blackjack. Player wins.\nPayout:",bet*(4.0))
            return bet*(4.0),bet
        elif sum_hand(dealer)==sum_hand(player)==21:
            print("Dealer and Player got blackjack. Draw.\nPayout:",bet)
            return bet,bet
    #if dealer or player gets natural blackjack, returns based on outcome 
    else:        
        ans=input("Stand(s) or Hit(h)? ")
        #asks player to stand with current card or hit for new card  
        print()
        if ans=="s" or ans=="S":
            show(dealer,player)
            return check(dealer,player,current_deck,bet)
        elif ans=="h" or ans=="H":
            hit(player,current_deck)
            show(dealer,player)
            return check(dealer,player,current_deck,bet)
        else:
            print("Invalid response.")
    #returns based on 'check' function
            

def roulette(tot):
    if tot<=0:
        print("Out of Money. Please restart.")
        return
    #the main roulette game
    pockets=[x for x in range(1,37)]
    #creates list of pockets numbered from 1 to 37
    dic={}
    for k in pockets:
        if k in range(1,11):
            if k%2!=0:
                dic[k]='red'
            else:
                dic[k]='black'
        elif k in range(11,19):
            if k%2==0:
                dic[k]='red'
            else:
                dic[k]='black'
        elif k in range(19,29):
            if k%2!=0:
                dic[k]='red'
            else:
                dic[k]='black'
        else:
            if k%2==0:
                dic[k]='red'
            else:
                dic[k]='black'
    #creates dictionary based on pocket colour and number
    pockets.extend([x for x in range(1)])
    dic[pockets[-1]]='green'
    #appends 0 to pockets list and adds 0 and green to dic
    bet=float(input("Enter bet amount from seed money: "))
    if bet>tot:
        print("Bet exceeded seed amount.")
        return 0, 0
    elif bet<=0:
        print("Bet amount invalid.")
        return 0, 0
    t.sleep(0.6)
    print("""\nThe roulette wheel:
0 (Neither odd nor even - green)
1-10 (odd - red, even - black)
11-18 (odd - black, even - red)
19-28 (odd - red, even - black)
29-36 (odd - black, even - red)\n""")
    t.sleep(1.9)
    #prints all pockets and their related colour
    print("""Choose your bet:
Colour: Red(r), Black(b) or Green(g)
Parity: Odd(o) or Even(e)
Range: Low No.1-18(l) or High No.19-36(h)
No.: (Enter no. between 0-36 inclusive)
Grouping: Inclusive of( <Low No.> , <High No.>)""")
    t.sleep(1.9)
    #prints all possible states to bet on
    choice=input("Choice: ")
    #enter state you choose to bet on
    win=rn.choice(list(dic.keys()))
    t.sleep(0.8)
    #random pocket is chosen from pockets list
    print("\nThe roulette wheel spins...")
    t.sleep(2.0)
    print("The ball lands on {} and the colour is {}!\n".format(win,dic[win]))
    t.sleep(1.3)
    #prints chosen pocket and it's related colour
    #checks whether chosen pocket exists in chosen bet state
    #basen on outcome, returns a tuple of amount won and amount bet
    if choice=='r' or choice=='R':
        if dic[win]=='red':
            print("You have won!\nPayout:",bet*(1.7))
            return bet*(1.7),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)
            return bet-bet,bet
        
    elif choice=='b' or choice=='B':
        if dic[win]=='black':
            print("You have won!\nPayout:",bet*(1.7))
            return bet*(1.7),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)
            return bet-bet,bet
        
    elif choice=='g' or choice=='G':
        if dic[win]=='green':
            print("You have won!\nPayout:",bet*(4.0))
            return bet*(4.0),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)
            return bet-bet,bet
   
    elif choice=='o' or choice=='O':
        if win%2!=0:
            print("You have won!\nPayout:",bet*(1.5))
            return bet*(1.5),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)
            return bet-bet,bet
    
    elif choice=='e' or choice=='e':
        if win%2==0:
            print("You have won!\nPayout:",bet*(1.5))
            return bet*(1.5),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)
            return bet-bet,bet
        
    elif choice=='l' or choice=='L':
        if win in range(1,19):
            print("You have won!\nPayout:",bet*(1.5))
            return bet*(1.5),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)     
            return bet-bet,bet
        
    elif choice=='h' or choice=='H':
        if win in range(19,37):
            print("You have won!\nPayout:",bet*(1.5))
            return bet*(1.5),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)  
            return bet-bet,bet
        
    elif choice.isdigit():
        if int(choice)==0 and win==0:
            print("You have won!\nPayout:",bet*(4.0))
            return bet*(4.0),bet
        elif int(choice)==win:
            print("You have won!\nPayout:",bet*(3.5))
            return bet*(3.5),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)
            return bet-bet,bet
        
    elif choice.replace(',','').isdigit(): 
        low=int(choice.split(",")[0])
        high=int(choice.split(",")[1])
        diff=high-low+1
        if low<0 or high<0 or high>36 or diff<=1:
            print("Invalid End points. Try again.")
            return bet,bet
        elif 24<=diff<=36:
            print("Entry is too large. Try again.")
            return bet,bet
        elif win in range(low,high+1) and 12<diff<24:
            print("You have won!\nPayout:",bet*(2.2))
            return bet*(2.2),bet
        elif win in range(low,high+1) and 1<diff<12:
            print("You have won!\nPayout:",bet*(2.4))
            return bet*(2.4),bet
        else:
            print("Better luck next time!\nPayout:",bet-bet)        
            return bet-bet,bet
        
    else:
        print("Invalid Input. Try again.")
        

def slot_machine(tot):
    if tot<=0:
        print("Out of Money. Please restart.")
        return
    
    
    #slot-machine functions:
    def col_create(syms):
        #creates random shuffled column based on copy of all symbols list
        syms_copy=c.copy(syms)
        rn.shuffle(syms_copy)
        return syms_copy

    
    def col_shuffle():
        #shuffles the 3 columns and returns a 3x3 
        #matrix of middle symbols of columns
        symbols=['$','2','3','combo','a','a','b','b','c']
        col1=col_create(symbols)
        col2=col_create(symbols)
        col3=col_create(symbols)
        col_=[col1,col2,col3]
        col_=[[col_[i][j] for i in range(3)] for j in range(3,6)]
        return col_
    

    def col_show(col):
        #displays the 3x3 matrix of the columns with row and column no.
        t.sleep(0.8)
        print("1:      2:      3:".center(34))
        for i in range(len(col)):
            print(f"{i+1}:    ",end="")
            for j in col[i]:
                print(j.center(5),end='   ')
            print()
        print()
        t.sleep(1.2)
    

    def win_states(col,amt):
        #determines if player has won based on 3x3 matrix 
        #arrangement and bet state chosen
        #if bet state exists in matrix, then returns 
        #tuple of amount won and amount bet
        if col[0]==col[1]==col[2]:
            if col[0]=='a':
                print("You win a Mini Lottery!\nPayout: ",amt*(1.5))
                return amt*(1.5),amt
            elif col[0]=='b':
                print("You win a Mini Lottery!\nPayout: ",amt*(1.5))
                return amt*(1.5),amt
            elif col[0]=='c':
                print("You win a Mini Lottery!\nPayout: ",amt*(1.7))
                return amt*(1.7),amt
            elif col[0]=='2':
                print("You win a Lotto!\nPayout: ",amt*(2.0))
                return amt*(2.0),amt
            elif col[0]=='3':
                print("You win a Lotto!\nPayout: ",amt*(2.0))
                return amt*(2.0),amt
            elif col[0]=='$':
                print("You win the Jackpot!\nPayout: ",amt*(6.0))
                return amt*(6.0),amt
        else:
            if col[0]==col[1]=='combo':
                print("You win a Double Combo Reward!\nPayout: ",amt*(3.5))
                return amt*(3.5),amt
            elif col[0]=='combo'!=col[1]:
                print("You win a Combo Reward!\nPayout: ",amt*(2.5))
                return amt*(2.5),amt
            else:
                print("Better luck next time!\nPayout: ",amt-amt)
                return amt-amt,amt
                
    bet=float(input("Enter bet amount from seed money: "))   
    if bet>tot:
        print("Bet exceeded seed amount.")
        return 0, 0
    elif bet<=0:
        print("Bet amount invalid.")
        return 0, 0
    t.sleep(0.6)
    print("\nInitial State:\n")
    col_show(col_shuffle())
    #prints an initial state of 3x3 matrix which does not affect final state
    print("""Bet Payout:
a a a - Mini 1 (1.5)
b b b - Mini 2 (1.5)
c c c - Mini 3 (1.7)
2 2 2 - Lotto 1 (2.0)
3 3 3 - Lotto 2 (2.0)      
$ $ $ - Jackpot (6.0)
combo ? ? - Combo(from left) with anything (2.5)
Double combo - 2 Combos(from left) with anything (3.0)""".center(20))
    t.sleep(1.9)
    #prints all possible bet multipliers which can be won
    print("""\nBet States:
Diagonal from 1,1 to 3,3 - (1)
Diagonal from 3,1 to 1,3 - (2)
Row 1 from 1,1 to 1,3 - (3)
Row 2 from 2,1 to 2,3 - (4)
Row 3 from 3,1 to 3,3 - (5)
Multiple(includes any of previous bets) - (<num>,<num>,<num>,<num>,<num>)""")
    t.sleep(1.9)
    #prints all possible states player can bet on
    bet_state=input("Choose bet state: ")
    t.sleep(0.9)
    #asks player to choose a state to bet on
    print("\nThe slots spin...")
    t.sleep(1.9)
    print("It stops and shows it's final state.\n")
    col_all=col_shuffle()
    col_show(col_all)
    #prints a final state of 3x3 matrix from which bet states are checked
    col_dia1=[col_all[0][0],col_all[1][1],col_all[2][2]]
    col_dia2=[col_all[2][0],col_all[1][1],col_all[0][2]]
    col_row1=[col_all[0][0],col_all[0][1],col_all[0][2]]
    col_row2=[col_all[1][0],col_all[1][1],col_all[1][2]]
    col_row3=[col_all[2][0],col_all[2][1],col_all[2][2]]
    #creates 5 unique lists which represent 
    #either a column or row of the matrix
    dic={1:col_dia1,2:col_dia2,3:col_row1,4:col_row2,5:col_row3}
    #creates dictionary linking bet state 
    #chosen with list associated with it
    if bet_state[0:len(bet_state):2].isdigit():
        num=bet_state[0:len(bet_state):2]
        win_return=[]
        for i in range(len(num)):
            col_b=dic[int(num[i])]
            win_return.append(win_states(col_b,bet/len(num)))
        payout_bet=sum([win_return[i][0] for i in range(len(win_return))])
        return payout_bet,bet
    elif bet_state in ['1','2','3','4','5']:
        return win_states(dic[int(bet_state)],bet)
    else:
        print("Invalid Bet State chosen.")
        return 0,0
    #checks for 'win_states' 


def casino(seed):
    #takes total seed money as argument
    in_buff=seed
    #creates and asigns value of total seed money to a temporary variable 
    print("\nWelcome to the Casino!")
    t.sleep(0.8)    
    print(f"Your seed money is ${seed}")
    t.sleep(0.8)
    print("""\nWhich game would you like to play?
1. Blackjack
2. Roulette
3. Slot Machine
4. Exit Casino""")
    t.sleep(0.9)
    #shows all possible things player can do
    ans=input("Enter choice(<No.>): ")
    t.sleep(0.5)
    #asks player what to do
    if ans=='1':
        t.sleep(0.8)
        print("""\nBlackjack: A card game where dealer
and player try to acquire cards with 
a total face value of 21 and no more.""")
        #prints brief definition of game
        t.sleep(1.1)
        ans2=input("Continue with blackjack?(y/n) ")
        #player can choose to look at definitions of game 
        #and exit or play the selected game
        t.sleep(0.9)
        if ans2=='y' or ans2=='Y':
            print(f"\nSeed Money: ${in_buff}")
            #prints current seed money of player
            result_bet=blackjack(in_buff)
            #assigns tuple returned by game function to result variable
            while True:
                #loops game playing process until player chooses to quit game
                in_buff=in_buff+result_bet[0]-result_bet[1]
                #temp variable is assigned new value based on result variable
                ans3=input("Leave Blackack?(y/n) ")
                t.sleep(0.9)
                #asks if player will exit current game 
                if ans3=='n' or ans3=='N':
                    while True:
                        #creates loop where player plays new game 
                        #with temp variable as seed money
                        print(f"\nSeed Money: ${in_buff}")
                        t.sleep(0.9)
                        #prints temp variable as seed money 
                        result_bet=blackjack(in_buff)
                        #result variable is assigned new value based 
                        #on new game return value 
                        break
                        #exits new game loop with updated variable values
                elif ans3=='y' or ans3=='Y':
                    print(f"\nRemaining Money: ${in_buff}\nExited Blackjack.")
                    #prints remaining money as temp variable
                    break
                    #exits game loop
                else:
                    print("Invalid response. Exiting Blackjack.")
            ans4=input("Leave casino?(y/n) ")
            t.sleep(0.9)
            #asks if player wants to leave casino after exiting game
            if ans4=='y' or ans4=='Y':
                print(f"\nExited casino.\nRemaining Money: ${in_buff}")
                #prints remaining money after exiting game
            elif ans4=='n' or ans4=='N':
                casino(in_buff)
                #creates new casino function with 
                #temp variable as seed money argument
                return     
                #exits original casino function
        elif ans2=='n' or 'N':
            print("\nReturning to main menu")
            casino(in_buff)
            return
        else:
            print("\nInvalid response. Returning to main menu.")
            casino(in_buff)
            return
    elif ans=='2':
        t.sleep(0.8)
        print("""\nRoulette: A gambling game where 
players bet on a ball which is dropped 
on a revolving wheel with numbered 
and coloured compartments.""")
        t.sleep(1.1)
        ans2=input("Continue with roulette?(y/n) ")
        t.sleep(0.9)
        if ans2=='y' or ans2=='Y':
            print(f"\nSeed Money: ${in_buff}")
            result_bet=roulette(in_buff)
            while True:
                in_buff=in_buff+result_bet[0]-result_bet[1]
                ans3=input("Leave Roulette?(y/n) ")
                t.sleep(0.9)
                if ans3=='n' or ans3=='N':
                    while True:
                        print(f"\nSeed Money: ${in_buff}")
                        result_bet=roulette(in_buff)
                        break
                elif ans3=='y' or ans3=='Y':
                    print(f"\nRemaining Money: ${in_buff}")
                    print("Exited Roulette.")
                    break
                else:
                    print("Invalid response. Exiting Roulette.")
            ans4=input("Leave casino?(y/n) ")
            if ans4=='y' or ans4=='Y':
                print(f"\nExited casino.\nSeed Money: ${in_buff}")
            elif ans4=='n' or ans4=='N':
                casino(in_buff)             
            return
        elif ans2=='n' or ans2=='N':
            print("\nReturning to main menu")
            casino(in_buff)
            return
        else:
            print("\nInvalid response. Returning to main menu.")
            casino(in_buff)
            return
    elif ans=='3':
        t.sleep(0.5)
        print("""\nSlot Machine: A gambling machine 
that determines payoff of player's 
bets by final alignment of a set 
of spinning symbols.""")
        t.sleep(1.3)
        ans2=input("Continue with slot machine?(y/n) ")
        t.sleep(0.9)
        if ans2=='y' or ans2=='Y':
            print(f"\nSeed Money: ${in_buff}")
            result_bet=slot_machine(in_buff)
            while True:
                in_buff=in_buff+result_bet[0]-result_bet[1]
                ans3=input("Leave Slot Machine?(y/n) ")
                t.sleep(0.9)
                if ans3=='n' or ans3=='N':
                    while True:
                        print(f"\nSeed Money: ${in_buff}")
                        result_bet=slot_machine(in_buff)
                        break
                elif ans3=='y' or ans3=='Y':
                    print(f"\nRemaining Money: ${in_buff}")
                    print("Exited Slot Machine.")
                    break
                else:
                    print("Invalid response. Exiting Slot Machine.")
            ans4=input("Leave casino?(y/n) ")
            if ans4=='y' or ans4=='Y':
                print(f"\nExited casino.\nSeed Money: ${in_buff}")
            elif ans4=='n' or ans4=='N':
                casino(in_buff)
            return
        elif ans2=='n' or ans2=='N':
            print("\nReturning to main menu")
            casino(in_buff)
            return
        else:
            print("\nInvalid response. Returning to main menu.")
            casino(in_buff)
            return
    elif ans=='4':
        print(f"Exited casino.\nSeed Money: ${in_buff}")
        return
    else:
        print(f"Invalid response. Exiting casino.\nSeed Money: ${in_buff}")
        return


seed=rn.randrange(500,1000)
#creates and assigns a random value b/w 500 and 1000 to a variable

if __name__ == '__main__':
    casino(seed)
    #runs the 'casino' function with seed as argument from current module
    
