
# Servidor que presta el servicio de una calculadora

import zmq

context = zmq.Context()             # Guarda el resultado de una funcion
socket = context.socket(zmq.REP)    # Creo un socket con "contexto"
socket.bind("tcp://*:5555")         # Le digo al socket 3 cosas: el protocolo tcp es para comunicacion
                                    # //*: es la interfaz de red por defecto
                                    # "5555" es una peticion para que se comunique por ese puerto


while True:                                 # siempre esta activo

    mensaje1 = socket.recv_string()         # en la variable "mensaje1" guardo el resultado de la funcion

    mensaje11 = int(mensaje1)               # en la variable mensaje11 paso de cadena a entero el mensaje1

    print("Mensaje recibido:" , mensaje11)  # imprimo el mensaje

    socket.send_string("ok")                # Envia al cliente un mensaje "ok" en string

    mensaje2 = socket.recv_string()         # recibe el segundo mensaje y lo guarda en una variable
    mensaje22 = int(mensaje2)               # cambia de formato el mensaje

    print("Mensaje recibido:" , mensaje22)  # imprimo el mensaje
    socket.send_string("ok")                # Envia al cliente un mensaje "ok" en string

    mensaje3 = socket.recv_string()         # Recibe un tercer mensaje, en este debe venir la operacion

    if (mensaje3 == "+"):                   # Comprueba si es una suma
        total = mensaje11 + mensaje22       # Realiza la operacion y la guarda en la variable "total"

    #total = mensaje11 + mensaje22
    if (mensaje3 == "-"):                   # Comprueba si es una resta
        total = mensaje11 - mensaje22       # Realiza la operacion y la guarda en la variable "total"

    if (mensaje3 == "*"):                   # Comprueba si es una multiplicacion
        total = mensaje11 * mensaje22       # Realiza la operacion y la guarda en la variable "total"

    if (mensaje3 == "/"):                   # Comprueba si es una division
        total = mensaje11 / mensaje22       # Realiza la operacion y la guarda en la variable "total"

    if (mensaje3 == "**"):                  # Comprueba si es una potencia
        total = mensaje11 ** mensaje22      # Realiza la operacion y la guarda en la variable "total"


    totall = str(total)                     # Cambia de formato lo que tenga en la variable "local"

    socket.send_string(totall)              # Envia por el socket lo que tenga en "totall"
