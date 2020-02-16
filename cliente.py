
# Cliente que pide conexion a un servidor local para hacer uso de una calculadora

import zmq

context = zmq.Context()                         # crea un contexto "caja negra"

#  Socket to talk to server
print("Conectando con el servidor")
socket = context.socket(zmq.REQ)                # REQ define el rol del cliente (hacer solicitudes)
socket.connect("tcp://localhost:5555")          # el socket hace conexion, usa el protocolo tcp
                                                # localhost es la ip local
                                                # "5555" usa el mismo puerto del servidor

print("ingrese el primero numero: ")            # Imprime un mensaje
x = input()                                     # Recibe por teclado y guarda en la variable "x"
socket.send_string(x)                           # hace el send (envia) envia un mensaje
mensaje1 = socket.recv_string()                 # recibe del servidor un mensaje si no lo recibiera para la ejecucion

print("ingrese el segundo numero:")             # Imprime un mensaje
y = input()                                     # Recibe por teclado y guarda en la variable "y"
socket.send_string(y)                           # hace el send (envia) envia un mensaje
mensaje2 = socket.recv_string()                 # recibe del servidor un mensaje si no lo recibiera para la ejecucion

print("ingrese la operacion (opciones: + - * / **): ")
z = input()                                     # Recibe por teclado y guarda en la variable "z"
socket.send_string(z)                           # Envia el mensaje que este en la variable "z"
mensaje3 = socket.recv_string()                 # Recibe un mensaje
print("Resultado: ", mensaje3)                  # Imprime el resultado del mensaje3
