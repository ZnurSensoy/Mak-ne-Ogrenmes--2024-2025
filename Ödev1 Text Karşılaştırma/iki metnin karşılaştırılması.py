str1 = open('m1.txt', 'r').read()
str2 = open('m2.txt', 'r').read()

#Yukardaki kodlarda m1 ve m2 metinlerini str1 ve str2 olarak atıyoruz,okutuyoruz.

str1 = str1.replace(".","")
str1 = str1.replace(",","")
str1 = str1.replace("'","")

str2 = str2.replace(".","")
str2 = str2.replace(",","")
str2 = str2.replace("'","")

#Yukarıdaki kodlarda atadığımız metinlerin içerisindeki nokta,virgül ve üstten tırnak işaretlerini kaldırıyoruz.

durma = ["ve","veya","ile","çünkü","birkaç","böyle","falan","herkes","hiçbiri",
          "gibi","hangi","kim","şu","şey","yada","zira","zaten","yine","neyse",
          "ama","ancak","asla","az","bazı","bazısı","belki","birçok","çok","çoğu",
          "daha","değil","diğer","elbette","hiç","ise","kendi","kime","niye","önce",
         "ötürü","rağmen","şunu","şunlar","tümü","veya","yoksa","zaten","zira"]
for i in durma:
    str1 = str1.replace(i,"")
    str2 = str2.replace(i, "")

#Yukarıdaki kodlarda bir liste oluşturuyoruz.(Bağlaç ve yardımcı kelimeleri içeriyor.)Bu listedeki kelimeler metinden çıkarılıyor döngü ile kelimeler metinlerden temizleniyor.    

l1 = list(str1.split(" "))
print(l1)
print(len(l1))

l2 = list(str2.split(" "))
print(l2)
print(len(l2))

#Yukarıdaki kodlarda iki metin de boşluklarından bölünerek ayrı ayrı kelime olarak ayrılıyor.Bu kelimeler l1 ve l2 listesine atanıyor.Print ile de listedeki kelimeleri yazdırıyoruz.


s1 = set(l1)
print(s1)
print(len(s1))
s2 = set(l2)
print(s2)
print(len(s2))

#Yukarıdaki kodlarda l1 ve l2 listesindeki tekrar eden kelimeleri kaldırıyoruz.(Sadece bir kez bulunuyor.)l1 ve l2 boyutlarını yazdırıyoruz.

st = set.union(s1,s2)
print(st)
print(len(st))

#Yukarıdaki kodlarda 2 metnin kümelerini birleştiriyoruz.Birleştikten sonraki küme boyutunu yazdırıyoruz.

ts = len(s1)+len(s2)
print("İki metin için tekil sözcük sayısı = ", ts)
tss = len(st)
print("Birleşim sonrası tekil sözcük sayısı = ",tss)
fark = ts - tss
print("Fark = ", fark)
benzeme = (fark*100)/tss
print("Benzeme oranı = %",benzeme)

#Yukarıdaki kodlarda 2 metindeki toplam tekil keime sayısı ie birleşim sonrası tekil kelime sayısı karşılaştırırz.2 metinde ortak olan kelimelerin sayısını buluyoruz en son olarak benzeme oranını hesaplıyoruz.
