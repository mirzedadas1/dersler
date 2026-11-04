# parent class,child class, and inheritance(miras almaq),method overriding,super() hem goturur hemde muraciet edir...



class Masin:
    def __init__(self,markasi,rengi):
        self.markasi=markasi
        self.rengi=rengi

    def siqnal(self):
        print("Bip Bip") 

class IdmanMasini(Masin):
    def __init__(self,markasi,rengi,modeli):
        super().__init__(markasi,rengi)
        self.modeli=modeli

    def siqnal(self): 
        print("bum bum")

masin1=Masin("Mercedes","Qara")
idman_masin1=IdmanMasini("BMW","Ag","M5")

idman_masin1.siqnal()






'''Heyvan adli class olsun.
icinde ses_ver() metodu olsun.
ve  printe heyvan ses verir yazsin,
it adli class olsun,heyvan classindan miras alsin ve 
ses_ver() metodunu override etsin ve printe "hav hav" yazsin.
pişik adli class olsun,heyvan classindan miras alsin ve
 ses_ver() metodunu override etsin ve printe "miyav miyav" yazsin.
    
'''
'''class Heyvan:
    def ses_ver(self):
        print("Heyvan ses verir")

class It(Heyvan):
    def ses_ver(self):
        print("Hav Hav")
class Pisik(Heyvan):
    def ses_ver(self):
        print("Miyav Miyav")
    
heyvan1 = Heyvan()
it1 = It()
pisik1 = Pisik()

it1.ses_ver()
heyvan1.ses_ver()
pisik1.ses_ver()'''












    

