from personnage import Personnage
import random




class Combat:
    def __init__ (self, personnage1:Personnage, personnage2: Personnage):
        self.p1 = personnage1
        self.p2 = personnage2

    def demarrer(self):
        self.p1.load_stuff()
        self.p2.load_stuff()
        while not self.p1.vie <= 0 and not self.p2.vie <= 0:
            if self.p1.vie < 50:
                if random.randint(1,2 ) == 1:
                    print(self.p1.soins())
                    continue

            if self.p2.vie < 50:
                if random.randint(1,2 ) == 1:
                    print(self.p2.soins())
                    continue
                
            if random.randint(1,3 ) == 1:
                print(self.p1.crier())
                continue
            if random.randint(1,3 ) == 1:
                print(self.p2.crier())
                continue

            print(self.p1.attaquer(self.p2))
            print(self.p2.attaquer(self.p1))
            