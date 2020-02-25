# Cliente que pide conexion a un servidor local para hacer uso de una calculadora

import zmq
import os
import json


def Enviar():

    archivo = open("/home/utp/Descargas/SegundaParte/CarpetaCliente/prueba.txt" , "rb")
    contenido = archivo.read(1024)
    while contenido:                               # Recibe por teclado y guarda en la variable "x"
        socket.send(contenido)                           # hace el send (envia) envia un mensaje
        contenido = archivo.read(1024)                 # recibe del servidor un mensaje si no lo recibiera para la ejecucion

    archivo.close()
    print("El archivo se ha enviado")
    mensajeentrante = socket.recv_string()

def Recibir():
    archivorecibido = open("/home/utp/Descargas/SegundaParte/CarpetaCliente/ArchivoRecibidoCliente.txt", "wb")
    socket.send_string("ok")
    data = socket.recv(1024)
    archivorecibido.write(data)

    print("Se ha recibido el archivo")
    archivorecibido.close()
    socket.send_string("Ok")
    socket.recv_string()

def Listar():
    socket.send_string("ok")
    lista = socket.recv_string()
    listajson = json.loads(lista)
    print("se muestra la lista de archivos")
    print(listajson)


if __name__ == "__main__":
    context = zmq.Context()
    print("Conectando con el servidor")
    socket = context.socket(zmq.REQ)                # REQ define el rol del cliente (hacer solicitudes)
    socket.connect("tcp://localhost:5555")
    print("Se encuentra conectado al servidor ")            # Imprime un mensaje
    condicion = True
    while condicion:
        print("¿Que operacion desea realizar?")
        print("1. Enviar 2. Recibir 3. Listar 4. Salir")
        opcion = input()
        socket.send_string(opcion)
        mensajeentra = socket.recv_string()
        if opcion == "1":
            Enviar()
        if opcion == "2":
            Recibir()
        if opcion == "3":
            Listar()
        if opcion == "4":
            socket.close()
            condicion = False
