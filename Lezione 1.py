# Programmazione con Python in 90 minuti

# Lezione 4
# <- si usa per inserire degli appunti al codice


print("stringa ")  # per stampare, si usano "" per le stringhe
print(5)  # per stampare numero non sono necessarie "", sia interi che con la virgola
print(5 + 3)  # stampa la somma
print(10 / 3)  # stampa la divisione
print(10 // 3)  # stampa solo l'intero della divisione
print(10 % 3)  # stampa il resto della divisone
# potenza
print(10 ** 2)
# per unire le stringhe
print("5" + "2")
print("ciao" + " " + "python")
print("ciao", "python")
input ("Come ti chiami ?")
name = input ("come ti chiami?")
print(name)
grandpa_age= input("Quanti anni ha tuo nonno?")
var="ciao"
type(var)
print(var)
#per convertire il numero in una stringa
var=5
var=str(5)
type(var)
print(var)

#per convertire la stringa in un numero
var="5"
var=str(5)
type(var)
print(var)

#Convertire una stringa ,che non è un numero, in numero
var="gatto"
var=int(var)
#mi da un errore in cui dice il tipo di errore

num=input("Inserisci un numero: ")
type(num) #di base da una stringa
num=int(num)
print("il numero che hai inserito è ",num)
#se invece inserisco una strina
num=input("Inserisci un numero: ")
type(num) #di base da una stringa
num=str(num)
print("il numero che hai inserito è ",num)
#risulta un errore
#uso try except

try:
    type(num)
    num = int(num)
    print("il numero che hai inserito è ", num)
except ValueError:
    print("il dato che hai inserito non è un numero")
    #cioe fa inserire il numero e se è giusto lo stampa altrimenti ti dice che ciò che hai inserito non è un numero

#FORMATTAZIONE
#unire stringhe con numeri
cat="Elon"
age=2
print("Il mio gatto si chiama "+cat+" ed ha" +age+ "anni")
#mi darebbe un errore quindi posso fare
print("Il mio gatto si chiama "+cat+" ed ha" +str(age)+ "anni")
#O meglio

#tramite la formattazione
print("Il mio gatto si chiama %s ed ha %d anni"%(cat,age))
#%s per la stringa
#%f float se scrivo %.2f significa che prendo solo 2 numeri dopo la virgola

#formattazione (new school)
print("Il mio gatto si chiama {cat}, ha {age} anni e pesa {weigh} kg".format(cat=cat, age=age,weigh=weigh))
#Formattazione Python 3.6
print(f"Il mio gatto si chiama {cat}, ha {age} anni e pesa {weigh} kg")

#Liste e Tuple
#liste

my_list=[10,5,8,3,11,2]
type(my_list)
len(my_list) #lunghezza lista

#indexing
my_list[0]

#slicing
my_list[0:3] #stampa i primi 3 elementi
my_list[::-1] #inverte la lista


#modifica
my_list[0]=0 #sostituisce  0 nella posiz 0

my_list[-2:]=[7,1] #sostituisce gli ultimi 2 numeri della lista

#verifica
animals=["cane","gatto","topo"]
"uomo" in animals #mi dice se la parola è presente nella lista

#rimozione per valore
animals.remove("gatto") #rimuove la parola gatto dalla lista

#rimozione per indice (ESTRAZIONE)
animals=animals.pop(1)

#aggiungere elementi alla lista
animals.append("bestia demoniaca") #inserisce il nuovo elemento in coda
#aggiungere elementi in una certa posizione
animals.insert(1,"topo") #inserisce la parola in indice 1

#TUPLE
#non possono modificarsi

my_tuple=(10,5,8,3,9)
type(my_tuple)

#valgono stesse proprietà di slicing e indexing delle liste ma non si può modificare
#se prova a modificare mi da errore


#ottenere l'indice di un elemento

my_tuple.index("ciao")

#conta gli elementi

my_tuple.count("ciao") #conta quanti ciao sono nella tupla

len(my_tuple) #da la lunghezza della tupla

#SET
#un set è un inseieme di elementi unici non ordinati cioè non compare 2 volte lo stesso elemento e la disposizione al suo interno non è importante

name={"Nome1","Nome2","Nome3"}
#aggiungere elemente
name.add("nome4")

#rimuovere elemento
name.remove("Nome2")
#se provo ad eleminare un elemento che non è presente ottengo un errore
#se non siamo sicuri che un nume sia presente si usa discard
name.discard("paolo")

#estrazione di un elemento da un set
name.pop() #estrae un elemento casualmente

#svuotare un set
name.clear()

#trasformare lista in set
names_list={"Nome1","Nome2","Nome3"}
names_list=set(names_list)

#si può fare l'inverso

names_list=list(names_list)

#frozen set =set immutabili
names=frozenset({"Nome1","Nome2","Nome3"})
#non posso usare il metodo pop

#DIZIONARI
items = {"latte":3, "riso":1, "pane":2} #elementi chiave calore
items["latte"] #restituisce il valore della chiave

items["cereali"]=1 #inserisce la chiave valore

items["yogurt"]={"fragola":2, "bianco";3 } #aggiunge un altro dizioneario

#per estrarre un elemtneto della 2 diz
items["yogurt"]["fragola"]

keys=list(items) #converte in una lista

#per ottenere solo i valori
values=list(items.values())

#CICLI

#ciclo for
n=int(input("Fino a che numero vuoi stampare?"))

for i in range(0,n);
    print(i)

n=int(input("quanti numeri di Fibonacci vuoi stampare?"))
fib_num=0
next_fib_num=1

for i in range(n):
    tmp=next_fib_num
    next_fib_num+=fib_num
    fib_num=tmp
    print\("Il numero di Fibonacci è= %d",(i+1,fib_num))


#swapping
#serve per non utiliz la variab temporanea
n=int(input("quanti numeri di Fibonacci vuoi stampare?"))
fib_num=0
next_fib_num=1

for i in range(n):
    fib_num,next_fib_num=next_fib_num,next_fib_num+fib_num
    print\("Il numero di Fibonacci è= %d",(i+1,fib_num))


#Iterazione sulle liste

shopping_list=["p1","p2","p3","p4"]
for i in range(len(shopping_list)):
    print("%d %s)" %(i+1, shopping_list[i]))

shopping_list=["p1","p2","p3","p4"]
for entry in range(len(shopping_list)):
    print("-%s" %entry)

shopping_list=["p1","p2","p3","p4"]
for i,entry in enumerate(shopping_list):
    print("%d %s" %(i+1,entry))

    #CICLO WHILE

#espressioni booleane

#uguaglianza
5==5
#differenza
 5!= 5
 #maggioanza
 6>9
 #mag o uguale
 6>=7

#ciclo while
#in questo caso a differenza del ciclo for va inizializ i e increment
i=0;
while i<n:
    print(i)
    i+=1

    #inter il ciclo se l'indice è mag di un certo break
    i=1
    while i<n:
        if(i>=25):
           break
    print(i)
    i+=2

    #Istruzioni condizionali e operatori logici
n=int(input("Inserisci un numero positivo:"))
    if(n%2==0);
    print("%d è un numero pari "%n)
    else
    print("%d è un numero dispari "%n)
#if if
    if(n<0):
        print("%d non è un numero positivo" %n)
    if (n % 2 == 0);
        print("%d è un numero pari " % n)
        else
        print("%d è un numero dispari " % n)

        #se voglio concatenare se è neg si ferma al primo if
if (n < 0):
    print("%d non è un numero positivo" % n)
    elif (n % 2 == 0);
    print("%d è un numero pari " % n)
    else
    print("%d è un numero dispari " % n)

    #si possono usare gli operatri logici
    #AND
    1==1 and 2==2
    1==2 or 2==1
    not x==n

    #FUNZIONI

    def calarea(b,h):
        area=b*h/2
        return area
    b=5
    h=5
    area=calarea(b,h)

    #funzione senza return

    def print_shoppinglist(shopping_list)
        print("La tua lista è")
        for i,entry in enumerate(shopping_list):
            print("%d %s"%(i+1,entry))


  print_shoppinglist(shopping_list)

  #CLASSI E BASI
  #creare classe

  class Triangle:
      #le funz della classe vengono chiamate metodi
     def area(self,b,h):
         return b*h/2
     def perimeter(self,a,b,c):
         return a+b+c
     triangle=Triangle()

  triangle.area(3,5) #rest area
  triangle.perimeter(4,3,8)  #rest perimetro

#oppure usando gli attrib
#GEOMETRI
class Triangle:
    #per idnicare una stringa

"""
Questa classe rappresenta un triangolo
"""
def __init__(self,a,b,c,h):
    self.a,self.b,self.c,self.h=a,b,c,h

    def area(self):
        return self.b * self.h / 2

    def perimeter(self):
        """
        Calcolo del perimetro del triangolo
        """
        return self.a + self.b + self.c
    triangle = Triangle(4,3,8,3)
triangle.area()  # rest area
triangle.perimeter()  # rest perimetro


#MODULI e STANDARD LIBRARY
#per importare un modulo si scive import NOMEMOD senza .py
import script

#per eseguire una funz del modulo

script.NOMFUNZ()

import Geometry
x=Geometry.x(6.)
x.area()
rectangle=Geometry.Rectangle(5,3)
rectangle.perimeter()
from Geometry import Triangle, Squ

#ci sono funzioni già implement in python per import
import os
os.getcwd()

import datetime
datetime.datetime.now()
#per calc il tempo per eseg una funz
from time import time
n=2
pow=10
tick=time.time()
for _ in range(pow)
    n_pow*=n
    duration=time()*tick



