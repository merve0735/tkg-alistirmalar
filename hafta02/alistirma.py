# Hafta 2: Python temelleri
#
# Her fonksiyonun içindeki `pass` satırını silip kendi kodunuzu yazın.
# Fonksiyonların adlarını ve parametrelerini DEĞİŞTİRMEYİN; testler bu adlarla çalışır.
# Kendi bilgisayarınızda denemek için:  cd hafta02  ve ardından  python -m pytest -v


# 1. İşaret
# Sayı 0'dan büyükse "pozitif", küçükse "negatif", 0 ise "sıfır" döndürün.
# Örnek: isaret(5) -> "pozitif"
def isaret(sayi):
<<<<<<< HEAD
    if sayi > 0:
        return "pozitif"
    elif sayi < 0:
        return "negatif"
    else:
        return "sıfır"

print(isaret(5))   
print(isaret(-3))  
print(isaret(0))   
=======
    pass

>>>>>>> upstream/main

# 2. Dönem notu
# Vizenin %40'ı ile finalin %60'ını toplayıp döndürün.
# Örnek: donem_notu(50, 70) -> 62.0
def donem_notu(vize, final):
<<<<<<< HEAD
    return vize * 0.4 + final * 0.6

print(donem_notu(50, 70))
#pass hata olüşmasını önleyen anahtar kelime
=======
    pass

>>>>>>> upstream/main

# 3. Harf sayma
# `metin` içinde `harf` karakterinin kaç kez geçtiğini döndürün.
# Büyük/küçük harf ayrımı yapın: "A" ile "a" farklı harflerdir.
# Örnek: harf_say("merhaba", "a") -> 2
def harf_say(metin, harf):
<<<<<<< HEAD
    return metin.count(harf)

print(harf_say("merhaba", "a"))
=======
    pass
>>>>>>> upstream/main


# 4. Faktöriyel
# n! = 1 * 2 * 3 * ... * n değerini bir döngüyle hesaplayın. 0! = 1'dir.
# Örnek: faktoriyel(5) -> 120
def faktoriyel(n):
<<<<<<< HEAD
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))
=======
    pass
>>>>>>> upstream/main


# 5. Geçenler
# Nottan 60 ve üzeri olanları, sıralarını bozmadan yeni bir liste olarak döndürün.
# Örnek: gecenler([70, 45, 90]) -> [70, 90]
def gecenler(notlar):
<<<<<<< HEAD
    return [not_ for not_ in notlar if not_ >= 60]

print(gecenler([70, 45, 90]))
=======
    pass
>>>>>>> upstream/main
