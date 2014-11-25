'''
Created on 23 lis 2014

@author: Ewcia
'''
from math import sqrt 

class zespolona:

    def __init__(self, r, u):
        self.r = r
        self.u = u
    def get_r(self):
        return self.__r
    def set_r(self,r):
        self.__r=r
    def get_u(self):
        return self.__u
    def set_u(self,u):
        self.__u=u
    def dodaj(self, z2):
        print "suma : " + str(self.r+z2.r)+"+" + str(self.u+z2.u)+'i'
    def odejmij(self, z2):
        print "roznica : " + str(self.r-z2.r) + str(self.u-z2.u)+'i'
    def modul(self):
        print "modul : "+ str(sqrt((self.u)**2+(self.r)**2))
    def drukuj(self):
        print str(self.r)+ "+" + str(self.u)+"i"

z1 = zespolona(1,2) 
z2 = zespolona(3,4)
print "liczba 1 : " 
z1.drukuj()
print "liczba 2 :" 
z2.drukuj()
zespolona.dodaj(z1, z2)
zespolona.odejmij(z1, z2)
zespolona.modul(z1)
