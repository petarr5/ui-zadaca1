def fil(pec,ulaz):
    kraj={}
    for (n,k) in pec.items():
        if k>ulaz:
            kraj[n]=k
    return kraj
pec={}
pec['Pero Peric']=175
pec['Marko Markic']=180
pec['Jure Juric']=165
pec['Marija Maric']=190
print(pec)
print("Unesi visinu za filtriranje rijecnika")
ulaz=int(input())
izlaz=fil(pec,ulaz)
print(izlaz)

