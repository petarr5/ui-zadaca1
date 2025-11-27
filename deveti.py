matrica=[["5","4","a","1"],["c","3","12","b"],["7","9","0","d"]]
rjecnik={}
i=0
j=0
for r in matrica:
    for s in r:
        if s.isnumeric()!=True:
            rjecnik[(i,j)]=s
        j+=1
    j=0
    i+=1
print(rjecnik)