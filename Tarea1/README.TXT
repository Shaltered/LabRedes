Martin Rodriguez
201973620-5

Tomas Rebolledo
201973537-3

La manera correcta de correr el codigo es runeando primero ya sea C4.go o ServidorIntermediario.py, para correr 
a C4.go hay que escribir el comando "go run C4.go" en la misma direccion en la que se encuentran los archivos, mientras
que para correr a ServidorIntermediario.py hay que correr el codigo como usualmente se hace (como presionar ctrl+F5 desde
Visual Studio Code o F5 desde el propio Idle), luego de que estos 2 codigos esten corriendo, hay que encender al cliente.

Como restriccion, los inputs del cliente deben ser jugadas validas (No en espacios fuera de rango o donde no cabe una nueva ficha ni
letras, solamente el numero a jugar sin espacios extras en el mensaje)
Ejemplo:
| X | 0 | 0 | 0 | 0 | 0 |
| I | 0 | 0 | 0 | 0 | 0 |
| I | 0 | I | 0 | I | 0 |
| X | 0 | I | X | X | 0 |
| X | I | X | X | X | 0 |
| X | X | I | I | I | 0 |
No se puede jugar una pieza en la posicion 1, por lo que las unicas opciones disponibles para jugar son desde la posicion 2 a la 6