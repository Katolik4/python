from config import ConfigPL


class Menu():

    def __init__(self):

        self.cfg = ConfigPL("menu.json")
        self.data = self.cfg.dict
        self.pozycje = 1
        self.podmenu = 1
        self.policz()




    def wyswietltyt(self,menu):
        print(self.data[menu])
        print("ilosc pozycji", self.pozycje)
        print("ilosc podmenu", self.podmenu)
        return (self.data[menu])


    def policz(self):
        x = len(self.cfg.dict)
        self.pozycje = x

    def policzpodmenu(self, menu):
        x = len(self.data[menu])
        self.podmenu = x

    def oledprint(self, dane):
        print(dane)

    def test(self):

        self.oledprint(self.oledtyt())

    def oledtyt(self):
        for tytul in self.data:
            self.oledprint(tytul)

    def oledmenu(self, tyt):
        for poz in self.data[tyt]:
            self.oledprint(poz)



if __name__ == '__main__':
    menu = Menu()
    #menu.wyswietl("Ustawienia LED")
    menu.test()
    #menu.oledmenu("Minutnik")
