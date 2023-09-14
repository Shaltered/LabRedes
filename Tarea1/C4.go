// Funciones Necesarias
package main

import (
	"fmt"
	"math/rand"
	"net"
	"strconv"
	"strings"
	"time"
)

func main() {
	//Conexion Principal (UDP1) con el servidor intermedio por el puerto 5000
	UdPort := ":5000"
	BUFFER := 1024
	BUFFER2 := 1025
	buffer := make([]byte, BUFFER)
	buffer2 := make([]byte, BUFFER2)

	rand.Seed(time.Now().Unix())

	s, err := net.ResolveUDPAddr("udp4", UdPort)
	if err != nil { //Errores de conexion
		fmt.Println(err)
		return
	}

	connection, err := net.ListenUDP("udp4", s)
	if err != nil { //Errores de conexion
		fmt.Println(err)
		return
	}
	defer connection.Close()

	//LOOP principal del juego
	for true {
		//Conexion UDP2 para enviar jugada al servidor
		UdPort2 := rand.Intn(65535-8000) + 8000 //Generar puerto aleatorio
		s2, err := net.ResolveUDPAddr("udp4", ":"+strconv.Itoa(UdPort2))
		if err != nil { //Errores de conexion
			fmt.Println(err)
			return
		}

		connection2, err := net.ListenUDP("udp4", s2)
		if err != nil { //Errores de conexion
			fmt.Println(err)
			return
		} //Cerrar conexion en cuanto python la cierre

		fmt.Println("Puerto UDP2 Aleatorio :", UdPort2)
		n, addr, _ := connection.ReadFromUDP(buffer) //Lectura de la orden desde intermedio
		msg := string(buffer[:n])
		_, _ = connection.WriteToUDP([]byte(strconv.Itoa(UdPort2)), addr) // Enviar Puerto2
		fmt.Println("Recibi el msg del Server intermedio")
		fmt.Println(msg)

		if msg == "Final" {
			fmt.Println("Juego finalizado")
			return
		} else if msg == "Disponible" {
			_, addr2, _ := connection2.ReadFromUDP(buffer2)
			response1 := "Ready"
			response := []byte(response1)
			_, _ = connection2.WriteToUDP(response, addr2)
		} else { //gaming mode
			fmt.Println("GamingMode")
			_, addr2, _ := connection2.ReadFromUDP(buffer2)
			fmt.Println("Antes de JUgada")
		JUGADA:
			random := rand.Intn(6)
			if !strings.Contains(msg, strconv.Itoa(random)) {
				fmt.Println("Ciclo")
				goto JUGADA
			}
			fmt.Println(random)
			response := strconv.Itoa(random)
			fmt.Println(response)
			responseF := []byte(response)
			fmt.Println("Antes de write")
			_, _ = connection2.WriteToUDP(responseF, addr2)
			fmt.Println("Despues de write")
		}

		connection2.Close()
		//Generar jugada

	}

}
