from socket import *

serverName = "127.0.0.1"
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
numero = "124"
clientSocket.send(numero.encode())
print("Número enviado ao servidor TCP: " + numero)
clientSocket.close()