#Card module
#For blackjack game

class Card(object):
    ''' A playing card '''

    RANKS = ['A','1','2','3','4','5','6','7','8','9',
             '10','J','Q','K']
    SUITS = ['h','d','s','c']

    def __init__(self,rank,suit,face_up = True):

        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def __str__(self):

        if self.face_up:
            rep = self.rank + self.suit
        else:
            rep = 'XX'

        return rep

    def flip(self):

        self.face_up = not self.face_up


class Hand(object):
    ''' A playing hand '''

    def __init__(self):

        self.cards = []
        

    def __str__(self):

        if self.cards:
            rep = ''
            for i in self.cards:
                rep += str(i)+'\t'
        else:
            rep = '<EMPTY>'

        return rep

    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)
    
    def clear(self):
        self.cards = []

        
class Deck(Hand):
    ''' A playing deck '''

    def populate(self):

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, num_cards = 1):

        for hand in hands:
            for i in range(num_cards):
                if self.cards:
                    card = self.cards[0]
                    self.give(card,hand)
                else:
                    print('No more cards to deal')
            
if __name__ == '__main__':
    print('This is a module')
    input('Enter to exit')
