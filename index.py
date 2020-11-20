# Programación del menu de la bisutería.

from Ventas import *
from validaciones import *
import datetime
import sys

try:
    while True:
        separador = ("-" * 75 + "\n")
        print("Registro del detalle de ventas de la bisutería.")
        print(separador)

        menu = ["1.- Registrar una venta.", "2.- Consultar las ventas de un día especifico.", "3.- Salir."]
        for i in menu:
            print(i)
            
        intentos = 4
        opcion = input("Elige la opción deseada: ")
        Validacion.limpiar_pantalla()
        while Validacion.entero(opcion) == False:
            intentos -= 1
            opcion = input(f"Intentalo nuevamente, tienes {intentos} intentos mas: ")
            print(separador)
            if intentos == 1:
                intentos += 3
                Validacion.bloqueo(10)
                print(separador)
        
        
        if Validacion.entero(opcion) == 1:
            Validacion.limpiar_pantalla()
            print(separador)
            print("Registro de ventas.")
            print(separador)
            fecha = datetime.date.today()
            Ventas.crear_ticket(fecha)
            '''intentos = 4
            numero_ventas = input("¿Cuantas ventas desea registrar? ")
            print(separador)
            while Validacion.cantidad(numero_ventas) == False:
                intentos -= 1
                numero_ventas = input(f"Intentalo nuevamente, ingresa un número entero, tienes {intentos} intentos mas: ")
                print(separador)
                if intentos == 1:
                    Validacion.bloqueo(10)
                    print(separador)
                    intentos += 3'''                
                
            a = True
            while a == True:
                
                intentos = 4
                descripcion = input("Descripción del articulo: ")
                while Validacion.descripcion(descripcion) == None or Validacion.descripcion(descripcion) == False:
                    intentos -= 1
                    descripcion = input(f"Intentalo nuevamente, ingresa un texto, tienes {intentos} intentos mas: ")
                    print(separador)
                    if intentos == 1:
                        Validacion.bloqueo(10)
                        print(separador)
                        intentos += 3
                    
                
                intentos = 4
                unidades = input(f"Cantidad de unidades de {descripcion}: ")
                while Validacion.cantidad(unidades) == False:
                    intentos -= 1
                    unidades = input(f"Intentalo nuevamente, ingresa un número entero, tienes {intentos} intentos mas: ")
                    print(separador)
                    if intentos == 1:
                        Validacion.bloqueo(10)
                        print(separador)
                        intentos += 3

                intentos = 4
                precio = input(f"Precio unitario de {descripcion}: ")
                while Validacion.precio(precio) == False:
                    intentos -= 1
                    precio = input(f"Intentalo nuevamente, ingresa un valor númerico, tienes {intentos} intentos mas: ")
                    print(separador)
                    if intentos == 1:
                        Validacion.bloqueo(10)
                        print(separador)
                        intentos += 3
                total = Validacion.precio(precio) * Validacion.cantidad(unidades)
                venta = Ventas(descripcion, Validacion.cantidad(unidades), Validacion.precio(precio), total, fecha)
                print(separador)
                print(f"Información del producto añadido a la venta.")
                print(separador)
                venta.ver_venta()
                print(separador)
                venta.guardar_ticket()


                reg = input("¿Desea agregar mas articulos a la transaccion? \n Presione 1 para continuar o dos para salir: ")
                while Validacion.continuar(reg) == False:
                    intentos -= 1
                    print(separador)
                    reg = input(f"Intentalo nuevamente, presiona 1 o 2, tienes {intentos} intentos mas: ")
                    print(separador)
                    if intentos == 1:
                        Validacion.bloqueo(10)
                        print(separador)
                        intentos += 3
                        
                if  Validacion.continuar(reg) == 1:
                    print(separador)
                    a == False
                    
                     
                elif Validacion.continuar(reg) == 2:
                    print(separador)
                    break

        if Validacion.entero(opcion) == 2:
            Validacion.limpiar_pantalla()
            print(separador)
            fecha = input("Escriba una fecha(año-mes-dia): ")
            print(f"Ventas realizadas el día {fecha}.")
            print(separador)
            Ventas.consulta(fecha)
            print(separador)

        if Validacion.entero(opcion) == 3:
            print(separador)
            print("EJECUCION FINALIZADA")
            print(separador)
            break
except:
    print(f"Ha ocurrido el siguiente error: {sys.exc_info()}")
