#while,for, break, continue,pass

#[  baslangic    :  son   :    addim sayi    ]

# istifadeciden kodu daxil etmesini isteyin ve kod "1234" olana qeder istifadeciye kodu daxil etmesini isteyin.
#  Eger istifadeci dogru kodu daxil ederse "dogru kod daxil etdiniz" yazdirin, 
# eks halda "yanlis kod daxil etdiniz" yazdirin ve istifadeciden yeniden kodu daxil etmesini isteyin.

eded = int(input("eded daxil edin: "))
cem = 0 

while eded != 0:
    cem = cem + eded
    eded = int(input("eded daxil edin: "))
print("Cem:", cem)