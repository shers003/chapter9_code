#Blackjack
'''Pusedo:
Deal each player and dealer 2 cards
for each player
 while the player asks for a hit and is not busted
  Deal player another car
if no players still playing
 show dealers two cards
otherwise
 while the dealer must hit and player not busted
  deal the dealer an additional card
 if the dealer is busted
  for each player still playing
   player wins
  otherwise
   for each player still playing
    if the player total greater than dealer
     player wins
    otherwise if the player total is less than dealers
     the plaeyer loses
    otherwise
     player pushes
'''

import game, cards

class BJ_Card(cards.Card):
    ''' A Blackjack card '''
    ACE_VALUE = 1

    @property
    def value(self):
        
        if self.face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
            
        return v

class BJ_Deck(cards.Deck):
    ''' A Blackjack deck '''

    #Overwritting to use BJ_Card
    def populate(self):
        
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                card = BJ_Card(rank,suit)
                self.cards.append(card)

class BJ_Hand(cards.Hand):
    ''' A Blackjack Hand '''

    #Over writting constructor
    def __init__(self, name):
        super(BJ_Hand,self).__init__()
        self.name = name

    def __str__(self):

        rep = self.name + ':\t' + super(BJ_Hand,self).__str__()

        if self.total:
            rep += '(' + str(self.total) + ')' 
        return rep        

    @property
    def total(self):

        #Check if a card is flipped then returns None 
        for card in self.cards:
            if not card.value:
                return None

        #Total up values
        t = 0
        for card in self.cards:
            t += card.value

        #Determine if cards contain an ace
        ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                ace = True

        #if hand contains ace and total low enogh treat ace as 11
        if ace and t <= 11:
            #Plus 10 as already added 1 in BJ_Card.value method
            t += 10

        return t

    #check if busted
    def is_busted(self):
        #returns true or false depending on outcome of condition 
        return self.total > 21

class BJ_Player(BJ_Hand):
    ''' A blackjack player '''
        
    def is_hitting(self):
        res = game.ask_yes_no('\n'+self.name+
                              ' do you want to hit? (y/n): ')
        return res == 'y'

    def bust(self):        
        print(self.name,'busted')
        self.lose()
        
    def lose(self):
        print(self.name,'LOSES')

        
    def win(self):       
        print(self.name,'WINS')

    def push(self):
        print(self.name,'PUSHES')
        
class BJ_Dealer(BJ_Hand):
    ''' A blackjack dealer '''

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name,'busted')

    def flip_first_card(self):
        card = self.cards[0]
        card.flip()

class BJ_Game(object):
    ''' A blackjack game '''    

    def __init__(self, names):
        self.players = []

        for name in names:

            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer('Dealer')

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    
    def __additional_cards(self, player):
        
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
        print(player)
        if player.is_busted():
            player.bust()

    def play(self):
        ''' Game loop '''
        print()

        if len(self.deck.cards) < 21:
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()
        
        ''' Dealing player and dealer two cards '''
        self.deck.deal(self.players+[self.dealer], num_cards = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        ''' Dealing additional cards to player '''
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() #Revel delears first card
       
        if not self.still_playing:
            ''' Since all plaeyers busted show dealers hand '''
            print(self.dealer)
        else:
            ''' Deal additional cards to dealer '''
            #print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    
                    if player.total > self.dealer.total:
                        player.win()
                        
                    elif player.total < self.dealer.total:
                        player.lose()
                        
                    else:
                        player.push()

        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print('\t\tWelcome to blackjack\n\n')

    names = []
    number = None
    
    while not number:
        try:
            number = game.ask_number('How many players are going to play today? ',
                                    low = 1, high = 8)
        except ValueError:
            print('Pls enter a number\n')
            
    for i in range(number):
        name = input('Enter player name: ')
            
        names.append(name)

        
    print()    

    theGame = BJ_Game(names)
    again = None
    while again != 'n':
        theGame.play()
        again = game.ask_yes_no('Do you want to play again (y/n)')
        
    

main()
input('Enter to Exit')    
