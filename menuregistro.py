from registro import Registro
from datetime import datetime,date

class MenuRegistro:
    def __init__(self,conexion,cursor):
        self.registro=Registro(conexion,cursor)

        while True:
            print("1) Agregar registro")
            print("2) Buscar por planta")
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
        dia=input("Dia: ")
        mes=input("Mes: ")
        year=input("Año: ")
        fecha=date(int(year),int(mes),int(dia))
        luz=input("Luz (lm): ")
        ph=input("pH: ")
        humedad=input("Humedad %: ")
        co2=input("CO2 %: ")
        id_planta=input("Id planta: ")
        self.registro.agregar(fecha,luz,ph,humedad,co2,id_planta)

    def buscar(self):
        id_planta=input("Id planta: ")
        resultados=self.registro.buscar(id_planta)
        for p in resultados:
            print(p)
            #print("{0:2} {1:10} {2:10}".format(p[0],p[1],str(p[2])))
            print("{0:2} {1:10} {2:3} {3:3} {4:3} {5:3} {5:3}".format(p[0],str(p[1]),p[2],p[3],p[4],p[5],p[6]))
