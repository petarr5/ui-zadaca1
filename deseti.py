niz=["aba","abc","cc","ijiki"]
brojac=0
for i in niz:
    pom=i[0]
    if pom in i[1:] and len(i)>=3:
        brojac+=1
print(brojac)