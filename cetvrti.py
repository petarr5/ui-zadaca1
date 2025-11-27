import random
niz=random.sample(range(0,1000),3)
print(niz)
i=0
broji=0
pec={}
while i<10:
    for n in niz:
        broj=int(n)
        while broj >0:
            pom=broj%10
            if pom==i:
                broji+=1
                pec[i]=broji
            broj=int(broj/10)
    broji=0
    i+=1
print(pec)