import random
def loto642():
    i=0
    niz=[]
    while i<7:
        broj=random.randint(0,42)
        if broj not in niz:
            niz.append(broj)
            i+=1
    return niz
    

ulaz=[5,20,14,22,35,40]
tocan=[]
sum=0
bounus=[10]
rez=loto642()
bonus_iz=rez.pop()
print(f"Bonus broj je {bonus_iz}")

if bounus==bonus_iz:
    tocan.append(bonus_iz)
for n in ulaz:
    for l in rez:
        if n==l:
            tocan.append(n)
for l in tocan:
    sum+=l
print(f"Izvučeni brojevi su {rez}")
if tocan==[]:
    print("NIste pogidli nit jedna broj")
else:
    print(f"Pogođeni brojevi su {tocan}")
    print(f"Zbroj pođenih brojeva je  {sum}")
    print(f"Najveci podeni broje je {max(tocan)}")
    print(f"Najmanji pođeni broje je  {min(tocan)}")