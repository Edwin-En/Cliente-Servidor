# Cliente que pide conexion a un servidor local para hacer uso de una calculadora

import zmq
import os
import json
import sys
import hashlib


posicion = 1024                #Variable de transferencia 1 Kb

Buf_SIZE = 65536
Part_SIZE = 1024  #1 kb


def SacarHash(filename):
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(Buf_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()




def Enviar():

    print("¿Que archivo desea enviar?")
    print("Se recomienda enviar el archivo de ejemplo prueba.txt")

    archivoleido = input()
    #archivoleido = "prueba.txt"
    archivohash =  SacarHash(archivoleido)

    if os.path.exists(archivoleido):
        archivo = open(archivoleido , "rb")
        i = 0
        socket.send_string(archivohash)
        socket.recv_string()
        while True:
            archivo.seek(posicion*i)
            contenido = archivo.read(posicion)
            if contenido:
                i += 1
                socket.send(contenido)
                socket.recv_string()
            else:
                break

        archivo.close()
        print("El archivo se ha enviado")
        #mensajeentrante = socket.recv_string()
    else:
        print("El archivo no fue encontrado")
        Enviar()

def Recibir():

    #carpeta = os.mkdir("CarpetaCliente")
    archivorecibido = open("CarpetaCliente/archivorecibidocliente", "wb")
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

def Salir():
    socket.send_string("ok")
    print("Terminando conexion con el servidor")
    socket.close()


if __name__ == "__main__":
    context = zmq.Context()
    print("Conectando con el servidor")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")                  # En este espacio modificar la ip de conexion
    print("Se encuentra conectado al servidor ")
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
            Salir()
            condicion = False
