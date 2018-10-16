from planta import Planta
from datetime import datetime,date

class MenuPlanta:
    def __init__(self,conexion,cursor):
        self.planta=Planta(conexion,cursor)

        while True:
            print("1) Agregar planta")
            print("2) Buscar por invernadero")
            print("0) Regresar")
            op=input("Seleccion: ")

            if   op=='1':
                self.agregar()
            elif op=='2':
                self.buscar()
            elif op=='0':
                break
            else:
                print("No valido")

    def agregar(self):
        cultivo=input("Cultivo: ")
        #fecha=datetime.now().date()
        dia=input("Dia: ")
        mes=input("Mes: ")
        year=input("Año: ")
        fecha=date(int(year),int(mes),int(dia))
        id_inv=input("Id invernadero: ")
        id_clasi=input("Id clasificacion: ")
        self.planta.agregar(cultivo,fecha,id_clasi,id_inv)

    def buscar(self):
        id_inv=input("Id Invernadero: ")
        resultados=self.planta.buscar(id_inv)
        for p in resultados:
            #print(p)
            print("{0:2} {1:10} {2:10}".format(p[0],p[1],str(p[2])))
