# Video Poker program
# Christine Mounce
# OOP- Griffin


class card(object):
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        
    def __cmp__(self,rhs):
        return self.rank < rhs.rank 
        
    def __lt__(self,rhs):
        return self.__cmp__(rhs)
        
    def __str__(self):
        return "(%s,%s)" % (self.rank,self.suit)
        
"""
This class will run the game.
    -print menus
    -prompts user
    -keep track of ( and display) game score
    -etc
"""        
class game_driver(object):
    def __init__(self):
        self.gamescore = 0;
        
    def printMenu(self):
        pass
        """
        Print menu:
        [1] Start Game
        [2] Redeal Hand
        [3] Quit
        """
        
"""
 This is the video_poker class. It does both the poker stuff and the graphics
    -dealing cards
    -determining winning hands
    -getting images for cards
 """       
class video_poker(object):
    def __init__(self):
        self.hand = []
        self.suitDict = {}
        self.rankDict = {}
    
    def dealhand(self):   
        self.hand.append(card(1,11)) #I really need to make this do it randomly.
        self.hand.append(card(1,11)) #ugh 
        self.hand.append(card(1,12)) #maybe i'm making this harder than it needs to be
        self.hand.append(card(1,13))
        self.hand.append(card(1,14))
        #time to build the suitDict and rankDict for the hand
        #doing this as soon as I build the hand and rebuild the hand
        for card in hand:
            if not card.rank in rankDict:
                rankDict[card.rank] = 1
        else:
            rankDict[card.rank] += 1 
        
        if not card.suit in suitDict:
            suitDict[card.suit] = 1
        else:
            suitDict[card.suit] += 1 
        
    #returns boolean value
    def straight(hand):
        return (hand[4].rank - hand[0].rank) == 4 and len(hand) == 5 
     
     #returns boolean value   
    def flush(suitDict):
        return len(suitDict.keys()) == 1
    
    #returns boolean value    
    def straightFlush(hand,suitDict):
        return flush(suitDict) and straight(hand)
    
    #returns boolean value    
    def royalFlush(hand,suitDict):
        return straightFlush(hand,suitDict) and hand[4].rank == 14

        




        



"""
Let's take a walk through my logic. Try to keep up. 
 
step one: start game. either print a opening message, or don't.(haven't decided yet) 
           initialize Game stuff.
           Deal first hand. (also display the hand)
           
step two:  Display menu (redeal or all is good or quit?)

step three:delete cards chosen and deal in new cards (if redealling only)
           
step four: figure out any winnning combos in hand & calculate points 

step five: display points and ask if they want to continue playing
""" 
mygame = video_poker()
mygame.dealhand()
print(suitDict)
print(rankDict)
 
 
       
"""
#print(hand)
print(suitDict)
print(rankDict)

print(len(rankDict.keys()))


print(straight(hand))
print(flush(suitDict))
print(straightFlush(hand,suitDict))
print(royalFlush(hand,suitDict))
#option = raw_input("Which option do you choose? Type a number: ")
#if option == 1 
    #call deal hand. and start game
#elif option == 2
    #ask which cards to delete. delete those cards from hand and get new
#elif option == 3
    #display quit message and end game/program
#else
    #print not a valid option try again you dumb dumb
    
 """   