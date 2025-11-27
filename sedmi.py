dnevnik={"ivan":(3,2,4),"marko":(5,5,4),"ana":(2,3,4)}
suma=0
novi={}
novi1={}
broj=[]
imena=[]
for (k,v) in dnevnik.items():
    suma=round(sum(v)/len(v))
    novi[k]=suma
print(novi)
for (k,v) in novi.items():
    if v not in broj:
        broj.append(v)
for i in broj:
    for (k,v) in novi.items():
        if v==i:
            imena.append(k)
    novi1[i]=imena
    imena=[]

print(novi1)
    