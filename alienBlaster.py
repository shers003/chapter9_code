#Alien blaster program
#Shows of how to classes interact with one another

class Human(object):
    ''' A human with a first for alien blood'''

    def __init__(self,name):
        self.__name = name
        
    def pew(self,opp):
        print(self.__name,'pews',opp.name,'(the alien)')
        opp.die()

class Alien(object):

    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def die(self):
        print('Why has this happened to me? '+\
              'I done nothing wrong??\n')

print('\t\tSee the unfortunate death of an alien\n\n')

bob = Human('Bob')
jim = Alien('Jim')

bob.pew(jim)
input('Enter to exit')
