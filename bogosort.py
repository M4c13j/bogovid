import hashlib
from os import waitpid
from random import shuffle
from threading import Thread
from time import sleep

HISTORY_LENGHT = 50
class Bogo:
    def __init__(self):
        self.lista = []
        self.count = 0
        self.history = []
        self.closest = 0
        self.sorted = False
    
    
    def setup(self,seq):
        ''' Setup method for the class
        '''
        if type( seq ) is list:
            self.lista = seq
            self.closest = 0
    
    def historyAdd(self,seqs):
        #print( str(len(self.history))+ str(seqs) + str(self.history) )
        self.history.insert(0,seqs)
        if len(self.history) > HISTORY_LENGHT+1:
            self.history.pop()
    
    def ifSorted(self):
        for i in range(len(self.lista)):
            if (i+1) != self.lista[i]:
                return False
        return True
    def sort(self):
        '''
        One step of bogosort

        Randomly shuffles lista , checks the longest common prefix with
        '''
        shuffle( self.lista )
        sned = self.lista.copy()
        self.historyAdd( sned )
        self.count += 1
        
        correct = 0
        while correct < len(self.lista) and self.lista[ correct ] == correct + 1:
            correct += 1
        
        if self.ifSorted():
            self.sorted = True
            return True

        self.closest = max( self.closest , correct )
        return False

    def run(self):
        if not self.sorted:
            self.sort()
        #sleep( 1 )
        print( self.lista )
        


        



# class ProcessHandle:
#     def __init__(self,seq):
#         self.bogo = Bogo()
#         self.bogo.setup( seq )

#         process =  threading.Thread( target=self.run )
#         process.daemon = True
#         process.start()

#     def run(self):
#         if self.bogo.sort():
            


if __name__ == "__main__":
    bogo = Bogo()
    bogo.setup( [1,2,5,4,3] )
    bogo.sort()
    print( bogo.lista )
    bogo.sort()
    print( bogo.lista )
    bogo.sort()
    print( bogo.lista )