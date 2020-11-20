import datetime
import os
import sys
import sqlite3

class Ventas:
    
    def __init__ (self, descripcion, cantidad, precio_unitario, total, fecha):
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__total = total
        self.__fecha = fecha
        
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def cantidad(self):
        try:
            self.__cantidad == int(self.__cantidad)
            return self.__cantidad
        except ValueError:
            return False
    
    @property
    def precio_unitario(self):
        try:
            self.__precio_unitario == float(self.__precio_unitario)
            return self.__precio_unitario
        except ValueError:
            return False
        
    
    @property
    def total (self):
        return self.__total
    
    @property
    def fecha (self):
        return self.__fecha
#-------------------------------------------------------------------------------------------------------------------

    @cantidad.setter
    def cantidad(self, valor):
        cantidad = valor
            
    @precio_unitario.setter
    def precio_unitario(self, valor):
        self.__precio_unitario= valor
            
    @total.setter
    def total(self,valor):
        total = valor
        
        
    @fecha.setter
    def fecha(self,valor):
        self.__fecha = valor
        
    @descripcion.setter
    def descripcion(self,valor):
        self.__descripcion = valor
      
    @staticmethod
    def comprobacion_precio (instancia):
        if instancia != False:
            return instancia
        while instancia == False:
            nuevo = input("Hubo un error, intentalo nuevamente: ")
            try:
                nuevo = float(nuevo)
                instancia = nuevo
                return instancia
            except:
                print(f"ATENCIÓN: Debe ingresar un número.")
                
    @staticmethod
    def comprobacion_cantidad(instancia):
        if instancia != False:
            return instancia
        while instancia == False:
            nuevo = input("Hubo un error, intentalo nuevamente: ")
            try:
                nuevo = int(nuevo)
                instancia = nuevo
                return instancia
            except:
                print(f"ATENCIÓN: Debe ingresar un número.")

    @staticmethod
    def consulta(a):
        try:
            with sqlite3.connect("PIA_Bisuteria.db") as conexion:
                enlace = conexion.cursor()
                consulta = (f"select Venta.Ticket, Articulo.descripcion, Articulo.cantidad, Articulo.precio, Articulo.total, Ticket.fecha from Ticket, Venta, articulo where Ticket.id_ticket = Venta.Ticket and Articulo.id_articulo = Venta.Articulo and Ticket.fecha = '{a}'")
                enlace.execute(consulta)
                verificar = enlace.fetchall()
                if verificar == None or len(verificar)==0:
                    print("Su fecha no fue encontrada o su tabla se encuentra vacia")
                else:
                    print(f"Venta \t  Articulo \t \t \t  Cantidad \t \t Precio \t \t Total \t \t Fecha")
                    print("-" * 70)
                    for a, b, c, d, e, f  in verificar:
                       print(f"{a} \t  {b} \t \t \t  {c} \t \t {d} \t \t {e} \t \t {f}")
                    print()
                        
        except:
            print(f"Su fecha no fue encontrada o su tabla se encuentra vacia")

    def ver_venta (self):
        print(f"Articulo: {self.__descripcion}")
        #print(f"Número de unidades: {self.__cantidad}")
        #print(f"Precio unitario: {self.__precio_unitario}")
        print(f"Importe: {self.__total}")
        print(f"Fecha de registro: {self.__fecha}")
    
        
#-------------------------------------------------------------------------------------------------------------------
    def guardar_ticket(self):
        try:
            with sqlite3.connect("PIA_Bisuteria.db") as conexion:
                enlace = conexion.cursor()
                #---------------------------------------------------
                enlace.execute("select max(id_ticket) from TICKET")
                c = enlace.fetchone()
                if c[0] == None:
                    c = 1
                else:
                    c = int(c[0])
                #instruccion1 = f"INSERT INTO Ticket Values({c}, '{self.__fecha}');"
                #--------------------------------------------------------------------
                enlace.execute("select max(id_articulo)+1 from ARTICULO")
                x = enlace.fetchone()
                if x[0] == None:
                    x = 1
                else:
                    x = int(x[0])
                instruccion2 = f"INSERT INTO Articulo Values({x}, '{self.__descripcion}', {self.__cantidad}, {self.__precio_unitario}, {self.__total});"
                #----------------------------------------------------------------------------
                instruccion3 = f"INSERT INTO VENTA Values({c}, {x});"
                #enlace.execute(instruccion1)
                enlace.execute(instruccion2)
                enlace.execute(instruccion3)
                print("Articulo registrado a la venta actual exitosamente.")
        except sqlite3.Error as e:
            print (f"Error de sql {e}")
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}{c}")
            

            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}{c}")
            
    @staticmethod
    def crear_ticket(fecha):
        try:
            with sqlite3.connect("PIA_Bisuteria.db") as conexion:
                enlace = conexion.cursor()
                #---------------------------------------------------
                enlace.execute("select max(id_ticket)+1 from TICKET")
                c = enlace.fetchone()
                if c[0] == None:
                    c = 1
                else:
                    c = int(c[0])
                instruccion1 = f"INSERT INTO Ticket Values({c}, '{fecha}');"
                enlace.execute(instruccion1)
                print("Se creo una nueva venta.")
        except sqlite3.Error as e:
            print (f"Error de sql {e}")
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()}{c}")

        
            




            
    