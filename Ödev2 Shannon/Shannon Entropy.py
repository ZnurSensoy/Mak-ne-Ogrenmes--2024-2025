import math


s = "Zahide Nur Şensoy"


s = s.replace(" ", "")


liste = []
for i in s:
    liste.append(i)

print("Karakter Listesi:", liste)


k = set(liste)
print("Benzersiz Karakterler:", k)


d = {}
for i in k:
    adet = liste.count(i)
    oran = adet / len(liste)
    d.update({i: oran})

print("Frekans Oranları:", d)


shannon = 0
for i in d:
    v = d[i]
    shannon += v * math.log(v, 2)

shannon *= -1
print("Shannon Entropisi:", shannon)


bs = math.ceil(shannon)
print("Bit sayısı =", bs)


dk = list(k)

b = []
for i in range(int(math.pow(2, bs))):
    a = bin(i)[2:]  
    b.append(a)


dk.sort()
print("Sıralı Benzersiz Karakterler:", dk)
print("İkili Kodlar (Başlangıç):", b)

for i in range(len(b)):
    for j in range(bs - len(b[i])):
        b[i] = "0" + b[i]  

print("İkili Kodlar (Doldurulmuş):", b)


coded = ""
for i in liste:
    coded += b[dk.index(i)] + "-"  

print("Kodlanmış Metin:", coded.strip("-")) 
