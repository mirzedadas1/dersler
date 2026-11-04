# try - except - finally,Errorlar,else,raise



balans = 1000

try:
    mebleg = float(input("Kocurulecek Meblegi daxil edin: "))
    if mebleg > balans:
        raise ValueError("Balansdan artıq məbləğ daxil etdiniz!")
    if mebleg < 0:
        raise ValueError("Mənfi məbləğ daxil etdiniz!")

except ValueError:
    print("Xəta baş verdi! Zəhmət olmasa düzgün məbləğ daxil edin.")
else:
    balans -= mebleg
    print("Əməliyyat uğurlu oldu! Yeni balans:", balans)
finally:
    print("Əməliyyat tamamlandı.")