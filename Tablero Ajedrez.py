
from interfaz import RepresentaTablero
import copy
#   a   b    c    d    e    f    g    h
m = [["Br1","Bn","Bb","Bq","Bk","Bb","Bn","Br2"],#8
    ["Bp","Bp","Bp","Bp","Bp","Bp","Bp","Bp"], #7
    ["","","","","","","",""],                 #6
    ["","","","","","","",""],                 #5
    ["","","","","","","",""],                 #4
    ["","","","","","","",""],                 #3
    ["Wp","Wp","Wp","Wp","Wp","Wp","Wp","Wp"], #2
    ["Wr1","Wn","Wb","Wq","Wk","Wb","Wn","Wr2"]] #1
estados = [[]]
tablero=RepresentaTablero(m)
estados.append(copy.deepcopy(m))
pi=[0,0]
pf=[0,0]
palabra = ""
x = ""
movimiento_n = 0
letra = {"A": 0, "B":1, "C": 2, "D":3 , "E":4 , "F":5, "G":6, "H":7}
numeros = {0: 8 , 1:7 , 2:6 , 3:5 , 4:4 , 5:3 , 6:2 , 7:1 , 8:0}
control = [0,0,0,0,0,0]
blancas = True

def contarMovimientos(x):
    if x % 2 == 0:
        print("Mueve el blanco")
    else:
        print("Mueve el negro")

def comprobarMovimientos(x, y):
    if x[0] == "W":
        y = True
        if x == "Wk":
            control[0] += 1
        elif x == "Wr1":
            control[2] += 1
        elif x == "Wr2":
            control[3] += 1
    else:
        y = False
        if x == "Bk":
            control[1] += 1
        elif x == "Br1":
            control[4] += 1
        elif x == "Br2":
            control[5] += 1
    return y

def enroque(x):
    if movimiento_n % 2 == 0:
        b = m[7][4]
        if x == "C" and control[0]== 0 and control[3] == 0 and m[7][5] == "" and m[7][6] == "":
            m[7][6] = m[7][4]
            m[7][5] = m[7][7]
            m[7][4] = ""
            m[7][7] = ""
            mostrarestado(m)
            return

        else:
            print("No se puede realizar el enroque")
        if x == "L" and control[0]== 0 and control[2] == 0 and m[7][1] == "" and m[7][2] == "" and m[7][3] == "":
            m[7][3] = m[7][0]
            m[7][2] = m[7][4]
            m[7][4] = ""
            m[7][0] = ""
            mostrarestado(m)
            return
        else:
            print("No se puede realizar el enroque")
    elif movimiento_n % 2 != 0:
        if x == "C" and control[1] == 0 and control[5] == 0 and m[0][5] == "" and m[0][6] == "":
            m[0][6] = m[0][4]
            m[0][5] = m[0][7]
            m[0][4] = ""
            m[0][7] = ""
            mostrarestado(m)
            return
        else:
            print("No se puede realizar el enroque")
        if x == "L" and control[1] == 0 and control[4] == 0 and m[0][1] == "" and m[0][2] == "" and m[0][3] == "":
            m[0][2] = m[0][4]
            m[0][3] = m[0][0]
            m[0][4] = ""
            m[0][0] = ""
            mostrarestado(m)
            return
        else:
            print("No se puede realizar el enroque")
def torre(x , pf):
    y = 0
    h = ""
    print(x[0])
    if x[0] == "w":
        h = "B"
        print(h)
    elif x[0] == "B":
        h = "W"
        print(h)
    
    if pi[0] == pf[0]:
        for F in range(0 ,  pf[1]):
            A = m[7-F][pf[0]]
            if A == "":
                y = 0
            elif A[0] == x[0]:
                if A == x:
                    y = 0
                else:
                    y = 1
                    break
            elif A[0] != x[0]:
                y = 0
                pf = [pf[0],7-F]                  
                break
    elif pi[1] == pf[1]:
        for F in range(0 ,  pf[1]):
            A = m[pf[1]][7-F]
            if A == "":
                y = 0
            elif A[0] == x[0]:
                if A == x:
                    y = 0
                else:
                    y = 1
                    break
            elif A[0] != x[0]:
                y = 0
                pf = [pf[0],7-F]                  
                break
    elif pi[0] != pi[0] or pi[1] != pf[1]:
        print("El movimiento no es legal")
        return
    if y == 1:
        print("El movimiento no es legal")
        return
    else:
        print("El movimiento es legal")
        mover(pi, pf)


def movimiento_legal(x,pf):
    if x[1] == "r":
        torre(x,pf)
    else:
        mover(pi , pf)
def canviarnumeros(X, Y):
    X[0] = letra[str(X[0]).upper()]
    Y[0] = letra[str(Y[0]).upper()]
    X[1] = numeros[int(X[1])]
    Y[1] = numeros[int(Y[1])]

    return(X , Y)

def mostrarestado(estado):
    for i in estado:
        print(i)
def mover(pi , pf):
    if movimiento_n % 2 == 0:
        if blancas == True:
            m[pf[1]][pf[0]] = x
            m[pi[1]][pi[0]] = ""
            estados.append(copy.deepcopy(m))
            mostrarestado(m)
        else:
            print("Debes mover una pieza blanca")
    else:
        if blancas == False:
            m[pf[1]][pf[0]] = x
            m[pi[1]][pi[0]] = ""
            estados.append(copy.deepcopy(m))
            mostrarestado(m)

        else:
            print("Debes mover una pieza negra")


while palabra != "Exit":
    palabra = input("Quieres decir una posicion?")
    if palabra.lower() == "exit":
        palabra = input("Quieres ver los movimientos de la partida?")
        if palabra.lower() == "si":
            for i in estados:
                mostrarestado(i)
                print("------------------")
        break
    else:
        contarMovimientos(movimiento_n)
        movimiento = input("Escribe la poscion inicial y final")
        if len(movimiento) == 4:
            pi[0] = str(movimiento[0])
            pi[1] = int(movimiento[1])
            pf[0] = str(movimiento[2])
            pf[1] = int(movimiento[3])
            canviarnumeros(pi, pf)
            x = m[pi[1]][pi[0]]
            y = m[pf[1]][pf[0]]
            comprobarMovimientos(x,blancas)
            blancas = comprobarMovimientos(x, blancas)
            movimiento_legal(x, pf)
            tablero.actualiza(m)
            movimiento_n += 1
        elif len(movimiento) == 1:
            enroque(movimiento)
            movimiento_n += 1
            tablero.actualiza(m)
        else:
            print("Escribe bien la posicion")