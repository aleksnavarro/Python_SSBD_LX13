from dueno import Dueno

class MenuDueno:
    def __init__(self,conexion,cursor):
        self.dueno=Dueno(conexion,cursor)
        while True:
            print("1) Agregar dueño")
            print("2) Mostrar dueños")
            print("0) Regresar")
            op = input("Seleccion: ")

            if   op=="1":
                self.agregar()
            elif op=="2":
                self.mostrar()
            elif op=="0":
                break
            else:
                print("No valido")

    def agregar(self):
        nombre=input("Nombre: ")
        apellidos=input("Apellidos: ")
        self.dueno.crear(nombre,apellidos)

    def mostrar(self):
        resultado=self.dueno.recuperar()
        for r in resultado:
            print("{0:3} {1:10} {2:15}".format(r[0],r[1],r[2]))
