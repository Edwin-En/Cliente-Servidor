# Servidor que presta el servicio de una calculadora

import zmq
import os
import json

posicion = 1024

# No queda en estado atrapante pero solo recibe 1 parte del archivo, se queda pegado con archivos mayores a 1 kb


def Recibir():

    if os.path.exists("CarpetaServidor"):
        i = 1
        nombredearchivo = socket.recv_string()
        socket.send_string("ok")
        condicion = True

        while condicion:
            data = socket.recv()
            #archivorecibido = open("CarpetaServidor/" + nombredearchivo + ".txt",  "wb")
            archivorecibido = open("CarpetaServidor/" + nombredearchivo + str(i) + ".txt",  "wb")
            archivorecibido.write(data)

            print("Se ha recibido el archivo")
            archivorecibido.close()
            socket.send_string("Ok")
            i += 1
            condicion = False

    else:
        carpeta = os.mkdir("CarpetaServidor")
        Recibir()
        #print("error al recibir el archivo")


def Enviar():

    archivo = open("CarpetaServidor/prueba.txt" , "rb")
    contenido = archivo.read(1024)
    socket.recv_string()
    while contenido:
        socket.send(contenido)                       # hace el send (envia) envia un mensaje
        contenido = archivo.read(1024)

    archivo.close()
    print("El archivo se ha enviado")
    mensajeentrante = socket.recv_string()
    socket.send_string("ok")

def Listar():

    socket.recv_string()
    lista = os.listdir("CarpetaServidor")
    listajson = json.dumps(lista)
    socket.send_string(listajson)

def Salir():
    socket.recv_string()
    print("Terminando ejecucion del servidor")
    socket.close()

if __name__ == "__main__":

    condicion = True
    while condicion:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")
        print("Servidor activo")
        mensaje = socket.recv_string()
        mensajesale = socket.send_string("ok")
        if mensaje == "1":
            Recibir()
        if mensaje == "2":
            Enviar()
        if mensaje == "3":
            Listar()
        #if mensaje == "4":
            #Salir()
            #condicion = False
