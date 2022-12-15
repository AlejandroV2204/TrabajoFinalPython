#Universidad del valle - sede Buga.
#Tecnología en Desarrollo de Software - 2724.
#Fundamentos de programación.
#Jhon Alex Rodríguez - 2264363.
#John Alejandro Vallarino Cruz - 2264332.

TarifaAuto = 0
TarifaMoto = 0
Vehiculos = []

TarifaAuto = 40
TarifaMoto = 40
Vehiculos = [

    ["Automóvil  ", "ASD333", 1030, "", "Alberto", "", ""],
    ["Motocicleta", "ASD22F", 1030, "", "Benitez", "", ""],
    ["Automóvil  ", "BCB333", 1130, "", "Carlos", "", ""],
    ["Motocicleta", "GGF33K", 1130, "", "Diego", "", ""]]


def cuadreCaja():
    n = len(Vehiculos)
    print("************* Cuadre de Caja *************")
    ingresosTotales = 0
    for i in range (n):        
        if Vehiculos[i][6] != "":
            ingresosTotales = ingresosTotales + Vehiculos[i][6]
    print("Sumatoria total de los vehículos que registraron salida: "+str(ingresosTotales))

def mostrar(tipo):
    n = len(Vehiculos)
    print("Tipo de búsqueda: "+tipo)
    print("|  TIPO  |  PLACA|ENTRA|SALE| DUEÑO |MIN|TOTAL|")
    for i in range (n):
        for j in range (7):
            if Vehiculos[i][0] == tipo:
                print(Vehiculos[i][j],end=' ')
        if Vehiculos[i][0] != tipo:
            print(end='')
        else:
            print()

def mostrarVehiculo():
    opc = 1
    while opc > 0 and opc < 3:
        print("************* Menú Mostrar Vehículo *************")
        print("1. Mostrar todos los Automóviles.")
        print("2. Mostrar todas las Motocicletas.")
        print("3. Regresar al menú principal.")
        opc = int(input("Eliga una opción: "))
        if opc == 1:
            mostrar("Automóvil  ")
        if opc == 2:
            mostrar("Motocicleta")

def buscar(tipo):
    placa = input("Ingrese la placa a buscar: ")
    n = len(Vehiculos)
    placaEncontrada = False
    tipoVehiculo = False
    for i in range(n):
        if placa == Vehiculos[i][1]:
            placaEncontrada = True
            if tipo == Vehiculos[i][0]:
                tipoVehiculo = True
                if placaEncontrada == True and tipoVehiculo == True:
                    print("Número de Placa: "+Vehiculos[i][1])
                    print("Vehículo tipo: "+Vehiculos[i][0])
                    print("Hora de ingreso: "+str(Vehiculos[i][2]))
                    print("Hora de salida: "+str(Vehiculos[i][3]))
                    print("Nombre: "+Vehiculos[i][4])
                    print("Numero minutos: "+str(Vehiculos[i][5]))
                    print("Total: "+str(Vehiculos[i][6]))
                    pregun = input("¿Desea intentar nuevamente buscar un "+tipo+"? (si/no): ")
                    if pregun == "si":
                        buscar()
    if placaEncontrada == False or tipoVehiculo == False:
        print("!Vehículo no encontrado!")
        pregun = input("¿Desea intentar nuevamente buscar un "+tipo+"? (si/no): ")
        if pregun == "si":
            buscar()


def buscarVehiculo():
    opc = 1
    while opc > 0 and opc < 3:
        print("************* Menú buscar vehículo *************")
        print("1. Buscar Motos")
        print("2. Buscar Autos")
        print("3. Regresar al menú principal")
        opc = int(input("Eliga una opción: "))
        if opc == 1:
            buscar("Motocicleta")           
        if opc == 2:
            buscar("Automóvil  ")
 

def calcularMinutos(hora, hora2):
    hh = hora // 100
    mm = hora % 100
    hh2 = hora2 // 100
    mm2 = hora2 % 100
    minh = (hh * 60) + mm
    minh2 = (hh2 * 60) + mm2
    minutos = minh2 - minh
    return minutos


def salidaVehículo():
    global TarifaAuto
    global TarifaMoto
    vehiculosalida = False
    placaEncontrada = False
    verifiTipo = False
    tarifa = 0
    posicion = 0
    prueba = True
    dato = []
    tipo = input("Ingrese el tipo de vehículo A (Automóvil) o M (Motocicleta): ")
    tipo = verificaTipo(tipo)
    placa = input("Ingrese la placa a buscar: ")
    n = len(Vehiculos)
    for i in range(n):    
        if placa == Vehiculos[i][1]:
            placaEncontrada = True
            posicion = i
            tarifa = Vehiculos[i][6]
            tipoVehiculo = Vehiculos[i][0]
            if tipoVehiculo == tipo:
                verifiTipo = True
        if tarifa == "":
            vehiculosalida = True

    if placaEncontrada == True and vehiculosalida == True and verifiTipo == True:
        hora2 = int(input("Registre la hora de salida en HHMM: "))
        hora2 = verificaHora(hora2)
        hora2 = verificaHoraSalida(Vehiculos[posicion][2], hora2)
        minutos = calcularMinutos(Vehiculos[posicion][2], hora2)
        total = minutos * TarifaAuto
        Vehiculos[posicion][3] = hora2
        Vehiculos[posicion][5] = minutos
        Vehiculos[posicion][6] = total
        print("Tipo de vehículo: "+str(tipo))
        print("Placa: "+placa)
        print("Hora salida: "+str(hora2))
        print("Número de minutos: "+str(minutos))
        print("Total a pagar: "+str(total))
        pregun = input("¿Desea sacar otro vehículo? (si/no): ")
        if pregun == "si":
            salidaVehículo()

    if placaEncontrada == True:
        if vehiculosalida == False:
            print("El vehículo ya salio")
            pregun = input("¿Desea intentar otra vez? (si/no): ")
            if pregun == "si":
                salidaVehículo()
    if placaEncontrada == True:             
        if verifiTipo == False:
            print("El vehículo no esta registrado")
            pregun = input("¿Desea intentar otra vez? (si/no): ")
            if pregun == "si":
                salidaVehículo()
    
    if placaEncontrada == False:
        print("El vehículo no esta registrado")
        pregun = input("¿Desea intentar otra vez? (si/no): ")
        if pregun == "si":
            salidaVehículo()
   

def verificaHoraSalida(hora, hora2):
    if hora > hora2:
        prueba = False
        print("La hora de salida no puede ser menor que la hora de entrada")
        while prueba == False:
            hora2 = int(input("Registre la hora de salida en HHMM: "))
            hora2 = verificaHora(hora2)
            if hora > hora2:
                prueba = False
            else:
                prueba = True
    return hora2


def verificaHora(hora):
    prueba = True
    msj = ""
    hh = hora // 100
    mm = hora % 100
    if hh >= 0 and hh <= 23:
        if mm >= 0 and mm <= 59:
            prueba = True
        else:
            prueba = False
            msj = "Los minutos ingresados son incorrectos"
    else:
        prueba = False
        msj = "La hora ingresada es incorrecta"
    while prueba == False:
        print(msj)
        hora = int(input("Registrar hora en HHMM: "))
        hh = hora // 100
        mm = hora % 100
        if hh >= 0 and hh <= 23:
            if mm >= 0 and mm <= 59:
                prueba = True
            else:
                prueba = False
                msj = "Los minutos ingresados son incorrectos"
        else:
            prueba = False
            msj = "La hora ingresada es incorrecta"
    return hora


def verificaTipo(tipo):
    if tipo == "A" or tipo == "a" or tipo == "M" or tipo == "m":
        verifi = True
    else:
        verifi = False
    while verifi == False:
        print("¡Error, por favor ingrese una opción valida!")
        tipo = input("Ingresar el tipo del vehículo A (Automóvil) o M (Motocicleta): ")
        if tipo == "A" or tipo == "a" or tipo == "M" or tipo == "m":
            verifi = True
        else:
            verifi = False

    if tipo == "A" or tipo == "a":
        tipo = "Automóvil  "
    if tipo == "M" or tipo == "m":
        tipo = "Motocicleta"

    return tipo

def ingresarVehiculo():
    dato = []
    validarPlaca = True 
    tipo = input("Ingresar el tipo del vehículo A (Automóvil) o M (Motocicleta): ")
    tipo = verificaTipo(tipo)
    if tipo == "Automóvil  ":
        placa = input("Ingrese la placa del Automóvil (3 letras seguidas de 3 números): ")
    else:
        placa = input("Ingrese la placa de la motocicleta (3 letras seguida de dos números, seguida de una letra): ")
    n = len(Vehiculos)
    for i in range(n):
        if Vehiculos[i][1] == placa:
            validarPlaca = False
    if validarPlaca == True:
        hora = int(input("Registrar hora de ingreso HHMM: "))
        hora = verificaHora(hora)
        nombre = input("Ingrese el nombre del cliente: ")
        horaS = ""
        minutos = ""
        total = ""
        dato.append(tipo)
        dato.append(placa)
        dato.append(hora)
        dato.append(horaS)
        dato.append(nombre)
        dato.append(minutos)
        dato.append(total)
        Vehiculos.append(dato)
    if validarPlaca == False:
        print("El vehículo ya esta registrado")

def modificarTarifa():
    global TarifaAuto
    global TarifaMoto
    opc = 1
    while opc > 0 and opc < 3:
        print("************* Menú modificar tarifa *************")
        print("1. Modificar tarifa para Automóvil")
        print("2. Modificar tarifa para Motocicleta")
        print("3. Regresar al sub de menú tarifas")
        opc = int(input("Eliga una opción: "))
        
        if opc == 1:
            TarifaAuto = int(input("Ingrese el valor de la tarifa a cobrar por minuto para Automóviles: "))
        if opc == 2:
            TarifaMoto = int(input("Ingrese el valor de la tarifa a cobrar por minuto para Motocicleta: "))
            
def mostrarTarifas():
    global TarifaAuto
    global TarifaMoto
    print("Tarifa por minuto para Automóvil $"+str(TarifaAuto))
    print("Tarifa por minuto para Motocicleta $"+str(TarifaMoto))

def ingresarTarifa():
    global TarifaAuto
    global TarifaMoto
    opc =  1
    while opc > 0 and opc < 3:
        print("************* Menú ingresar tarifa *************")
        print("1. Ingresar tarifa de Automóvil")
        print("2. Ingresar tarifa de Motocicleta")
        print("3. Regresar al sub de Menú tarifas")
        opc = int(input("Eliga una opción: "))

        if opc == 1:
            TarifaAuto = int(input("Ingrese el valor de la tarifa a cobrar por minuto para Automóviles: "))
        if opc == 2:
            TarifaMoto = int(input("Ingrese el valor de la tarifa a cobrar por minuto para Motocicletas: ")) 

def tarifas():
    opc = 1
    while opc > 0 and opc < 4:
        print("************* Menú tarifas *************")
        print("1. Ingresar Tarifas")
        print("2. Mostrar Tarifas")
        print("3. Modificar Tarifas")
        print("4. Regresar al Menú principal")
        opc = int(input("Eliga una opción: "))

        if opc == 1:
            ingresarTarifa()
        if opc == 2:
            mostrarTarifas()
        if opc == 3:
            modificarTarifa()
            

def menu():
    opc = 1
    while opc > 0 and opc < 7:
        print("******** Menú Principal ***********")
        print("1. Tarifas")
        print("2. Ingresar Vehículo")
        print("3. Buscar vehículo")
        print("4. Mostrar vehículo")
        print("5. Salida vehículo")
        print("6. Cuadre de caja")
        print("7. salir")
        opc = int(input("Eliga una opción del menú: "))

        if opc == 1:
            tarifas()
        if opc == 2:
            ingresarVehiculo()
        if opc == 3:
            buscarVehiculo()
        if opc == 4:
            mostrarVehiculo()
        if opc == 5:
            salidaVehículo()
        if opc == 6:
            cuadreCaja()
    print("Gracias por usar nuestro servicio")

menu()  
        
