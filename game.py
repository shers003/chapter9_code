#Game
#Going to be used as a module in simpleGame.py

class Player(object):
    ''' A player class '''

    def __init__(self,name,score):
        ''' Constroctor '''
        self.name = name
        self.score = score

    def __str__(self):

        rep = self.name + ':\t' + str(self.score)
        return rep

def ask_yes_no(question):
    rep = None
    while rep not in ('y','n'):
        rep = input(question).lower()
    return rep

def ask_number(question,high,low):
    rep = None
    while rep not in range(low,high):
        rep = int(input(question))
    return rep


if __name__ == '__main__':
    print(__name__)
    print('File should only be run as a module')
    input('Enter to exit')
    
