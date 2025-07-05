from ast import arg


def usalma(number):

    def inner(power):
        return number ** power
    
    return inner



def yetki_sorgula(page):

    def inner(role):
        if role == "admin":
            return f'{role} rolü {page} sayfasına ulaşabilir'
        else:
            return f'{role} rolü {page} sayfasına ulaşamaz'
    return inner

yetki = yetki_sorgula("product edit")
print(yetki("admin"))
        


def hesap_makinesi(seçenek):
    def toplama(*args):
        toplam = 0
        for number in args:
            toplam += number
        return toplam
    def çikarma(*args):
        çikarma = 0
        for number in args:
            çikarma -= number
        return çikarma
    def çarpma(*args):
        çarpım = 1
        for number in args:
            çarpım *= number
        return çarpım
    def bölme(*args):
        bölüm = 0
        for number in args:
            x = args[number] // arg[number + 1]
    
    if seçenek == "toplama":
        return toplama
    elif seçenek == "çıkarma":
        return çikarma
    elif seçenek == "çarpma":
        return çarpma
    elif seçenek == "bölme":
        return bölme
    

toplama = hesap_makinesi("toplama")
print(toplama(5,1,2))