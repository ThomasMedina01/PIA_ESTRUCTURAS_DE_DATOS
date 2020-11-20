import sys
import sqlite3
from sqlite3 import Error


try:
    with sqlite3.connect("PIA_Bisuteria.db") as conexion:
        enlace = conexion.cursor()
        enlace.execute("CREATE TABLE IF NOT EXISTS TICKET (id_ticket INTEGER PRIMARY KEY AUTOINCREMENT, fecha DATE);")
        enlace.execute("CREATE TABLE IF NOT EXISTS ARTICULO(id_articulo INTEGER PRIMARY KEY AUTOINCREMENT, descripcion TEXT NOT NULL, cantidad INTEGER, precio FLOAT, total FLOAT);")
        enlace.execute("CREATE TABLE IF NOT EXISTS VENTA(Ticket INTEGER NOT NULL REFERENCES 'TICKET'('id_ticket'), Articulo INTEGER NOT NULL REFERENCES 'ARTICULO'('id_articulo'), PRIMARY KEY(Ticket, Articulo));")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")