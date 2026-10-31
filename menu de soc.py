def mostrarmenu ():
    print("menu del analista soc")
    print("1.escanear servidor en busca de alertas")
    print("2.escanear estado de firewall")
    print("3.cerrar sesion")

def escanear_servidor ():
    print("escaneando servidor en busqueda de amenazas")
    print ("se encontraron 3 amenazas")
    print ("sistema seguro")

def ver_firewall ():
    print("escanseando estado del firewall")
    print ("firewall activo y funcionando correctamente")

def cerrar_sesion ():
    print("cerrando sesion")
    sesion = False
    
print ("iniciando sesion de analista soc")

sesion = True

while sesion:
    mostrarmenu()
    opcion = input("ingrese una opcion: ")
    
    if opcion == "1":
        escanear_servidor()
    elif opcion == "2":
        ver_firewall()
    elif opcion == "3":
        print("cerrando sesion")
        cerrar_sesion()
    else:
        print("opcion incorrecta")