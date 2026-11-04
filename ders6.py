def sifre_yoxla():
    sifre = input("Şifrə daxil edin: ")

    while True:
        if sifre == "1234":
            print("Şifrə doğru! Giriş uğurludur.")
            break
        else:
            print("Yanlış şifrə! Yenidən cəhd edin.")
            sifre = input("Şifrə daxil edin: ")

sifre_yoxla()