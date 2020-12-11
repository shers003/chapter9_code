#Playing cards
#Demonstrates combining objects

class Card(object):
    ''' A playing card '''
    RANKS = ['A','1','2','3','4','5','6','7',
             '8','9','10','J','Q','K']

    SUITS = ['c','d','h','s']

    #Me playing around is pontless does not work
    #Not to sure why tho
    @property
    def ranks(s):
        ranks = ''
        for i in Card.RANKS:
            ranks += str(i)+' '
        
        return ranks
    
    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit

    def __str__(self):

        rep = self.rank + self.suit

        return rep

class Hand(object):

    def __init__(self):

        self.cards = []

    def __str__(self):

        if self.cards:
            rep = ''

            for card in self.cards:
                rep += str(card)+' '
        else:
            rep = '<EMPTY>'

        return rep
                
    def add(self,card):

        self.cards.append(card)

    def give(self,card,otherHand):

        self.cards.remove(card)
        otherHand.add(card)

    def clear(self):

        self.cards = []

#This class will inherit all of Hand class methods
#plus more
#Hand is passed as a parmaeter
class Deck(Hand):
    ''' Inherits all of Hand class methods
        including __init__ '''

    def populate(self):

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):

        import random
        random.shuffle(self.cards)

    def deal(self,hands,num_cards = 1):
        ''' my own code if error refer to pg259'''

        for hand in hands:
            for c in range(0,num_cards):
                  if self.cards:
                      card = self.cards[-1]
                      self.give(card,hand)
                  else:
                      print('No more cards to deal')
                
        

def main():
    print('\t\tWelcome to the card game\n\n')

    card1 = Card('A','c')
    print('First card object: ')
    print(card1)

    card2 = Card('1','c')
    card3 = Card('2','c')
    card4 = Card('3','c')
    card5 = Card('4','c')
    card6 = Card('5','c')

    print('The rest of the cards: ')
    print(card2)
    print(card3)
    print(card4)
    print(card5)
    print(card6)

    print('This is my hand')
    my_hand = Hand()
    print(my_hand)

    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
    my_hand.add(card6)

    print('This is my hand now')
    print(my_hand)

    print('This is your hand')
    your_hand = Hand()
    print(your_hand)

    my_hand.give(card1,your_hand)
    my_hand.give(card2,your_hand)
    my_hand.give(card3,your_hand)

    print('This is your hand now')
    print(your_hand)
    print('This is my hand now')
    print(my_hand)

    print('This is hand safter I clear ')
    your_hand.clear()
    my_hand.clear()
    print(your_hand)
    print(my_hand)

    print('\n\nCreated a new deck')
    d = Deck()
    print('Deck:')
    print(d)

    print('\npopulated deck:')
    d.populate()
    print(d)

    print('\nshuffled deck:')
    d.shuffle()
    print(d)

    print('\nDealing to two hands 20 cards')
    hands = [my_hand,your_hand]
    d.deal(hands,20)
    print('my hand:')
    print(my_hand)
    print('your hand:')
    print(your_hand)
    print('Deck:')
    print(d)

    print('\nClearing deck then hands:')
    d.clear()
    my_hand.clear()
    your_hand.clear()
    print(d)
    print(my_hand)
    print(your_hand)
    

main()

input('Press enter to exit')
