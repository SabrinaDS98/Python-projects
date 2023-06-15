#Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

# Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro.Senza usare len
def lung(stringa):
    c =0;
    for lettera in stringa:
        c +=1
    return c

carattere = input("Inserisci una parola oppure un carattere: ")
p=lung(carattere)
print('la stringa è lunga : ', p)

# Se viene inserito un carattere verifica se è una vocale
vocali = ["a", "e", "i", "o", "u"]
if p==1:
  if carattere in vocali:
    print(f"Il carattere {carattere} è una vocale")
  else:
    print(f"Il carattere {carattere} non è una vocale")

else:
 #data una parola contare vocali
    l=0
    i=0
    for car in carattere:
        if car in vocali:
                    l += 1

    print('il numero '
          'di vocali presenti è: ',l)

#Ripetizioni vocali
print('Occorrenze a ',carattere.count('a'))
print('Occorrenze e ',carattere.count('e'))
print('Occorrenze i ',carattere.count('i'))
print('Occorrenze o ',carattere.count('o'))
print('Occorrenze u ',carattere.count('u'))

#ricerca carattere
p=input('inserisci la parola o il carattere da ricercare : ')

if p in carattere:
    print('Il carattere è presente')
else:
    print('il carattere non è presente')


import string
def listAlphabet():
  return list(string.ascii_lowercase)

for let in listAlphabet():
    print('Occorrenze ',let,': ', carattere.count(let))
#Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.

def occ_alf(str):
        alf = {}
        for carattere in str:
            if carattere in alf:
                alf[carattere] +=1
            else:
                alf[carattere] =1
        return alf

print(occ_alf(carattere))

#

#Scrivi una funzione che data in ingresso una lista A contenente n parole,
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

def contapa(stringa_ins):
  conta_let = []
  for caratteri in stringa_ins:
        conta_let.append(len(caratteri))
  return conta_let



def char_counter_pro(lista_a):
    return [len(parola) for parola in lista_a]


n = int(input('quante parole vuoi inserire? '))
print('inserisci delle parole (premi invio ad ogni parola): ')
#parole = ['pasta','boa','occhio']

parole_lista = []
for parole in range(n):
    parole_lista.append(str(input()))

print(parole_lista)

lung= contapa(parole_lista)
print(lung)
print(char_counter_pro(parole_lista))


