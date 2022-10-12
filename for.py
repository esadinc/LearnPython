from function import isim_fonksiyonu
liste = ['esat',"rifat",12,24]

for value in liste:
    if type(value) is int:
        sd=isim_fonksiyonu(value)
        print(sd)