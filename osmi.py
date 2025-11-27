print("Unesite string")
unos=["dobar","dan"]
rjecnik={}
novi=[]
novi1=[]

for i in unos:
    rec=i
    for n in rec:
        if n not in novi:
            novi.append(n)
for l in novi:
    for i in unos:
        if l in i:
            novi1.append(i)
    rjecnik[l]=novi1
    novi1=[]
print(rjecnik)
    