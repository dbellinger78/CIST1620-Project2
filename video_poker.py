import random


DECK_SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
DECK_VALUES = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
POINT_VALUES = [14 , 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

class Card:
    '''
    The card class defines the attributes of the individual cards that comprise the deck used in the game.  
    Each card is assigned one of four suits, one of 13 deck values that correspond with the card values seen in physical card decks, 
    and a numeric point value that corresponds to the cards value.
    '''
    def __init__(self, suit, value, point, hold=False,):        
        self.suit = suit
        self.value = value
        self.point = point
        self.hold = hold
        self.image = f'cards/{self.value}{self.suit}.png'

    def __str__(self):
        return f'{self.value}{self.suit}'

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getPoint(self):
        return self.point

    def getHold(self):
        return self.hold

    def clearHold(self):
        self.hold = False    

    def setHold(self):
        if self.getHold() == False:
            self.hold = True
        elif self.getHold() == True:
            self.hold = False

        
def newDeck():
    '''
    The method uses the Card card class to create a list of 52 card objects that is used to represent the deck of cards in the game.
    '''
    newDeck = []
    i = 0
    for suit in DECK_SUITS:
        z = 0
        for value in DECK_VALUES:
            card = Card(DECK_SUITS[i], DECK_VALUES[z], POINT_VALUES[z])
            newDeck.append(card)
            z = z + 1
        i = i + 1

    return newDeck


def shuffle(list):
    '''
    This method is used to sort the object in the list object into a random order to simulate 
    the shuffling of the deck of cards before they are dealt out to the user.
    '''
    shuffleDeck = list

    i = 0
    while i < len(shuffleDeck):
        switch = random.randint(0, len(shuffleDeck)-1)
        card1 = shuffleDeck[i]        
        card2 = shuffleDeck[switch]
        shuffleDeck[i] = card2
        shuffleDeck[switch] = card1
        i = i + 1

    return shuffleDeck    
        

def deal(list):
    '''
    This method takes the first 5 card object in the list and assigns them to the user at the start of each hand of the game.
    '''
    deck = list

    hand = [deck[0], deck[1], deck[2], deck[3], deck[4]]

    return hand   


def determineHand(hand, bet):
    '''
    This method determines the result of the hand held by the user at the end of each hand using its subfunctions. 
    A message declaring the outcome of the hand is generated and a payout is calculated for 
    winning hands based on the amount of the players bet and is added to a player's bankroll.
    '''
    bet = bet
    hand = hand
    flush = False
    straight = False
    ace = False
    fourKind = False
    threeKind = False
    house = False
    flushCheck = []
    straightCheck = []
    houseCheck = []    
    i = 0
    while i < 5:
        check1 = hand[i].getSuit()
        check2 = hand[i].getPoint()
        flushCheck.append(check1)
        straightCheck.append(check2)
        houseCheck.append(check2)
        i = i + 1

    flushCheck.sort()
    '''
    The players hand is sorted and checked to determine if the hand is a flush where all 5 cards are the same suit.
    '''
    if flushCheck[0] == flushCheck[1]:
        if flushCheck[1] == flushCheck[2]:
            if flushCheck[2] == flushCheck[3]:
                if flushCheck[3] == flushCheck[4]:                    
                    flush = True    

    straightCheck.sort(reverse=True)
    '''
    The players hand is sorted and checked to see if the hand is a straight where all five cards are in sequential order.
    '''
    if straightCheck[0] == 14:
        '''
        The hand is checked to determine if it contains an Ace to account for this cards unique ability to be the highest card 
        or the lowest card within a straight.
        '''    
        ace = True
    '''
    Cards are checked to determine if they are in sequential order. 
    Will find alll straights except for those where an Ace is the low card.
    '''    
    if straightCheck[0] == straightCheck[1] + 1:
        if straightCheck[0] == straightCheck[2] + 2:
            if straightCheck[0] == straightCheck[3] + 3:
                if straightCheck[0] == straightCheck[4] + 4:
                    straight = True
    '''
    Hands that contain an ace are checked to determine if a straight with the Ace as the low card is present.
    '''            
    if straightCheck[0] == 14 and straightCheck[1] == 5:
        if straightCheck[2] == 4: 
            if straightCheck[3] == 3:
                if straightCheck[4] == 2:
                    straight = True  
               
    '''
    Hands not determined to contain a flush or a straight are checked to see if they contain a Full House
    where the hand contains three cards of the same value and the remaining two cards are the same value.
    Hands containing a Four of a Kind where four cards are the same value are also identified in this method.
    Hands containing a Three of a Kind where three cards are the same value but is not a Full House are also identified.
    '''           

    if flush == False and straight == False:    
        houseCheck.sort(reverse=True)
        if houseCheck[0] == houseCheck[1] and houseCheck[1] == houseCheck[2]:
            if houseCheck[2] == houseCheck[3]:
                fourKind = True
            else:
                if houseCheck[3] == houseCheck[4]:
                    house = True
                else: 
                    threeKind = True    
        elif houseCheck[4] == houseCheck[3] and houseCheck[3] == houseCheck[2]: 
            if houseCheck[2] == houseCheck[1]:
                fourKind = True
            else:
                if houseCheck[1] == houseCheck[0]:
                    house = True
                else:
                    threeKind = True
        else: 
            if houseCheck[1] == houseCheck[2] and houseCheck[2] == houseCheck[3]:
                threeKind = True    

    '''
    Hands that were identifed as being both a flush and a straight by previous checks and were 
    also identified as containing an Ace are checked to detemine if they hand is a Royal Flush 
    where the hand contains the Ace, King, Queen, Jack, and the 10 cards all of the same suit.
    '''

    if flush == True and straight == True:
        if ace == True:
            message = 'WINNER: Royal Flush!'
            if bet == 5:
                payout = 4000
            else:
                payout = bet * 250    
            return [message, payout]
        else:
            message = 'WINNER: Straight Flush!'
            payout = bet * 50
            return [message, payout]

    elif fourKind == True:
        message = 'WINNER: Four of a Kind!'
        payout = bet * 25
        return [message, payout]

    elif house == True:
        message = 'WINNER: Full House!'
        payout = bet * 9
        return [message, payout]

    elif flush == True:
        message = 'WINNER: Flush!'
        payout = bet * 6
        return [message, payout]

    elif straight == True:
        message = 'WINNER: Straight!'
        payout = bet * 4
        return [message, payout]

    elif threeKind == True:
        message ='WINNER: Three of a Kind!'
        payout = bet * 3
        return [message, payout]

    else:
        '''
        Hands where a Flush, Straight, Four of a Kind, or a Three of a Kind are not identified are checked
        to determine if one or more pairs of two cards of the same value are present in the hand.
        '''
        i = 0
        pairs = 0
        topPair = 0
        while i < 4:
            if houseCheck[i] == houseCheck[i + 1]:
                pairs = pairs + 1
                topPair = houseCheck[i]
                i = i + 1
            else:
                i = i + 1
        
        if pairs == 2:
            '''
            Hands that contain only two pairs of cards with matching values are identified.
            '''
            message = 'WINNER: Two Pairs!'
            payout = bet * 2
            return [message, payout]

            
        elif topPair > 10:
            '''
            Hands that contain only one pair with a value of Jack are better are identified.
            '''
            message = 'WINNER: Jacks or Better!'
            payout = bet
            return [message, payout]
        
        else:
            '''
            Losing hands are identified.
            '''
            if pairs == 1:
                message = 'You Lost! You need Jacks or better to win.'
                payout = 0
                return [message, payout]
            else:
                message = 'You Lost! Busted Hand!'
                payout = 0
                return [message, payout]


