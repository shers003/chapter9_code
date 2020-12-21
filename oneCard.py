#War
#player who is dealed highest card wins


import game,cards

class WarPlayer(cards.Hand):
    ''' Represents a player '''

    def __init__(self,name):
        super(WarPlayer,self).__init__()
        self.name = name

    def __str__(self):

        rep = self.name + ':\t' + super(WarPlayer,self).__str__()

        return rep

    @property
    def total(self):

        t = 0
        for card in self.cards:
            t += card.value
        return t
        
class WarCard(cards.Card):

    @property
    def value(self):

        if self.face_up:
            v = WarCard.RANKS.index(self.rank) + 1
        else:
            v = None

        return v

class WarDeck(cards.Deck):

    def populate(self):

        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                card = WarCard(rank,suit)
                self.cards.append(card)

class WarGame(object):

    def __init__(self, names):

        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()

        self.players = []
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)

    def getWinner(self):
        ''' This needs improving '''
        
        totals = []
        highestValue = None
        index = None
        w = []
        
        for i in self.players:
            totals.append(i.total)

        highestValue = max(totals)

        #checking for draw
        for j in self.players:
            if j.total == highestValue:
                w.append(j.name)

        return w
        
    def play(self):
        winners = []
        
        self.deck.deal(self.players)
        for p in self.players:
            print(p)
            
        winners = self.getWinner()
        
        if len(winners) == 1:
            print('The winner is: ',end=' ')
            for player in self.getWinner():
                print(player, end = ' ')
            print()
        else:
            print('The winners are: ',end=' ')
            for player in self.getWinner():
                print(player, end = ' ') 
            print()        




    
def main():
    ''' Main function '''
    print('\t\tWelcome to War cards\n\n')

    num = None
    while not num:
        try:
            num = game.ask_number('How many players do you want to play 2-8: '
                                  ,low = 2, high = 9)
        except ValueError:
            print('Enter a number')        
        
    names = []
    
    for i in range(num):
        name = input('Enter player name: ')
        names.append(name)

    again = None
    while again != 'n':
            theGame = WarGame(names)
            theGame.play()
            again = game.ask_yes_no('Do you want to play again ? (y/n)')

                
        


main()
input('\nEnter to exit')
