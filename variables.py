maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print( maasAhmet - (maasAhmet * vergi))

#değişken tanımlama kuralları 

#rakam ile başlayamaz

number1 = 10
print(number1)


number1 = 20
print(number1)

number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı

age = 20 
AGE = 30 

print (age)
print (AGE)

#Türkçe karakter kullanmayalım 

yas = 20

_age = 20

x = 1                #int 
y = 2.3              #float 
name = "esad"        #string
isStudent = True     #bool 

# x, y, name, isStudent = (1, 2.3, "Esad",True)

a = "10" 
b = "20" 
print(a+b)  # => 1020 

firstName = "Esad"

lastName = " Dinç"

print (firstName + lastName)   #Esad Dİnç

"""
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

Müşteri adı
Müşteri soyadı
Müşteri ad+soyadı
Müşteri cinsiyeti
Müşteri tc kimiliği
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı 
"""
musteriAdi = 'ali'
musteriSoyad = 'yılmaz '
musteriAdsoyad = musteriAdi + ' ' + musteriSoyad
musteriCinsiyet = True # erkek 
musteriTcKimlik = '12140642775'
musteriDogumyili = '1989' 
musteriAdresi = 'istabul kadıköy'
musterıYasi = 2022 - musteriDogumyili





"""
2-  Aşağıdaki siparişlerin toplam bilgisini hesaplayınız 

sipariş 1=> 110    TL 
sipariş 2=> 1100.5 TL
sipariş 3=> 356.95 TL 



"""


print( 110 + 110.95 + 356.95)


