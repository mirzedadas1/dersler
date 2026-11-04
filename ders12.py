#class"lar,obyektler(ATRIBUTLAR),__init__()->constructor,get_info() metodlari

'''class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print("Hesabin balansi:", self.balance)
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Yeni balans:", self.balance)
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Yeni balans:", self.balance)
        else:
            print("Balansda kifayet qeder pul yoxdur")
hesab1 = BankAccount("Mirza", 1000)

hesab1.deposit(200)
hesab1.withdraw(2000)'''

#BankAccount adli class yarat
# her hesabda sahibin adi,balansi olsun.
# class da 3 eded metod olsun
# 1 ci metod balans gostermek olsun -> show_balance()
# 2 ci metod pul elave etmek -> deposit()
#3 -cu metod pul cekmek -> withdraw()
# eger balansdan cox pul cekmek istese, "Balansda kifayet qeder pul yoxdur" yazdirsin

'''class Telebe:
    def __init__(self, ad,qrup,soyad):
        self.ad = ad
        self.qrup = qrup
        self.soyad = soyad

    def get_info(self,ad,soyad,qrup):
        print("Telebenin adi:", self.ad)
        print("Telebenin soyadi:", self.soyad)
        print("Telebenin qrupu:", self.qrup)

class MagistraturaTelebesi(Telebe):
    def __init__(self, ad, qrup,soyad,fakulte):
        super().__init__(ad, qrup,soyad)
        self.fakultet = fakulte

    def get_info(self, ad, soyad, qrup,fakulte):
        super().get_info(ad, soyad, qrup)
        print("Telebenin fakulteti:", self.fakulte)'''


'''class Telebe:
    def __init__(self, ad, qrup, soyad, fakulte):
        self.ad = ad
        self.qrup = qrup
        self.soyad = soyad
        self.fakulte = fakulte  


    def get_info(self):
        print("Telebenin adi:", self.ad)
        print("Telebenin soyadi:", self.soyad)
        print("Telebenin qrupu:", self.qrup)
        print("Telebenin fakulteti:", self.fakulte)

telebe1 = Telebe("Mirza", "A123", "Dadaşov", "Riyaziyyat")

telebe2 = Telebe("Nicat", "B456", "Hüseynov", "Biologiya")
telebe1.get_info()'''

'''Mehsul adli bir class yaradin,daxilinde marka,model,il atributlari olsun
get_info() metodu olsun,bu metod mehsulun melumatlarini ekrana cixarsin'''

'''Telebe adli class yaradin, atributlar olaraq ad ,soyad,bal olsun.set_bal adli metod olsun,bu metod telebenin
 balini deyissin.get_bal adli metod olsun,bu metod telebenin balini ekrana cixarsin
'''

class Telebe:
    def __init__(self, ad, soyad, bal):
        self.ad = ad
        self.soyad = soyad
        self.bal = bal

    def set_bal(self, teze_bal):
        self.bal = teze_bal

    def get_bal(self):
        print("Telebenin bali:", self.bal)