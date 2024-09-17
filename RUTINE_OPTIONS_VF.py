#Proyecto: Rutine Creator

#Espacio para definir variables ***NO BORRAR NINGUNA DE ESTAS***

salir = 1  #Esta variable controla si todo el codigo se va ejecutar o si se va a cerrar el programa
repetir = 1  #Esta variable controla si se va a mostrar la opcion de mostrar resultados en el menú
guardado = 1  #Esta variable controla si se va ejecutar el bloque de un resultado guardado 
Ca1 = 1  #Esta variable controla si hay resultados guardados en Calculadora 1
Ca2 = 1  #Esta variable controla si hay resultados guardados en Calculadora 2
Ca3 = 1  #Esta variable controla si hay resultados guardados en Calculadora 3
Ca4 = 1  #Esta variable controla si hay resultados guardados en Calculadora 4
ruti = 1  #Esta variable controla si hay resultados guardados en Rutina
Ejer = 1  #Esta variable controla si hay resultados guardados en Ejercicios por musculo
ejec = 1  #Esta variable controla si hay resultados guardados en ejecucion de ejercicios
e1 = 1
e2 = 1
e3 = 1
e4 = 1
e5 = 1    #Estas variables controla si hay resultados guardados en ejecucion de ejercicios por cada musculo.
e6 = 1
e7 = 1
e8 = 1
e9 = 1
e10 = 1
e11= 1
import os #Esto es para que sirva el os.system("Cls"), que sirve como limpiador de pantalla
m1 = {}
m2 = {}
m3 = {}
m4 = {}
m5 = {}
m6 = {}
m7 = {}
m8 = {}
m9 = {}           #  {}  =  DICCIONARIOS DONDE SE GUARADRÁN LOS RESULTADOS DE CADA USUARIO.
m10 = {}
m11 = {}
rutina = {}
camino_3 = {}
Calculadora_1 = {}
Calculadora_2 = {}
Calculadora_3 = {}
Calculadora_4 = {}

def resumir(mirarrr, diccion, mensaje):  #Esta es para acortar una validacion en mustra de datos en la funcion de busqueda_guardado.
    if mirarrr in diccion:
        print(mensaje)

def vermusculo(elegidouser, num, diccion, mira):  #Esta para mostar el resultado de resultados guardados segun lo que el usuario elija.
    if elegidouser == num:
        muestra_resultados(diccion, mira)

def busqueda_guardado(User_Elg):

    if User_Elg in rutina or User_Elg in m1 or User_Elg in m2 or User_Elg in m3 or User_Elg in m4 or User_Elg in m5 or User_Elg in m6 or User_Elg in m7 or User_Elg in m8 or User_Elg in m9 or User_Elg in m10 or User_Elg in m11 or User_Elg in camino_3 or User_Elg in Calculadora_1 or User_Elg in Calculadora_2 or User_Elg in Calculadora_3 or User_Elg in Calculadora_4:
        while True:
            os.system("Cls")
            print("Estos son los lugares en los que el usuario",User_Elg,"tiene resultados guardados:\n")
            if User_Elg in rutina:
                print("--> Rutina ( R )")
            if User_Elg in m1 or m2 or m3 or m4 or m5 or m6 or m7 or m8 or m9 or m10 or m11:
                print("--> Ejercicios por Musculo ( E )")
            if User_Elg in camino_3:
                print("--> Ejecucion de Ejercicios ( X )")
            if User_Elg in Calculadora_1 or User_Elg in Calculadora_2 or User_Elg in Calculadora_3 or User_Elg in Calculadora_4:
                print("--> Calculadoras ( C )")
            
            buscar = input("\nIngresa la letra de la opcion deseada: >>> ")
            buscar = buscar.upper()
            
            if buscar == "R" or buscar == "E" or buscar == "X" or buscar == "C":
                break
            else:
                os.system("cls")
                print("Elegiste una opcion inexistente, vuelve a intentarlo... \n")
                input("Tecla enter para continuar >>> ")


        if buscar == "R" and User_Elg in rutina:
            if User_Elg in rutina:
                muestra_resultados(rutina, User_Elg)
            else:
                os.system("cls")
                print("No hay resultados guardados, para este usuario \n")
                input("Tecla enter para continuar >>> ")

       

        if buscar == "E":
            if User_Elg in m1 or User_Elg in m2 or User_Elg in m3 or User_Elg in m4 or User_Elg in m5 or User_Elg in m6 or User_Elg in m7 or User_Elg in m8 or User_Elg in m9 or User_Elg in m10 or User_Elg in m11:
                while True:
                    os.system("Cls")
                    print("Estos son los musculos de los que hay resultados guardados:\n")
                    resumir(User_Elg, m1, "1: Espalda")
                    resumir(User_Elg, m2, "2: Trapecio")
                    resumir(User_Elg, m3, "3: Hombros")
                    resumir(User_Elg, m4, "4: Tríceps")
                    resumir(User_Elg, m5, "5: Bíceps")
                    resumir(User_Elg, m6, "6: Antebrazo")
                    resumir(User_Elg, m7, "7: Pecho")
                    resumir(User_Elg, m8, "8: Abdominal")
                    resumir(User_Elg, m9, "9: Glúteos")
                    resumir(User_Elg, m10, "10: Cuádriceps")
                    resumir(User_Elg, m11, "11: Pantorrillas")
                    elegido2 = input("Elige el numero del musculo del que deseas ver resultados >>> ")
                    um = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
                    if elegido2 in um:
                        break
                    else:
                        os.system("cls")
                        print("Elegiste una opcion inexistente, vuelve a intentarlo... \n")
                        input("Tecla enter para continuar >>> ")
                        
                vermusculo(elegido2, "1", m1, User_Elg)
                vermusculo(elegido2, "2", m2, User_Elg)
                vermusculo(elegido2, "3", m3, User_Elg)
                vermusculo(elegido2, "4", m4, User_Elg)
                vermusculo(elegido2, "5", m5, User_Elg)
                vermusculo(elegido2, "6", m6, User_Elg)
                vermusculo(elegido2, "7", m7, User_Elg)
                vermusculo(elegido2, "8", m8, User_Elg)
                vermusculo(elegido2, "9", m9, User_Elg)
                vermusculo(elegido2, "10", m10, User_Elg)
                vermusculo(elegido2, "11", m11, User_Elg)
            else:
                os.system("cls")
                print("No hay resultados guardados, para este usuario \n")
                

        if buscar == "X":
            if User_Elg in camino_3:
                muestra_resultados(camino_3, User_Elg)
            else:
                os.system("cls")
                print("No hay resultados guardados, para este usuario \n")
                

        if buscar == "C":
            if User_Elg in Calculadora_1 or User_Elg in Calculadora_2 or User_Elg in Calculadora_3 or User_Elg in Calculadora_4:
                while True:
                    os.system("Cls")
                    print("Estas son las calculadoras con resultados guardados\n")
                    resumir(User_Elg, Calculadora_1, "--> Calculadora calorias diarias: ( 1 )")
                    resumir(User_Elg, Calculadora_2, "--> Calculadora calorias diarias: ( 2 )")
                    resumir(User_Elg, Calculadora_3, "--> Calculadora calorias diarias: ( 3 )")
                    resumir(User_Elg, Calculadora_4, "--> Calculadora calorias diarias: ( 4 )")
                    elegido3 = input("\nElige el numero de la calculadora para ver sus resultados >>> ")
                    ua = ["1", "2", "3", "4"]
                    if elegido3 in ua:
                        break
                    else:
                        os.system("cls")
                        print("Elegiste una opcion inexistente, vuelve a intentarlo... \n")
                        input("Tecla enter para continuar >>> ")
                
                vermusculo(elegido3, "1", Calculadora_1, User_Elg)
                vermusculo(elegido3, "2", Calculadora_2, User_Elg)
                vermusculo(elegido3, "3", Calculadora_3, User_Elg)
                vermusculo(elegido3, "4", Calculadora_4, User_Elg)
            else:
                os.system("cls")
                print("No hay resultados guardados, para este usuario \n")       
    else:
        os.system("cls")
        print("No hay resultados guardados, para este usuario \n")
        


def hacer(validacionmsculo, diccionariomusculo): #Esta muestra los resultados de ejercicios por musculo si la validacion es correcta.
    if validacionmsculo > 1:    
        muestra_resultados(diccionariomusculo)
    else:
        os.system("Cls")
        print("No hay resultados guardados, primero debes usar ejercicios por musculo\n")

def menu_musculos():   #Esta funcion muestra el menu de ejercicios por musculo, en la opcion de rsultados guardados.
    while True:
        os.system("cls")
        print("----- EJERCICIOS POR MUSCULO -----\n")
        print("Elige el músculo que necesites ejercitar:\n ")
        print("1: Espalda")
        print("2: Trapecio")
        print("3: Hombros")
        print("4: Tríceps")
        print("5: Bíceps")
        print("6: Antebrazo")
        print("7: Pecho")
        print("8: Abdominal")
        print("9: Glúteos")
        print("10: Cuádriceps")
        print("11: Pantorrillas")
        global musculo
        musculo = input("\n>>> ")
        print("---------------------------")
        opciones_VALIDAS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        if musculo in opciones_VALIDAS:
            break
        else:
            os.system("cls")
            print("Elegiste una opcion inexistente, vuelve a intentarlo...\n") 
            input("Tecla enter para continuar >>> ")

def menu_musculos2():   #Esta funcion muestra el menu de ejercicios por musculo
    while True:
        os.system("cls")
        print("----- EJERCICIOS GUARDADOS -----\n")
        print("Elige el músculo del que quieres ver el resultado guardado:\n ")
        print("1: Espalda")
        print("2: Trapecio")
        print("3: Hombros")
        print("4: Tríceps")
        print("5: Bíceps")
        print("6: Antebrazo")
        print("7: Pecho")
        print("8: Abdominal")
        print("9: Glúteos")
        print("10: Cuádriceps")
        print("11: Pantorrillas")
        global musculo2
        musculo2 = input("\n>>> ")
        print("---------------------------")
        opciones_VALIDAS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        if musculo2 in opciones_VALIDAS:
            break
        else:
            os.system("cls")
            print("Elegiste una opcion inexistente, vuelve a intentarlo...\n") 
            input("Tecla enter para continuar >>> ")

def muestra_resultados(diccionario, user):   #Esta funcion se encarga de mostar los resultados guardados
    os.system("Cls")
    print("Este es el resultado guardado en el usuario:",user,"\n")
    print(diccionario[user]())

def guardado_resultados(diccionario, resultado):   #Esta funcion se encarga de guardar los resultados en el usuario elegido.
    while True:
        print("\n\n")
        confiramacion = input("Deseas guardar este resultado en otro usuario?\n\nSi: (1)\nNo: (2)\n\n>>> ")
        if confiramacion == "1" or confiramacion == "2":
            break
        else:
            os.system("cls")
            print("Elegiste una opcion inexistente, vuelve a intentarlo\n")
            input("Presione enter para continuar >>> ")
        
    if confiramacion == "1":
        os.system("cls")
        usuario = input("Ingresa el usuario >>> ")
                
        if usuario in diccionario:
            while True:
                os.system("cls")
                hola = input("Ya tines datos guardados en el usuario "+ usuario+". Deseas:\n\n Guardarlos en otro usuario: (1)\n Remplazar datos guardados:  (2)\n\n>>> " )
                if hola == "1" or hola == "2":
                    break
                else:
                    os.system("cls")
                    print("Elegiste una opcion inexistente, vuelve a intentarlo\n")
                    input("Presione enter para continuar >>> ")
            
            if hola == "1":
                os.system("cls")
                cambiar = input("Ingresa el usuario en el que quieres guardar este resultado: >>> ")
                os.system("cls")
                print("\nLos datos se han guardado exitosamente en el usuario: "+ cambiar+"\n")
                diccionario[cambiar] = resultado
                
            elif hola == "2":
                os.system("cls")
                print("Los datos se han reemplazodo exitosamente en el usuario: "+usuario+"\n")
                diccionario [usuario] = resultado
                
        else:
            os.system("cls")
            print("Los datos se han guardado exitosamente en el usuario: "+ usuario+"\n")
            diccionario[usuario] = resultado
             
    elif confiramacion == "2":
        os.system("cls")
        print("Los datos se han guardado exitosamente en el usuario: "+nombre+"\n")
        diccionario[nombre] = resultado

    return diccionario

#Bienvenida al sistema 
while True:
    os.system("cls")
    print("----- LOGIN -----\n")
    nombre = input("Ingrese un usuario >>> ")
    os.system("cls")
    while True:
        print("----- LOGIN -----\n")
        desicion = input("El usuario ingresado ("+nombre+") será el usuario predeterminado del sistema para guardar los resultados.\n\nAceptar    (1)\nReintentar (2)\n\n>>> ")
        if desicion == "1" or desicion == "2":
            break
        else:
            os.system("cls")
            print("Elegite una opcion inexistente, vuelve a intentarlo...\n")
            input("Presione enter para continuar >>> ")
        
    if desicion == "1":
        break
    elif desicion == "2":
        pass

#Menu de opciones
while salir != "10" :
    vali = True
    while vali :
        os.system("Cls")
        print("----- MENÚ PRINCIPAL -----\n")
        print("Escribe el numero de la opcion que deseas para continuar\n")
        if repetir >1 :
            print(">>> Resultados guardados:    (0)")
        else:
            print(" ")
        print(">>> Crear la rutina:         (1)")
        print(">>> Ejercicios por musculo:  (2)")
        print(">>> Ejecucion de ejercicios: (3)")
        print(">>> Calculadoras (varias):   (4)")
        print(">>> SALIR:                   (5)")
        camino = input("\n>>> ")
        os.system("Cls")
        if camino == "1" or camino == "2" or camino == "3" or camino == "4" or camino == "0" or camino == "5":
            vali = False
        else:
            vali = True
            os.system("Cls")
            print("Elegiste una opcion inexistente, vuelve a intentarlo\n")
            input("Presiona enter para continuar >>> ")


    #Codigo de camino 1 (Juan)
    #Elejir la dificultad
    vali = True
    if camino == "1" :
        while vali : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("¿En que nivel te encuentras?\n")
            print("Inicial: (1)")
            print("Intermedio: (2)")
            print("Avanzado: (3)")
            dificultad = input("\n>>> ")
            if dificultad == "1" or dificultad == "2" or dificultad == "3":
                vali = False
                print(" ")
            else:
                os.system("cls")
                print("Elegite una opcion inexistente, vuelve a intentarlo...\n")
                input("Presione enter para continuar >>> ")

        #ELEGIR TREN
        vali = True
        while vali : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Deseas entrenar:\n")
            print("Tren superior: (1)")
            print("Tren Inferior: (2)")
            print("Ambos: (3)")
            tren = input("\n>>> ")
            if tren == "1" or tren == "2" or tren == "3":
                vali = False
                print(" ")
            else:
                os.system("cls")
                print("Elegite una opcion inexistente, vuelve a intentarlo...\n")
                input("Presione enter para continuar >>> ")

        #ELEGIR LUGAR
        vali = True
        while vali : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Deseas entrenar en: \n")
            print("Casa: (1)")
            print("Gimnacio: (2)")
            lugar = input("\n>>> ")
            if lugar == "1" or lugar == "2" or lugar == "3":
                vali = False
                print(" ")
            else: 
                os.system("cls")
                print("Elegite una opcion inexistente, vuelve a intentarlo...\n")
                input("Presione enter para continuar >>> ")


        #MUESTRA DE RESULTADOS SEGUN LO ANTERIOR
        if lugar == "1" and  tren == "1": 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Su idea para la rutina es la sugiente:")
            print("---------------------------")
        
            if (dificultad == "1"):
                def lista_rutina():
                    print("Fondos en silla")
                    print("Flexiones")
                    print("Elevaciones Laterales con botella")
                    print("Dominadas")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "2"): 
                def lista_rutina():
                    print("Fondos en silla")
                    print("Flexiones diamante")
                    print("Elevaciones Laterales con botella")
                    print("Dominadas")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "3"):
                def lista_rutina():
                    print("Fondos en silla")
                    print("Flexiones declinadas")
                    print("Elevaciones Laterales con botella")
                    print("Dominadas")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)

            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
            repetir += 1
            ruti += 1




        if lugar == "1" and tren == "2" : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Su idea para la rutina es la sugiente:")
            print("---------------------------")
            if (dificultad == "1"):
                def lista_rutina():
                    print("Sentadilla")
                    print("Puente de Glúteos")
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "2"): 
                def lista_rutina():
                    print("Sentadilla zumo")
                    print("Puente de Glúteos")
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina()  
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "3"):
                def lista_rutina():    
                    print("Sentadilla cerrada")
                    print("Puente de Glúteos")
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")  
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
            repetir += 1
            ruti += 1


        if lugar == "1" and tren == "3" : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Su idea para la rutina es la sugiente:")
            print("---------------------------")
            
            if (dificultad == "1"):
                def lista_rutina():    
                    print("Flexiones")
                    print("Fondos en silla")
                    print("Dominadas")
                    print("Sentadilla") 
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "2"): 
                def lista_rutina():
                    print("Flexiones diamante")
                    print("Fondos en silla")
                    print("Dominadas")
                    print("Sentadilla zumo") 
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "3"):
                def lista_rutina():
                    print("Flexiones declinadas")
                    print("Fondos en silla, pies elevados")
                    print("Dominadas")
                    print("Sentadilla cerrada") 
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
        
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
            repetir += 1
            ruti += 1

        if lugar == "2" and tren == "1" : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Su idea para la rutina es la sugiente:")
            print("---------------------------")
            if (dificultad == "1"):
                def lista_rutina():    
                    print("Press Banca")
                    print("Curl Alternado")
                    print("Elevaciones laterales con mancuerna")
                    print("Extensiones de triceps con mancuerna")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "2"): 
                def lista_rutina():
                    print("Press Banca")
                    print("Curl Alternado")
                    print("Elevaciones laterales con mancuerna")
                    print("Extensiones de triceps en polea")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "3"):
                def lista_rutina():    
                    print("Press Banca")
                    print("Curl Alternado")
                    print("Elevaciones laterales con mancuerna")
                    print("Extensiones de triceps en polea")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
        
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
            repetir += 1
            ruti += 1

        if lugar == "2" and tren == "2" : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Su idea para la rutina es la sugiente:")
            print("---------------------------")
            if (dificultad == "1"):
                def lista_rutina():    
                    print("Hip Trust")
                    print("Prensa de Piernas")
                    print("Elevaciones de talon en maquina")
                    print("Sentadillas")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "2"): 
                def lista_rutina():    
                    print("Hip Trust")
                    print("Prensa de Piernas")
                    print("Elevaciones de talon en maquina")
                    print("Sentadillas zumo")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "3"):
                def lista_rutina():    
                    print("Hip Trust")
                    print("Prensa de Piernas")
                    print("Elevaciones de talon en maquina")
                    print("Sentadillas abiertas")
                    return " "
                guardado += 1
                lista_rutina() 
                guardado_resultados(rutina, lista_rutina)
    
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
            repetir += 1
            ruti += 1

        if lugar == "2" and tren == "3" : 
            os.system("Cls")
            print("----- RUTINA -----\n")
            print("Su idea para la rutina es la sugiente:")
            print("---------------------------")
            if (dificultad == "1"):
                def lista_rutina():    
                    print("Press Banca")
                    print("Extensiones de triceps cun mancuerna")
                    print("Remo")
                    print("Prensa de Piernas") 
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "2"): 
                def lista_rutina():    
                    print("Press Banca")
                    print("Extensiones de triceps en maquina")
                    print("Remo")
                    print("Prensa de Piernas") 
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
            elif (dificultad == "3"):
                def lista_rutina():    
                    print("Press Banca")
                    print("Extensiones de triceps en maquina")
                    print("Remo")
                    print("Prensa de Piernas") 
                    print("Sentadilla Búlgara")
                    print("Elevaciones de Talón elevado")
                    return " "
                guardado += 1
                lista_rutina()
                guardado_resultados(rutina, lista_rutina)
                
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
            repetir += 1
            ruti += 1

   # Camino 2 (EJERCICIOS POR MÚSCULO)
    if camino == "2":
        menu_musculos()
        os.system("cls")    
        
        print("----- EJERCICIOS POR MUSCULO -----\n")
        if musculo == "1":
            def em1():
                print("----- Espalda -----\n")
                print("Casa: Superman, Remo con banda de resistencia.")
                print("Gimnasio: Dominadas, Remo con barra.")
                return " "
            em1()
            guardado_resultados(m1, em1)
            guardado += 1
            e1 += 1
        elif musculo == "2":
            def em2():
                print("----- Trapecio -----\n")
                print("Casa: Encogimiento de hombros con banda, Elevación frontal con banda.")
                print("Gimnasio: Encogimiento de hombros con mancuernas, Remo al cuello.")
                return " "
            em2()
            guardado_resultados(m2, em2)
            guardado += 1
            e2 += 1
        elif musculo == "3":
            def em3():
                print("----- Hombros -----\n")
                print("Casa: Elevaciones laterales con botellas de agua, Flexiones en pica.")
                print("Gimnasio: Press militar con barra, Elevaciones laterales con mancuernas.")
                return " "
            em3()
            guardado_resultados(m3, em3)
            guardado += 1
            e3 += 1
        elif musculo == "4":
            def em4():
                print("----- Triceps -----\n")
                print("Casa: Fondos en silla, Extensiones de tríceps con banda.")
                print("Gimnasio: Fondos en paralelas, Extensiones de tríceps en polea.")
                return " "
            em4()
            guardado_resultados(m4, em4)
            guardado += 1
            e4 += 1
        elif musculo == "5":
            def em5():
                print("----- Biceps -----\n")
                print("Casa: Curl de bíceps con botellas de agua, Curl de bíceps con banda.")
                print("Gimnasio: Curl con barra, Curl alterno con mancuernas.")
                return " "
            em5()
            guardado_resultados(m5, em5)
            guardado += 1
            e5 += 1
        elif musculo == "6":
            def em6():
                print("----- Antebrazo -----\n")
                print("Casa: Curl de muñeca con botellas de agua, Extensión de muñeca con banda.")
                print("Gimnasio: Curl de muñeca con barra, Extensión de muñeca con mancuernas.")
                return " "
            em6()
            guardado_resultados(m6, em6)
            guardado += 1
            e6 += 1
        elif musculo == "7":
            def em7():
                print("----- Pecho-----\n")
                print("Casa: Flexiones, Flexiones declinadas.")
                print("Gimnasio: Press de banca, Aperturas con mancuernas.")
                return " "
            em7()
            guardado_resultados(m7, em7)
            guardado += 1
            e7 += 1
        elif musculo == "8":
            def em8():
                print("----- Abdominal -----\n")
                print("Casa: Crunches, Plancha.")
                print("Gimnasio: Crunch en máquina, Elevación de piernas colgado.")
                return " "
            em8()
            guardado_resultados(m8, em8)
            guardado += 1
            e8 += 1
        elif musculo == "9":
            def em9():
                print("----- Gluteos -----\n")
                print("Casa: Puente de glúteos, Patadas traseras.")
                print("Gimnasio: Hip thrust con barra, Sentadillas sumo.")
                return " "
            em9()
            guardado_resultados(m9, em9)
            guardado += 1
            e9 += 1
        elif musculo == "10":
            def em10():
                print("----- Cuadriceps -----\n")
                print("Casa: Sentadillas, Zancadas.")
                print("Gimnasio: Sentadilla con barra, Prensa de piernas.")
                return " "
            em10()
            guardado_resultados(m10, em10)
            guardado += 1
            e10 += 1
        elif musculo == "11":
            def em11():
                print("----- Pantorrillas -----\n")
                print("Casa: Elevación de talones en escalón, Elevación de talones en el suelo.")
                print("Gimnasio: Elevación de talones en máquina, Elevación de talones sentado con mancuernas.")
                return " "
            em11()
            guardado_resultados(m11, em11)
            guardado += 1
            e11 += 1
        
        print("\n\nSalir del programa: (10)")
        print("Volver al menú principal: (cualquier otro número o tecla Enter)")
        salir = input("\n>>> ")
        guardado += 1
        repetir += 1
        Ejer += 1


    # Camino 3 (EJECUCIÓN DE EJERCICIOS)
    if camino == "3":
        os.system("cls")
        def ejecucion_ejercicios():
            print("----- EJECUCION DE EJERCICIOS -----\n")
            print("Aquí tienes la ejecución correcta para algunos ejercicios:")
            print("---------------------------")
            print(" ")
            print("Flexiones:")
            print("1. Coloca las manos en el suelo a la altura de los hombros.")
            print("2. Extiende las piernas hacia atrás y apóyate sobre los dedos de los pies.")
            print("3. Mantén el cuerpo recto y baja el pecho hasta casi tocar el suelo.")
            print("4. Empuja el suelo con las manos hasta volver a la posición inicial.")
            print(" ")
            print("Sentadillas:")
            print("1. Coloca los pies a la altura de los hombros.")
            print("2. Baja las caderas como si te fueras a sentar en una silla.")
            print("3. Mantén la espalda recta y no dejes que las rodillas pasen la punta de los pies.")
            print("4. Sube nuevamente a la posición inicial.")
            print(" ")
            print("Fondos en silla:")
            print("1. Coloca las manos en el borde de una silla firme.")
            print("2. Extiende las piernas hacia adelante y apoya los talones en el suelo.")
            print("3. Baja el cuerpo doblando los codos hasta que los brazos formen un ángulo de 90 grados.")
            print("4. Empuja hacia arriba para volver a la posición inicial.")
            print(" ")
            print("Dominadas:")
            print("1. Agarra la barra con las palmas hacia adelante y las manos a la altura de los hombros.")
            print("2. Cuelga con los brazos completamente extendidos.")
            print("3. Sube el cuerpo hasta que la barbilla pase la barra.")
            print("4. Baja el cuerpo controladamente hasta la posición inicial.")
            print(" ")
            print("Press de banca:")
            print("1. Acuéstate en el banco con los pies firmemente en el suelo.")
            print("2. Agarra la barra con las manos a una distancia un poco mayor que la anchura de los hombros.")
            print("3. Baja la barra hasta tocar ligeramente el pecho.")
            print("4. Empuja la barra hacia arriba hasta extender completamente los brazos.")
            print(" ")
            print("Prensa de pierna:")
            print("1. Siéntate en la máquina y coloca los pies en la plataforma a la altura de los hombros.")
            print("2. Baja la plataforma controladamente doblando las rodillas.")
            print("3. Empuja la plataforma hacia arriba hasta extender completamente las piernas.")
            return " "
        ejecucion_ejercicios()
        guardado_resultados(camino_3, ejecucion_ejercicios)    
        guardado += 1
        repetir += 1
        ejec += 1
        print(" ")
        print("Salir del programa: (10)")
        print("Volver al menú principal: (cualquier otro número o tecla Enter)")
        salir = input("\n>>> ")
        

    #Camino 4 (CALCULADORAS)
    if camino == "4" :
        print("----- CALCULADORAS -----\n")
        print("Por favor elige la calculadora que deseas utilizar:\n")
        vali = True
        while vali : 
            print("-Calorías diarias necesarias: (1)")
            print("-Calculadora de porcentaje de grasa corporal: (2)")
            print("-Calculadora de indice de masa corporal: (3)")
            print("-Calculadora de 1RM: (4)")
            calculadora = input("\n>>> ")

            if calculadora == "1" or calculadora == "2" or calculadora == "3" or calculadora == "4":
                vali = False
                print(" ")
            else: 
                os.system("Cls")
                print("Elegiste una opcion inexistente, vuelve a intentarlo\n")
                input("Tecla enter para continuar >>> ")

        if calculadora == "1":
            #Ignacio
            while True:
                os.system("Cls")
                try:
                    print("----- CALORIAS DIARIAS -----\n")
                    peso = float(input("Ingrese su peso en kg: \n\n>>> "))
                    if peso <= 0:
                        print("El peso debe ser un valor positivo.\n")
                        input("Tecla enter para continuar >>> ")
                    else:
                        break
                except ValueError:
                    os.system("Cls")
                    print("Por favor, ingrese un número válido para el peso.\n")
                    input("Tecla enter para continuar >>> ")
            os.system("Cls")
            # Validación para la altura
            while True:
                os.system("Cls")
                try:
                    print("----- CALORIAS DIARIAS -----\n")
                    altura_cm = float(input("Ingrese su altura en cm: \n\n>>> "))
                    if altura_cm <= 0:
                        print("La altura debe ser un valor positivo.\n")
                        input("Tecla enter para continuar >>> ")
                    else:
                        break
                except ValueError:
                    os.system("Cls")
                    print("Por favor, ingrese un número válido para la altura.\n")
                    input("Tecla enter para continuar >>> ")
            os.system("Cls")
            # Validación para la edad
            while True:
                os.system("Cls")
                try:
                    print("----- CALORIAS DIARIAS -----\n")
                    edad = int(input("Ingrese su edad: \n\n>>> "))
                    if edad <= 0:
                        print("La edad debe ser un valor positivo.\n")
                        input("Tecla enter para continuar >>> ")
                    else:
                        break
                except ValueError:
                    os.system("Cls")
                    print("Por favor, ingrese un número válido para la edad.\n")
                    input("Tecla enter para continuar >>> ")
            os.system("Cls")
            # Validación para el nivel de actividad física
            while True:
                os.system("Cls")
                print("----- CALORIAS DIARIAS -----\n")
                print("¿Cuál es su nivel de actividad física?\n")
                print(">>> Sedentario (poco o ningún ejercicio): (1)")
                print(">>> Ligero (ejercicio ligero 1-3 días/semana): (2)")
                print(">>> Moderado (ejercicio moderado 3-5 días/semana): (3)")
                print(">>> Activo (ejercicio intenso 6-7 días/semana): (4)")
                print(">>> Muy activo (ejercicio intenso diario o dos veces al día): (5)")
                try:
                    actividad = int(input("\n>>> "))
                    if actividad in [1, 2, 3, 4, 5]:
                        break
                    else:
                        print("Por favor, ingrese un número entre 1 y 5.\n")
                        input("Tecla enter para continuar >>> ")
                except ValueError:
                    os.system("Cls")
                    print("Por favor, ingrese un número válido para el nivel de actividad física.\n")
                    input("Tecla enter para continuar >>> ")
            os.system("Cls")
            # Validación para el sexo
            while True:
                os.system("Cls")
                print("----- CALORIAS DIARIAS -----\n")
                print("¿Cuál es su sexo? ")
                print("Masculino: (1)")
                print("Femenino: (2)")
                try:
                    sexo = int(input("\n>>> "))
                    if sexo in [1, 2]:
                        break
                    else:
                        print("Por favor, ingrese 1 para Masculino o 2 para Femenino.\n")
                        input("Tecla enter para continuar >>> ")
                except ValueError:
                    os.system("Cls")
                    print("Por favor, ingrese un número válido para el sexo.\n")
                    input("Tecla enter para continuar >>> ")
            os.system("Cls")
            # Asignación del factor de actividad física
            if actividad == 1:
                factor = 1.2
            elif actividad == 2:
                factor = 1.375
            elif actividad == 3:
                factor = 1.55
            elif actividad == 4:
                factor = 1.725
            elif actividad == 5:
                factor = 1.9

            # Cálculo de la TMB
            if sexo == 1:
                tmb = 88.362 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * edad)
            elif sexo == 2:
                tmb = 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * edad)

            def cal_1():
                print("----- RESULTADO (CALORIAS DIARIAS)-----\n")
                calorias = tmb * factor
                print("--------------------------------------------------------------")
                print(f"Su requerimiento calórico diario es: {calorias:.2f} calorías")
                print("--------------------------------------------------------------")
                return " "
            cal_1()
            guardado_resultados(Calculadora_1, cal_1)

            print(" ")
            guardado += 1
            repetir += 1
            Ca1 += 1
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)\n")
            salir = input("\n>>> ")
        elif calculadora == "2":
            
            #Erick
            print(" ")
            while True:
                os.system("Cls")
                print("----- % GRASA CORPORAL -----\n")
                sexo = input("Ingrese su sexo (M para masculino, F para femenino):\n\n>>> ")
                if sexo == "M" or sexo == "F" or sexo == "m" or sexo == "f":
                    break
                else:
                    os.system("Cls")
                    print("Elegiste una opcion inexistente, vuelve a intentarlo\n")
                    input("Tecla enter para continuar >>> ")
            
            while True:
                os.system("Cls")
                print("----- % GRASA CORPORAL -----\n")
                try:
                    cintura = int(input("Ingrese la medida de su cintura (cm):\n\n>>> "))
                    if cintura >= 0 :
                        break
                except ValueError:
                    os.system("Cls")
                    print("No está ingresando un número válido. Por favor, introduzca un valor numérico.")  
                    input("Tecla enter para continuar >>> ")     
           
            while True:
                os.system("Cls")
                print("----- % GRASA CORPORAL -----\n")
                try:
                    cuello = int(input("Ingrese la medida de su cuello (cm):\n\n>>> "))
                    if cuello >= 0:
                        break
                except ValueError:
                    os.system("Cls")
                    print("No está ingresando un número válido. Por favor, introduzca un valor numérico.")
                    input("Tecla enter para continuar >>> ")
           
            while True:
                os.system("Cls")
                print("----- % GRASA CORPORAL -----\n")
                try:
                    estaturaCM = int(input("Ingrese su estatura (cm) (sin punto ni coma):\n\n>>> "))
                    if estaturaCM >= 0:
                        break
                except ValueError:
                    os.system("Cls")
                    print("No está ingresando un número válido. Por favor, introduzca un valor numérico.")    
                    input("Tecla enter para continuar >>> ") 
            os.system("Cls")
            while True:
                os.system("Cls")
                print("----- % GRASA CORPORAL -----\n")
                try:
                    peso = int(input("Ingrese su peso:\n\n>>> "))
                    if peso >= 0:
                        break
                except ValueError:
                    os.system("Cls")
                    print("No está ingresando un número válido. Por favor, introduzca un valor numérico.") 
                    input("Tecla enter para continuar >>> ")
            os.system("Cls")
            if sexo == "F" or sexo == "f":
                os.system("Cls")
                print("----- % GRASA CORPORAL -----\n")
                caderas=print("Ingresa cuanto miden tus caderas\n\n>>> ")
                porcentaje_grasa = (cintura + caderas - cuello) / estaturaCM
            else:
                print("Para hombre:")
                porcentaje_grasa = (cintura - cuello) / estaturaCM    

            porcentaje_grasa = porcentaje_grasa * 100
            porcentaje_grasa=round(porcentaje_grasa, 2)   

            estaturaMT = estaturaCM / 100
            imc = peso / (estaturaMT ** 2)
            imc= round(imc, 2)

            def cal_2():
                os.system("Cls")
                print("----- RESULTADO (% DE GRASA)-----\n")
                print("____________________________________________________")
                print("Su peso es de",peso,"Kg")
                print("Su porcenteje de grasa es",porcentaje_grasa,"%")
                print("Su IMC es de",imc)
                print("____________________________________________________")
                print("Clasificacion        20-30 años     40-59 años     60-79 años \n Bajo en Grasa        <21%           <23%           <24% \n Saludable           21-33%         23-35%         24-36% \n Sobre Peso          33-39%         35-40%         36-42% \n Obesidad            >39%           >40%           >42%")
                return " "
            cal_2()
            guardado_resultados(Calculadora_2, cal_2)

            guardado += 1
            repetir += 1
            Ca2 += 1
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)\n")
            salir = input("\n>>> ")
        elif calculadora == "3":
            
            #Juan
            vali = True
            while vali :
                os.system("Cls")
                print("----- IMS -----\n")
                print("Eligue tu genero:\n")
                print("Femenino: (1)")
                print("Masculino: (2)")
                genero2 = input("\n>>> ")
                
                if genero2 == "1" or genero2 == "2":
                    vali = False
                    print(" ")
                else: 
                    vali = True
                    os.system("Cls")
                    print("Ingresaste un valor incorrecto o fuera del rango, vuelvea intentarlo\n")
                    input("Para continuar pulse tecla enter >>> ") 
            
            vali = True
            while vali:
                try:
                    os.system("Cls")
                    print("----- IMS -----\n")
                    print("Ingresa tu peso:")
                    peso2 = float(input("\n>>> "))
                    if peso2 >= 0 and peso2 <= 1000 :
                        vali = False
                        print(" ")
                except ValueError:
                    vali = True
                    os.system("Cls")
                    print("Ingresaste un valor incorrecto o fuera del rango, vuelvea intentarlo\n")
                    input("Para continuar pulse tecla enter >>> ")

            vali = True
            while vali:
                try:
                    os.system("Cls")
                    print("----- IMS -----\n")
                    print("Ingresa tu altura:")
                    altura2 = float(input("\n>>> "))
                    if altura2 >= 0 and altura2 <= 1000 :
                        vali = False
                        print(" ")
                except ValueError:
                    vali = True
                    os.system("Cls")
                    print("Ingresaste un valor incorrecto o fuera del rango, vuelvea intentarlo\n")
                    input("Para continuar pulse tecla enter >>> ")
            
            os.system("Cls")
            if altura2 >= 100 :
                Imc2 = peso2 /(altura2 * altura2)*10000
            else:
                Imc2 = peso2 /(altura2 * altura2)
            
            def cal_3():
                print("----- RESULTADO (IMS) -----\n")
                print("* * * * * *  * * * * * *")
                print("PESO:  ", peso2, " kg")

                if altura2 >= 100 :
                    print("ALTURA:  ", altura2, " cm")
                else:
                    print("ALTURA:  ", altura2, " m")
                print("* * * * * *  * * * * * *")
                print("SU IMC ES: ", round(Imc2, 2))
                print("* * * * * *  * * * * * *")
                if genero2 == "1":
                    print("RANGO INDICE DE MASA CORPORAL EN MUJERES:")
                    print("MENOS DE 16  = DESNUTRICION")
                    print("DE 17 A 20   = BAJO PESO")
                    print("DE 21 A 24   = NORMAL")
                    print("DE 25 A 29   = SOBREPESO")
                    print("DE 30 A 34   = OBESIDAD")
                    print("DE 35 A 39  = OBES. MARCADA")
                    print("MAS DE 40  = OBES. MORBIDA")
                    print(" ")
                    print("***Estos son valores generales, para mas seguridad acudir a un especialista de la salud***")
                if genero2 == "2":
                    print("RANGO INDICE DE MASA CORPORAL EN HOMBRES:")
                    print("MENOS DE 17  = DESNUTRICION")
                    print("DE 18 A 21  = BAJO PESO")
                    print("DE 21 A 25  = NORMAL")
                    print("DE 26 A 30  = SOBREPESO")
                    print("DE 31 A 35  = OBESIDAD")
                    print("DE 36 A 40  = OBES. MARCADA")
                    print("40 O MAS  = OBES. MORBIDA")
                    print(" ")
                    print("***Estos son valores generales, para mas seguridad acudir a un especialista de la salud***")
                return " "
            cal_3()
            guardado_resultados(Calculadora_3, cal_3)

            repetir += 1
            guardado += 1
            Ca3 += 1
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")

        elif calculadora == "4":
            vali = True
            while vali:
                os.system("Cls")
                try:
                    print("----- 1RM -----\n")
                    pesoLevantado = float(input("Cuanto peso levantaste en tu ejercicio? >>> "))
                    if pesoLevantado <= 0:
                        vali = True
                        os.system("Cls")
                        print("Debe ser mayor a 0\n")
                        input("Para continuar pulse tecla enter >>> ")
                    else:
                        vali = False
                except:
                    os.system("Cls")
                    print("Ingresaste un valor incorrecto o fuera del rango, vuelvea intentarlo\n")
                    input("Para continuar pulse tecla enter >>> ")
            
            vali = True
            while vali:
                os.system("Cls")
                try:
                    print("----- 1RM -----\n")
                    repeticiones = int(input("Cuantas repeticiones completas lograste con ese peso? >>> "))
                    if repeticiones <= 0:
                        vali = True
                        os.system("Cls")
                        print("Debe ser mayor a 0\n")
                        input("Para continuar pulse tecla enter >>> ")
                    else:
                        vali = False
                except:
                    os.system("Cls")
                    print("Ingresaste un valor incorrecto o fuera del rango, vuelvea intentarlo\n")
                    input("Para continuar pulse tecla enter >>> ")
            os.system("Cls")

            def cal_4():
                print("----- RESULTADO (1RM) -----\n")
                Irm = pesoLevantado / (1.0278 - (0.0278 * repeticiones))
                print("Tu peso levantado es de:", pesoLevantado,"Kg")
                print("Tus repeticiones con ese peso son:", repeticiones,"reps")
                print("----------------------------------------------")
                print("Tu 1RM es de:", round(Irm,4),"Kg")
                print("El 1RM recomendado sería de:", round(Irm),"Kg")
                print("----------------------------------------------")
                return " "
            cal_4()
            guardado_resultados(Calculadora_4, cal_4)

            repetir += 1
            guardado += 1
            Ca4 += 1
            print(" ")
            print("Salir del programa: (10)")
            print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
            salir = input("\n>>> ")
    

    #CAMINO O (GUARDADO Y MUESTRA DE RESULTADOS)
    if camino == "0":
        os.system("Cls")
        print("----- RESULTADOS GUARDADOS -----\n")
        print("Por favor escribe el usuario del que deseas ver resultados guardados:\n")
        mirar = input(">>> ")
        os.system("Cls")
        busqueda_guardado(mirar)

        print(" ")
        print("Salir del programa: (10)")
        print("Volver al menu principal: (cualquier otro numero o tecla Enter)")
        salir = input("\n>>> ")
    
    #CAMINO 5 (SALIR)
    if camino == "5":
        exit()