
    #!/usr/bin/env python3
#SimonKuba

import random

class Kostka:
    def __init__(self, pocet_sten) 
        self.pocetSten = pocet_sten
    def hod(self,max):
        return random.randint(1,self.pocetSten)

k1 = Kostka(6)
k1.hod()
print(k1.hod())