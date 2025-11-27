
import random

ulaz=[]
naj=[]
vec_bio=[]
i=0
n=0
pon=0
while i < 100:
    broj=random.randint(0,30)
    ulaz.append(broj)
    i+=1
while n<=30:
    for m in ulaz:
        if m==n:    
            pon+=1

    if pon>=3:  
            naj.append(n)         
    n+=1
    pon=0
print("Ispis pocetene liste:")
print(ulaz)
print("Ispis konacne liste")
print(naj)


