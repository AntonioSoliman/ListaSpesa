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
    print("Elemento Eliminato")

def svouta():
    lista.clear()
    print("Lista Svuotata")

def conta():
    print("Gli elementi sono: ")
    print(len(lista))

while True:
    print("1. Aggiungi elementi alla lista ")
    print("2. Visualizza elementi della lista ")
    print("3. Elimina elementi della lista ")
    print("4. Conta elementi della lista ")
    print("5. Svuota lista")
    print("0. Esci dal Menu' ")
    a= int(input())
    
    if a== 1:
        aggiungi()
    elif a==2:
        visualizza()
    elif a==3:
       elimina()
    elif a==4:
        conta()
    elif a==5:
        svouta()
    elif a==0 :
        break
   





