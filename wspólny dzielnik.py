x=int(input("podaj liczbę x "))
y=int(input("podaj liczbę y "))

if x>y:
    z=y
else:
    z=x
for a in range(z,0,-1):
    print(a)
    if x%a==0 and y%1==0:
        break


x=5
y=4

if x>y:
    mniejsza = y
else:
    mniejsza = x
for i in range(mniejsza,0,-1):
    print(i)
    if x%i==0 and y%i==0:
        break






