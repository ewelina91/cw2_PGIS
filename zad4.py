class zwierzeta:
    def __init__(self, gromada, rodzina):
        self.gromada=gromada
        self.rodzina=rodzina
    def get_gromada(self):
        return self.__gromada
    def set_imie(self, gromada):
        self.__gromada=gromada
    def get_rodzina(self):
        return self.__rodzina
    def set_wiek(self, rodzina):
        self.__rodzina=rodzina
    def jestem(self):
        print "Jestem kangurem!"
    def pochodzenie(self):
        print "Naleze do gromady "+self.gromada+ " i rodziny "+self.rodzina

class KangurSzary(zwierzeta):
    def __init__(self,gromada,rodzina,hop):
        zwierzeta.__init__(self, gromada, rodzina)
        self.hop=hop
    def get_hop(self):
        return self.__hop
    def set_hop(self, hop):
        self.__hop=hop
    def skacz(self):
        if (self.hop==False):
            print "Nie umiem jeszcze skakac."
        else:
            print "Skacze bardzo wysoko...HOP HOP!"
    def wyglad(self):
        print "Mam dlugi ogon i odstajace uszy."

class MalyKangur(zwierzeta):
    def __init__(self, gromada, rodzina, jedzenie, torba):
        zwierzeta.__init__(self, gromada, rodzina)
        self.jedzenie=jedzenie
        self.torba=torba
    def get_jedzenie(self):
        return self.__jedzenie
    def set_jedzenie(self, jedzenie):
        self.__jedzenie=jedzenie
    def get_torba(self):
        return self.__torba
    def set_torba(self, torba):
        self.__torba=torba    
    def obiad(self):
        print "Jestem roslinozerca. Jem " + self.jedzenie
    def mama(self):
        print "Kiedy chce wskakuje mamie do "+self.torba
        
class wystepowanie(KangurSzary,MalyKangur):
    def __init__(self, gromada, rodzina, hop, jedzenie, torba, kraj, wzrost):
        KangurSzary.__init__(self, gromada, rodzina, hop)
        MalyKangur.__init__(self, gromada, rodzina, jedzenie, torba)
        self.kraj=kraj
        self.wzrost=wzrost
    def get_kraj(self):
        return self.__kraj
    def set_kraj(self, kraj):
        self.__kraj=kraj
    def get_wzrost(self):
        return self.__wzrost
    def set_wzrost(self, wzrost):
        self.__wzrost=wzrost
    def zasieg(self):
        if (self.kraj==True):
            print "Mieszkam w Tasmanii."
        else:
            print "Mieszkam w Australii."
    def siedlisko(self):
        print "Jak dorosne bede mierzyl az "+ str(self.wzrost)+ " metry!"
        
Johny=wystepowanie("ssaki","torbacze.",True, "liscie i pedy traw.","torby.",False,2)
Johny.jestem() 
Johny.pochodzenie()
Johny.zasieg()
Johny.obiad()
Johny.wyglad()
Johny.mama()
Johny.siedlisko()
Johny.skacz()