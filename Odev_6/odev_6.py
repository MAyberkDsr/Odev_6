import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

noktaSayisi = 1000

xKoordinatlari = np.random.randint(0,1001,noktaSayisi) # Rastgele x koordinatları üretildi
yKoordinatlari = np.random.randint(0,1001,noktaSayisi) # Rastgele y koordinatları üretildi

df = pd.DataFrame({"x" : xKoordinatlari, "y" : yKoordinatlari}) # Koordinatlar DataFrame yapıldı

df.to_excel("koordinatlar.xlsx",index=False) # Koordinatlar excel dosyasına kaydedildi

df = pd.read_excel("koordinatlar.xlsx") # Excel dosyasından koordinatlar okundu

print(df)

izgaraBoyutu = 200

plt.figure(figsize=(10, 10)) # Grafik oluşturuldu

renkler = ["red","yellow","blue","green","orange","purple","pink","brown","black","gray"] # Renkler atandı

renkIndex = 0

for i in range(0,1000,izgaraBoyutu): # x eksenindeki ızgaraların başlangıç koordinatları i
    renkIndex = (renkIndex +1) % len(renkler) # Index arttırıldı
    for j in range(0,1000,izgaraBoyutu): # y eksenindeki ızgaraların başlangıç koordinatları j
        izgaraAraligi = (xKoordinatlari >= i) & (xKoordinatlari < i+izgaraBoyutu) & (yKoordinatlari >= j) & (yKoordinatlari < j+izgaraBoyutu)  
        renkIndex = (renkIndex +1) % len(renkler) # Index arttırıldı
        renk = renkler[renkIndex]

        plt.scatter(xKoordinatlari[izgaraAraligi], yKoordinatlari[izgaraAraligi], s=10, c=renk)




plt.title('Rastgele Koordinatlar') # Başlık bilgisi eklendi
plt.xlabel('X Koordinatı') # X ekseni bilgisi eklendi
plt.ylabel('Y Koordinatı') # Y ekseni bilgisi eklendi
plt.grid(True) # Izgara çizgileri eklendi
plt.savefig('koordinatlar_grafik.jpg') # Grafik dosyaya kaydedildi
plt.show() # Grafik gösterildi