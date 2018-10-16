import mysql.connector
from dueno import Dueno
from menudueno import MenuDueno
from menuinvernadero import MenuInvernadero
from menuusuario import MenuUsuario
from menuplanta import MenuPlanta
from menuregistro import MenuRegistro

conexion=mysql.connector.connect(user='alejandro',password='12345',database='invernadero')
cursor=conexion.cursor()

while True:
    print("1) Menu dueño")
    print("2) Menu invernadero")
    print("3) Menu usuario")
    print("4) Menu planta")
    print("5) Menu registro")
    print("0) Salir")
    op=input("Seleccion: ")

    if   op=="1":
        menuD=MenuDueno(conexion,cursor)
    elif op=="2":
        menuI=MenuInvernadero(conexion,cursor)
    elif op=="3":
        menuU=MenuUsuario(conexion,cursor)
    elif op=='4':
        menuP=MenuPlanta(conexion,cursor)
    elif op=='5':
        menuR=MenuRegistro(conexion,cursor)
    elif op=="0":
        break
    else:
        print("No Valido")

#d=dueno(conexion,cursor)
#d.crear('nombres','apellidos')
#nombres=input('Nombre a ingresar: ')
#apellidos=input('Apellidos a ingresar: ')
#d.crear(nombres,apellidos)

#print(d.recuperar())
