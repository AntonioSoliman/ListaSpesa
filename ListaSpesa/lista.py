lista = []
def aggiungi():
     x= input("Aggiungi elemento : ")
     lista.append(x)

def visualizza():
    #questo codice stampa tutti gli elementi della lista seguiti da un numero
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def elimina():
    visualizza()
    e = int(input("inserisci elemento da eliminare: "))
    lista.pop(e-1)

while True:
    print("1. Aggiungi elementi alla lista ")
    print("2. Visualizza elementi della lista ")
    print("3. Elimina elementi della lista ")
    print("0. Esci dal Menu' ")
    a= int(input())
    
    if a== 1:
        aggiungi()
    elif a==2:
        visualizza()
    elif a==3:
       elimina()
    elif a==0 :
        break
   





