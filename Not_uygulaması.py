

def ortalama_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ad = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3
    if 100 >= ortalama >= 90:
        harf = 'AA'
    elif 89 >= ortalama >= 85:
        harf = 'BA'
    elif 80 >= ortalama >= 84:
        harf = 'BB'
    elif 75 >= ortalama >= 79:
        harf = 'CB'
    elif 70 >= ortalama >= 74:
        harf = 'CC'
    elif 65 >= ortalama >= 69:
        harf = 'DC'
    elif 60 >= ortalama >= 64:
        harf = 'DD'
    elif 50 >= ortalama >= 59:
        harf = 'FD'


    elif ortalama >= 65:
        harf = 'CC'
    else:
        harf = 'FF'
    return ad + ': ' + harf + "\n"
 
def notları_oku():
    with open("notlar.txt", "r", encoding="utf-8") as file:
        for öğrenci in file:
            print(ortalama_hesapla(öğrenci))

def not_gir():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")  
    with open("notlar.txt", "a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')

def notları_kayıt_et():
    with open("notlar.txt", "r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(ortalama_hesapla(i))
        
        with open("sonuçlar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


def not_sil():
    ad = input("öğrenci ad:") 
    soyad = input("öğrenci soyad:")



while True:
    print("Öğrenci notu kayıt programı.")
    print("****************************")
    
    islem = input("1-Notları oku \n2-Not gir \n3-Notları kayıt et \n4-Çıkış \nişlem: ")
    if islem == "1":
        notları_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notları_kayıt_et()
    elif islem == "4":
        break
    
    