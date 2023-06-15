#Trovare max e minimo di una lista
#Calcolo media

import random  # random()

lista_n = []  # Lista vuota

num=int(input('Quanti numeri vuoi inserire: '))
minimo =int(input('Inserisci il minimo: '))
massimo = int(input('Inserisci il massimo: '))

for i in range(num):
    x = random.uniform(minimo, massimo)
# x = random.randint(minimo, massimo) RANDOM INTERI

lista_n.append(x)

numero_maggiore = lista_n[0]
for numero in lista_n:
    if numero > numero_maggiore:
        numero_maggiore = numero
print("Il numero maggiore tra tutti è:", numero_maggiore)
numero_minore=lista_n[0]
for numero in lista_n:
    if numero < numero_minore:
        numero_minore = numero
print("Il numero minore tra tutti è:", numero_minore)

med=sum(lista_n)/num
print('la media dei valori della lista è : ', med)


#inserisci i tuoi numeri
numeri_lista = []
print('inserisci i tuoi numeri')
for numero in range(num):
    numeri_lista.append(int(input()))



numero_maggiore2 = numeri_lista[0]
for numero in numeri_lista:
    if numero > numero_maggiore2:
        numero_maggiore2 = numero
print("Il numero maggiore tra tutti è:", numero_maggiore2)
numero_minore2=numeri_lista[0]
for numero in numeri_lista:
    if numero < numero_minore2:
        numero_minore2 = numero
print("Il numero minore tra tutti è:", numero_minore2)

med=sum(lista_n)/num
print('la media dei valori della lista è : ', med)

##

# Scrivi un programma che chieda tre numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
n1=input('Inserisci il primo numero: ')
print(n1)
n2=input('Inserisci il secondo numero: ')
print(n2)
n3=input('Inserisci il terzo numero: ')
print(n3)

if n3 > n1 and n3 > n2:
     print('Il terzo numero è il maggiore')
elif n2 > n1 and n2 > n3:
         print('Il secondo numero è il maggiore')
elif n1 > n2 and n1 > n3:
            print('Il primo numero è il maggiore')
else:
            print('I numeri sono uguali')


#Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri,
# usando asterischi per disegnarlo.

import matplotlib.pyplot

import pandas.plotting


def istogramma(lista):
    for num in lista:
        print('-'* num)

print('inserisci una lista di numeri: ')
import array as arr
lista=arr.array('i',[2,6,8,9,2])


print(istogramma(lista))

import matplotlib.pyplot as plt
#plt.hist(lista)

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=lista, bins='auto', color='r',
                            alpha=0.7, rwidth=0.85)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')

plt.show()


import numpy as np

lista2=np.random.randint(0,10,5)
print(lista2)
istogramma(lista2)
plt.hist(lista2)
plt.show()

##

# Numeri perfetti
def perf(num):
   s=0
   for i in range(1, num//2 + 1):
       if n%i == 0:
         s += i
   if s == num:
        return True
   else:
        return False



n = int(input("Inserisci un numero intero positivo: "))
if perf(n):
    print(f"Il numero {n} è un numero perfetto.")
else:
    print(f"Il numero {n} non è un numero perfetto.")



