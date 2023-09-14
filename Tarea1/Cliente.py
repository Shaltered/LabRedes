import socket

#Por medio de la utilizacion de la libreria socket de python, crea una conexion TCP
#con el servidor. En caso de que se cree correctamente retorna un objeto tipo Socket
#en caso contrario devuelve False
def crear_conexion_tcp(ip, puerto):
    try:
        # Crear un socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Establecer la conexión con el servidor
        s.connect((ip, puerto))

        print(f"Conexión establecida con {ip}:{puerto}")

        return s  # Devolvemos el objeto de socket para usarlo más tarde

    except socket.error as e:
        print(f"Error al establecer la conexión: {str(e)}")
        return None

def enviar_datos(socket_tcp, datos):
    try:
        # Enviar datos al servidor
        socket_tcp.send(datos.encode())

    except socket.error as e:
        print(f"Error al enviar datos: {str(e)}")

def recibir_datos(socket_tcp, tamano_buffer=1024):
    try:
        # Recibir datos del servidor
        datos = socket_tcp.recv(tamano_buffer).decode()
        return datos

    except socket.error as e:
        print(f"Error al recibir datos: {str(e)}")
        return None

def cerrar_conexion(socket_tcp):
    socket_tcp.close()
    




clientSocket=crear_conexion_tcp("127.0.0.1",5001)
#Inicio del cliente
print("""
- - - - - - - - Bienvenido al Juego - - - - - - - -
- Seleccione una opcion
1-Jugar
2-Salir       
          """)

entrada=input()
flagMenu=True
while(flagMenu):
    if (entrada==1 or entrada == "1"):
        #Flujo normal del juego
        #intento de conexion con el servidor intermedio
        flagJuego=True
        flagGameplay=True
        while(flagJuego):
            enviar_datos(clientSocket,"Disponible")
            disponibilidad=recibir_datos(clientSocket)
            print("respuesta de disponibilidad: {0}".format(disponibilidad))
            print("- - - - - - - - Comienza el Juego - - - - - - - -")

            enviar_datos(clientSocket,"LetsPlay")#Hacer uso del else en servidorIntermedio
            while(flagGameplay):
                Tablero=recibir_datos(clientSocket)#Printea ya sea termino o ultima jugada
                print(Tablero)
                if(Tablero[0]=="¡"):#Lo printeado anterior fue termino y victoria del bot
                    Tablero=recibir_datos(clientSocket)#printear ultimo estado de tablero
                    print(Tablero)
                    #Opciones del jugador (again or end)
                    otra=input("\nTermino de la partida, desea otra partida o terminar el juego?\n1) Otra partida\n2) Salir\n")#AQUI SE MUERE WAAAAA
                    if(otra=="1"):
                        enviar_datos(clientSocket,"LetsPlay")
                        continue
                    else:
                        flagGameplay=False
                        flagJuego=False
                        entrada=2
                        enviar_datos(clientSocket,"Pesimos desarrolladores")
                        continue
                    
                
                    

                
                jugadaPlayer=input("Cual jugada quiere realizar?\n")
                enviar_datos(clientSocket,jugadaPlayer)
   
                Tablero=recibir_datos(clientSocket)#Pos jugada player
                print(Tablero)
                if(Tablero[0]=="¡"):#Lo printeado anterior fue termino
                    Tablero=recibir_datos(clientSocket)#printear ultimo estado de tablero
                    print(Tablero)
                    #Opciones del jugador (again or end)
                    otra=input("\nTermino de la partida, desea otra partida o terminar el juego?\n1) Otra partida\n2) Salir\n")
                    if(otra=="1"):
                        enviar_datos(clientSocket,"LetsPlay")
                        continue
                    else:
                        flagGameplay=False
                        flagJuego=False
                        entrada=2
                enviar_datos(clientSocket,"Pesimos desarrolladores")


        
    elif(entrada==2 or entrada== "2"):
        flagMenu=False
        enviar_datos(clientSocket,"Final")#Termino del game
    else:
        print("Entrada invalida, intentelo de nuevo\n")
        entrada=input()