#x=int(input("Podaj wynagrodzenie "))
#y=int(input("Podaj staż pracy "))
#print("Twoje miesięczne wynagrodzenie wynosi " + str(x+(y*250)))


#x=int(input("jaka jest cena laptopa " ))
#y=int(input ("jakie jest cło "))
#print("Do zapłaty masz " + str(round(x+(x*y/100))))

#y=int(input("Ile masz gotówki "))
#b=int(input("kurs bitcoina "))
#l=int(input("kurs litecoina "))

#print("Za " + str(y) + " zł" + " możesz kupić " + str(round(y/b)) + " bitcoiny " + str(y//e) + " etherum " + "lub " + str(y//l) + " litecoinów")



#str1="fullstack"
#a=len(str1)//2
#print(str1[a-1:a+2])

#s1="Fullstack"
#s2="Python"
#a=int(len(s1)/2)
#print(s1[:a]+s2+s1[a:])


#a="America"
#b="Japan"
#print(a[0]+b[0]+a[(int(len(a)/2))] + b[int((len(b)/2))]+ a[-1] + b[-1])

#s="python"
#s1=s[::-1]
#print(s1)

#tel={}
#print(tel)
#tel["ola"] = 1
#print(tel)

#zbior={4,'y',

#a=int(input("podaj liczbę a "))
#b=int(input("podaj liczbę b "))

#print("Twoje liczby to " + str(a) + " i " + str(b))

#print("wynik z dzielenia a i b to " + str(a/b))
#print("Wynik dzielenia całkowitego to "  + str(a//b))


#x=2
#y=3
#if x > 3 or y%2==0:
#    print("Co najmniej jeden z warunków jest spełniony")
#if x <= 3 and y%2!=0:
#    print("żaden warunek nie jest spełniony")
#x=12
#print(x>3 and x<9)

#x=12
#print(not(x>4 and x<9))

#warzywa = ['marchew', 'kalafior','kapusta']
#for warzywo in warzywa:
#    print("warzywo:", warzywo)

#lista=['Jola', "Maciek", 'Konrad', 'Artur', 'Rozalia']
#i=sorted(lista)
#a=0
#for x in i:
 #   if x[-1]=="a":
  #      a+=1
   #     print("kobieta: " + x)
    #else:
     #   print("meżczyzna: " + x)

#print(a)

#
#x=5
#y=4

#if x>y:
 #   z=y
#else:
#    z=x

#for i in range (z,0,-1):
#    print(i)
#    if x%i==0 and y%i==0:
#        break

#a = "Code brainers"
#b = 317

#b,a=a,b
#print(a)
#print(b)

#for i in range(1500,2701):
 #   if i%7==0 and i%5==0:
  #      print (i)

#def a (x):
#    b=0
#    for i in x:
#        b=b+1
#    return b
#print(a("Stół"))


#def lista(x):
#    b=0
#    for i in x:
#        b=b+i
#    return b
#print(lista([1,2,3]))

#def przykład(x):
#    wynik=x[0]
#    for i in x[1:]:
#        wynik=wynik*i
#    return wynik
#print(przykład([2,3]))


#def a(x):
#    b=x[0]
#    for i in x[1:]:
#        if i > b:
#            b=i
#    return b
#print(a([1,2,3,4]))

#def a(x):
#    b = x[0]
#    for i in x:
#        if i<b:
#            b=i
#    return b
#print(a([2,3,4]))

'''
def a(tekst):
    słownik = {}
    for i in tekst:
        listakluczy=słownik.keys()
        if i in listakluczy:
            słownik[i]+=1
        else:
            słownik[i]=1
    return słownik

tekst="google.com"
print(a(tekst))
'''

#def a(x):
#    b=0
#    for i in x:
#        if len(i)>=2 and i[0]==i[-1]:
#            b=b+1
#    return b
#print(a(['abc', 'xyz', 'aba', '1221']))

#Ćwiczenie
#Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
#Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#lista=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#def drugi(b):
#    return b[-1]
#def posortowana(a):
#    return sorted(a,key=drugi)
#print(posortowana(lista))

#Ćwiczenie
#Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha.
# Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
#Przykładowy ciąg : CodeBrainers
#Oczekiwany wynik: Cors

#Przykładowy ciąg : CB
#Oczekiwany wynik: CBCB
#Przykładowy ciąg : C
#Oczekiwany wynik: pusty ciąg

#przykładowyciąg = "CodeBrainers"
#def znaki(x):
#    if len(x)<2:
#        return (" ")
#    else:
#        return((x[0:2]+x[-2:]))
#
#print(znaki(przykładowyciąg))

"""
Ćwiczenie
Napisz program, policzy silnię dla liczby n tj.
n! = 1*2*3*4...*(n-2)*(n-1)*n
Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej siebie do momentu gdy będzie 
liczyła silnie dla 1 lub 0, która wynosi 0.
"""
"""
3!=1*2*3
4!=1*2*3*4
4!=3!*4
n!=(n-1)!*n
"""
"""
def silnia(n):
    if n ==1:
        return n
    else:
        return silnia(n-1)*n
print(silnia(3))
"""
"""
while True:
    x=input("Podaj liczbę x ")
    y=input("podaj liczbę y ")

    try:
        print(int(x)+int(y))

        break
    except ValueError:
        print("Błąd")
"""

"""
try:
    x = input("Podaj liczbę x ")
    y = input("podaj liczbę y ")
    wynik=int(x)/int(y)
except ZeroDivisionError:
    wynik=("Nie dzielimy przez 0")

print(wynik)
"""

"""
try:
    x = input("Podaj liczbę x ")
    y = input("podaj liczbę y ")
    wynik=int(x)/int(y)
    print(wynik)
except:
    pass
"""


