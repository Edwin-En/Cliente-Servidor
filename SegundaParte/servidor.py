# Servidor que presta el servicio de una calculadora

import zmq
import os
import json


def Recibir():
    #if os.path.exists("CarpetaServidor"):
    #carpeta = os.mkdir("CarpetaServidor")
    archivorecibido = open("/home/utp/Descargas/SegundaParte/CarpetaServidor/ArchivoRecibido.txt", "wb")
    data = socket.recv(1024)
    archivorecibido.write(data)

    print("Se ha recibido el archivo")
    archivorecibido.close()
    socket.send_string("Ok")
    #else:
    #    print("error al recibir el archivo")


def Enviar():


    archivo = open("/home/utp/Descargas/SegundaParte/CarpetaServidor/prueba.txt" , "rb")
    contenido = archivo.read(1024)
    socket.recv_string()
    while contenido:                               # Recibe por teclado y guarda en la variable "x"
        socket.send(contenido)                           # hace el send (envia) envia un mensaje
        contenido = archivo.read(1024)                 # recibe del servidor un mensaje si no lo recibiera para la ejecucion

    archivo.close()
    print("El archivo se ha enviado")
    mensajeentrante = socket.recv_string()
    socket.send_string("ok")

def Listar():
    socket.recv_string()
    lista = os.listdir("/home/utp/Descargas/SegundaParte/CarpetaServidor")                  # Ruta especifica de la carpeta que desea listar
    listajson = json.dumps(lista)
    socket.send_string(listajson)

#def Cerrar():
#    socket.recv_string("Fin")
#    print("Fin de la comunicacion del servidor")

#    socket.close()

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        print("Servidor activo")
        mensaje = socket.recv_string()
        mensajesale = socket.send_string("ok")
        if mensaje == "1":
            Recibir()
        if mensaje == "2":
            Enviar()
        if mensaje == "3":
            Listar()
        if mensaje == "4":
            socket.close()
