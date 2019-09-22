#!/usr/bin/python3
import socket
from colorama import init,Fore,Back,Style
def puerto():
    while True:
        print("1). scan de puertos abiertos")
        print("2). puerto specifico")
        print("salir")
        user_input = input(" :")
        if user_input == "salir":
            break
        elif user_input == "1":
            print("\n")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = 500
            sock.connect(('localhost',port))
            data = sock.recv(4096)
            sock.closer()
            print(data.decode())


        elif user_input == "2":
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            port = 500
            sock.bind(('localhost',port))
            print("esperando conexiones en el puerto",port)
            sock.listen(1)
            con, client_addr = sock.accept()
            text = "hola soy el servidor"
            con.send(text,encode())
            con.close()
            sock.close()
            print("\n")
        else:
            print("\n")

puerto()

          
