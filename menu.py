from config import ConfigPL

class Menu():

    def __init__(self):

        self.cfg = ConfigPL("menu.json")
        self.json = self.cfg.dict
        print(self.cfg.dict)
        print(self.json)
        self.pozycje = 1
        self.podmenu = 1
        self.policz()


    def wyswietl(self,menu):
        print(self.json[menu])
        print("ilosc pozycji", self.pozycje)
        print("ilosc podmenu", self.podmenu)

    def policz(self):
        x = len(self.cfg.dict)
        self.pozycje = x
    def policzpodmenu(self, menu):
        x = len(self.json[menu])
        self.podmenu = x

if __name__ == '__main__':
    menu = Menu()
    menu.wyswietl("Ustawienia LED")