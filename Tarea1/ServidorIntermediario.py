import socket

#Por medio de la utilizacion de la libreria socket de python, inicia una conexion
#Por medio del uso de socket, se creara un servidor con conexion TCP en python
"""

host='localhost'
PORT=8000

mi_socket=socket.socket()
mi_socket.bind((host, PORT)) #Asigna el puerto al host y lo asigna a mi_socket
print("Servidor corriendo")
mi_socket.listen(4)  ##Esperar por conexiones entrantes

while True:
    conexion , addr = mi_socket.accept()
    print('Conectado')
    print(addr[0],addr[1],addr)
    message="sex"
    conexion.send(message.encode())

    respuesta=conexion.recv(1024).decode()
    print(respuesta)
    conexion.close()
"""

#Retorna los lugares donde es posible jugar
def posiblesJugadas(lista):
    plays=[]
    for x in range(len(lista)):
        if (lista[x][0]==0):
            plays.append(x+1)
    if len(plays)>0:
        return plays
    else:
        return None

#mostrar tablero por medio de impresiones por pantalla
#input: tablero
#output: None
def mostrarTablero(lista):
    t=""
    for i in range(len(lista)):
        s=""
        for j in range(len(lista)):
            s+= " | "+str(lista[j][i])
        s+=" | "
        t+=s+"\n"

    return t


#Iniciar tablero nxn de Conecta4 de dimension predeterminada 6x6
#input: tamanio del cuadrado/tablero
#output: tablero de nxn
def iniciar_tablero(n=6):#valor que representa un espacio vacio es 0
    lista=[]
    for x in range(n):
        lista.append([])
        for y in range(n):
            lista[x].append(0)

    return lista

#Agregar pieza al tablero de Conecta4
#input: tablero, posicion en la matriz, token para representar la ficha jugada
#output: 0 fuera de rango, None si nadie gana, elemento raro si es que se gano
def agregar_pieza(lista,posicion=1,color=''):
    posicion=int(posicion)
    bottom=len(lista)-1 #El fondo o extremo de la matriz es equivalente a el len-1
    posicion-=1 #arregla la posicion para que sea como un arreglo clasico
    if(posicion>bottom or posicion<0 or lista[posicion][0]!=0):#Revisa si la jugada es invalidavalida
        print("Posición fuera de rango")
        return 0
    for x in range(bottom,-1,-1):
        if(lista[posicion][x]==0):
            print("Agregando {0} en ({1},{2})".format(color,posicion+1,len(lista)-x))
            lista[posicion][x]=color

            return checkearPunto(lista,(posicion,x))

#Revision horizontal
def checkHorizontal(lista,xy):
    x,y=xy #ya se encuentra arreglado el concepto de index
    token=lista[x][y]
    bottom=len(lista)-1

    count=1
    #revision izquierda
    x-=1
    #print(x>=0 , token==lista[x][y] , count<4)
    while(x>=0 and token==lista[x][y] and count<4):
            count+=1
            x-=1
            print("Hi",count)
            
    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} horizontal en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token
    
    #print("Revision horizontal izquierda fallida")

    x,y=xy#reinicia posiciones
    #revision derecha
    x+=1
    #print((limites)>=x , token==lista[x][y] , count<4)
    while((bottom)>=x and token==lista[x][y] and count<4):
            count+=1
            x+=1
            print("Hd",count)
            
    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} horizontal en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token
    
    #print("Revision horizontal derecha fallida")
    return None

#revision vertical
def checkVertical(lista,xy):
    x,y=xy #ya se encuentra arreglado el concepto de index
    token=lista[x][y]
    bottom=len(lista)-1

    
    count=1
    #REVISION VERTICAL
    y+=1
    #print(limites>=y , token==lista[x][y] , count<4)
    while(bottom>=y and token==lista[x][y] and count<4):
         count+=1
         y+=1
         print("V",count)

    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} vertical en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token


    ##print("revision vertical fallida")
    return None

#revision diagonal positiva
def checkDiagonalPositiva(lista,xy):
    x,y = xy
    token=lista[x][y]
    bottom=len(lista)-1


    count=1
    #revision diagonal + izquierda
    x-=1
    y+=1

    while(x>=0 and bottom>=y and token==lista[x][y] and count<4):
        x-=1
        y+=1
        count+=1
        print("D+r",count)
    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} diagonal positiva en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token
    
    x,y=xy
    #revision diagonal + derecha
    x+=1
    y-=1
    
    while(bottom>=x and y>=0 and token==lista[x][y] and count<4):
        #print(x,y)
        x+=1
        y-=1
        count+=1
        print("D+f",count)
    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} diagonal positiva en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token

    return None


#revision diagonal negativa
def checkDiagonalNegativa(lista,xy):
    x,y = xy
    token=lista[x][y]
    bottom=len(lista)-1


    count=1
    #retroceder en la diagonal
    x-=1
    y-=1
    while(x>=0 and y>=0 and token==lista[x][y] and count<4):
        x-=1
        y-=1
        count+=1
        print("D-r",count)
    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} diagonal negativa en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token
    
    x,y=xy
    #avanzar en la diagonal
    x+=1
    y+=1
    while(bottom>=x and bottom>=y and token==lista[x][y] and count<4):
        x+=1
        y+=1
        count+=1
        print("D-f",count)
    if (count>=4):
        #VICTORIA DE token####################
        print("Victoria por {0} diagonal negativa en posicion({1},{2})".format(token,xy[0]+1,len(lista)-xy[1]))
        return token


#revisar condicion de victoria
#input: tablero, posicion en la matriz de la ultima jugada
#output: token victorioso o None
def checkearPunto(lista,xy):
    
    if(checkHorizontal(lista,xy)!=None):
        return lista[xy[0]][xy[1]] #Token victorioso
    
    if(checkVertical(lista,xy)!=None):
        return lista[xy[0]][xy[1]] #Token victorioso

    if(checkDiagonalPositiva(lista,xy)!=None):
        return lista[xy[0]][xy[1]] #Token victorioso

    if(checkDiagonalNegativa(lista,xy)!=None):
        return lista[xy[0]][xy[1]] #Token victorioso

    return None




def crear_servidor_tcp(direccion, puerto):
    try:
        # Crear un socket TCP
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enlazar el socket a la dirección y puerto especificados
        servidor.bind((direccion, puerto))

        # Escuchar conexiones entrantes (puedes especificar cuántas conexiones en la cola)
        servidor.listen(5)

        print(f"Servidor escuchando en {direccion}:{puerto}")

        return servidor

    except socket.error as e:
        print(f"Error al crear el servidor: {str(e)}")
        return None

def aceptar_conexion(servidor):
    try:
        # Aceptar una conexión entrante
        cliente_socket, cliente_direccion = servidor.accept()
        print(f"Conexión aceptada desde {cliente_direccion[0]}:{cliente_direccion[1]}")

        return cliente_socket

    except socket.error as e:
        print(f"Error al aceptar la conexión: {str(e)}")
        return None

def enviar_datos(socket_cliente, datos):
    try:
        # Enviar datos al cliente
        socket_cliente.send(datos.encode())

    except socket.error as e:
        print(f"Error al enviar datos: {str(e)}")

def recibir_datos(socket_cliente, tamano_buffer=1024):
    try:
        # Recibir datos del cliente
        datos = socket_cliente.recv(tamano_buffer).decode()
        return datos

    except socket.error as e:
        print(f"Error al recibir datos: {str(e)}")
        return None

def cerrar_conexion(socket):
    socket.close()



if __name__ == "__main__":
    direccion_servidor = '127.0.0.1'  # Puedes cambiar esto a la dirección IP deseada
    puerto_servidor = 5001  # Puedes cambiar esto al puerto deseado

    servidor = crear_servidor_tcp(direccion_servidor, puerto_servidor)
    cliente_socket = aceptar_conexion(servidor)#Cliente socket 
    print("Conexion realizada con cliente")
    
    Flag=True
    servidorUDP= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP
    goData=('localhost',5000)
    
    tablero=iniciar_tablero()
    playerToken="X"
    robotToken="I"
    while Flag:#Mientras no se cierre el programa
        mensaje=recibir_datos(cliente_socket)
        if(mensaje=="Final"):
            Flag=False
            servidorUDP.sendto(mensaje.encode(),goData)#Avisa al c4 que termino
        elif (mensaje=="Disponible"):
            servidorUDP.sendto(mensaje.encode(),goData)
            try:#Conexion UDP2 de puerto aleatorio genereado en Golang
                #Conexion con Gato.go(Server) UDP2

                serverPort2, _ = servidorUDP.recvfrom(1024)#Recibir puerto desde el server por UDP1
                serverPort2=int(serverPort2.decode())
                print("Recibido Puerto SOCKET UDP2 :{}".format(serverPort2))
                serverSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#skt.AF_INET indica la direccion ipv4 y skt.SOCK_DGRAM para el tipo de conexion udp para UDP2
                print("Conectado Puerto SOCKET UDP2 :{}".format(serverPort2))
                serverSocket2.bind(("",serverPort2))
            except:
                pass
              
            serverSocket2.sendto('wa'.encode(), ('localhost', serverPort2))#Enviar posicion mas que nada para saber el address en golang e intercambiar informacion.
            msg2, addr2 = serverSocket2.recvfrom(1025)#Jugada desde el Server UDP2
            serverSocket2.close()
            msg2 =  msg2.decode()
            print (msg2)
            #servidorPort=int(servidorUDP.recvfrom(1024)[0].decode())
            enviar_datos(cliente_socket,"OK")
            

        else:#LetsPLay
            mensaje = str(posiblesJugadas(tablero))
            if(mensaje==None):#No hay jugadas posibles EMPATE
                pass

            #Sector Player
            enviar_datos(cliente_socket,mostrarTablero(tablero))
            
            jugada=recibir_datos(cliente_socket)
            if(jugada=="Final"):
                Flag=False
                servidorUDP.sendto(jugada.encode(),goData)
                break 
            victory=agregar_pieza(tablero,jugada,playerToken)
            if(victory!=0 and victory!=None):
                enviar_datos(cliente_socket,"¡Victoria por parte de {0}!".format("Jugador" if victory==playerToken else "Bot"))
                enviar_datos(cliente_socket,mostrarTablero(tablero))
                tablero=iniciar_tablero()
                continue
                #ALGUIEN GANO FILO ZA PUTA
                
            enviar_datos(cliente_socket,mostrarTablero(tablero))
            #FinPlayerGaming

            mensaje = str(posiblesJugadas(tablero))
            if(mensaje==None):#No hay jugadas posibles EMPATE
                pass
            #Sector Robot
            
            
            servidorUDP.sendto(mensaje.encode(),goData)
            try:#Conexion UDP2 de puerto aleatorio genereado en Golang
                #Conexion con Gato.go(Server) UDP2

                serverPort2, _ = servidorUDP.recvfrom(1024)#Recibir puerto desde el server por UDP1
                serverPort2=int(serverPort2.decode())
                print("Recibido Puerto SOCKET UDP2 :{}".format(serverPort2))
                serverSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#skt.AF_INET indica la direccion ipv4 y skt.SOCK_DGRAM para el tipo de conexion udp para UDP2
                print("Conectado Puerto SOCKET UDP2 :{}".format(serverPort2))
                serverSocket2.bind(("",serverPort2))
            except:
                pass
              
            serverSocket2.sendto('wa'.encode(), ('localhost', serverPort2))#Enviar posicion mas que nada para saber el address en golang e intercambiar informacion.
            msg2, addr2 = serverSocket2.recvfrom(1025)#Jugada desde el Server UDP2
            serverSocket2.close()
            msg2 =  msg2.decode()
            print (msg2)

            victory=agregar_pieza(tablero,msg2,robotToken)#Victoria de bot
            if(victory!=0 and victory!=None):
                correccionFlujoVictoriaBot=recibir_datos(cliente_socket)
                enviar_datos(cliente_socket,"¡Victoria por parte de {0}!".format("Jugador" if victory==playerToken else "Bot"))
                enviar_datos(cliente_socket,mostrarTablero(tablero))
                tablero=iniciar_tablero()
                continue

                #ALGUIEN GANO FILO ZA PUTA
            
            

#Manda lista con posibles jugadas para realizar (en caso de ser player tmb manda el tablero en el estado actual)
#espera a recibir dicha jugada por parte del jugador el cual recibio el estado actual del tablero


"""a=iniciar_tablero()
mostrarTablero(a)
print('\n\n')

agregar_pieza(a,2,"g")

agregar_pieza(a,2,"r")

agregar_pieza(a,3,"g")
agregar_pieza(a,3,"g")
agregar_pieza(a,4,"g")
agregar_pieza(a,4,"g")
agregar_pieza(a,4,"r")
agregar_pieza(a,4,"r")
agregar_pieza(a,1,"r")
agregar_pieza(a,3,"r")
print('\n\n')
mostrarTablero(a)"""