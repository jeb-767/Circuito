import time
class coche():
    def __init__(self):
        self.gasolinaMax = 100
        self.ruedas = 4
        self.color = "Azul"
        self.velocidad = 50
        self.gasolina = 0
    def prueba(self):
        print("Hola")
    def setParametros(self,velocidad,gasolina):
        self.gasolinaMax = gasolina
        self.velocidad = velocidad
        self.gasolina = self.gasolinaMax
        return self.gasolinaMax , self.velocidad, self.gasolina
    def Recargar(self):
        recarga = 10
        while self.gasolina <= self.gasolinaMax:
            self.gasolina += recarga
            time.sleep(1)
        self.Carrera()
    def Carrera(self):
        gasto = self.velocidad * 0.1
        distancia = 0
        vel =self.velocidad *1000 / 3600 
        print(gasto)
        while self.gasolina >= 0:
            time.sleep(1)
            print(self.gasolina)
            self.gasolina -= gasto
            distancia += vel
            print(distancia)
            if self.gasolina <= 0:
                print("Te has quedado sin gasolina")
                self.Recargar()
                break
   
            
            
    
        