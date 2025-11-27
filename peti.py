pocetak=[5,7]
print("Unesi smjer kretanja robota u obliku SJIZ")
unos=input()
novi=unos.upper()
for l in novi:
    if l=="S":
        pocetak[1]+=3
    if l=="J":
        pocetak[1]+=-1
    if l=="I":
        pocetak[0]+=1
    if l=="Z":
        pocetak[0]+=-1
print(f"Konočna pozicija robota{pocetak}")