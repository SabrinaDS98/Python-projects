def convers(dato):
    mt=dato*0.000621371
    print('La conversione in miglia terrestri è: ',mt)
    ia=dato*1.09361296
    print('La conversione in iarde è: ',ia)
    pi=dato*3.28084
    print('La conversione in piedi è: ',pi)
    po=dato*39.37008
    print('La conversione in pollici è: ',po)
    mn=dato*0.00053995682073434
    print('La conversione in miglia navali è: ',mn)

m=int(input('Inserisci la misure in metri: '))
c=convers(m)

#Convertire una data (dd:hh:mn) in secondi
def conv_h( data):
    for elementi in data:
        a=data[0]*365*24*60*60
        g=data[1] * 24 * 60*60
        o=data[2] *60 *60
        m=data[3]*60
        tot= a+ o + m + g
    print('In totale ',data[0],'anni',data[1],'giorni',data[2],'ore e',data[3], 'minuti sono', tot ,'secondi')

a=int(input('Inserischi il numero di anni: '))
d=int(input('Inserisci il numero di giorni: '))
h=int(input('Inserisci le ore: '))
min=int(input('Inserisci i minuti: '))
da = [a,d, h, min]
conv_h(da)

#conversione gradi celsius

t=int(input('Inserisci la temperatura da convertire :'))

f=(t*9/5) + 32
print('La temperatura in gradi Fahrenheit è: ',f,'°F')

k=t + 273.15
print('La temperatura in gradi Kelvin è:', k ,'K')


#conversione decimale binario


def d_b(x):
    return int(bin(x)[2:])

num=int(input('Inserisci il numero da convertire:'))

print(d_b(num))

#Codice ascii associato
def trova_ascii():
    carattere = input("Inserisci il carattere che ti interessa convertire: ")
    valore = ord(carattere)
    print( f"Il valore ASCII associato a '{carattere}' è {valore}")

trova_ascii()

#