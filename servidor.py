'''
Este servidor irá testar se um número é par ou ímpar
'''

import socket as s

def verificar(valorAReceber):
    resto = valorAReceber % 2

    if(resto == 0):
        print("Número é par")
    else:
        print("É ímpar!")

serverPort = 8000
serverIP = '127.0.0.1'

serverSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print("Server listening...")

while True:
    client_connection, client_address = serverSocket.accept()
    request = client_connection.recv(1024).decode()
    print(request)
    valor = int(request.encode())
    verificar(valor)
    client_connection.close()
