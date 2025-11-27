def izracun(na_kru,broj):
    if na_kru==[]:
       return print("Niti jedna točka nije na kružnici")
    else:
        pog=(spremi/broj)*100
        return  print(f"Pogođeno je {pog}% točaka")
def pripada(a,b,r,prvi,drugi,na_kru):
    na_kru=0
    x=float(prvi)
    y=float(drugi)
    if (x-float(a))**2+(y-float(b))**2==r**2:
        na_kru+=1
        print("Unesena točka se nalazi na kružnici")
    else:
        print("Unesena točka se ne nalazi na kružnici")
    return na_kru

a=0 
b=0
r=5
print("Unesite 10 točaka")
i=0
broj=0
na_kru=[]
spremi=0
while i<10:
    unos=input()
    rez=unos.split(',')
    if rez[0]=='0' and rez[1]=='0':
        izracun(spremi,broj)
        break
    broj+=1
    spremi+=pripada(a,b,r,rez[0],rez[1],na_kru)
    