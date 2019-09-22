import os
import json
import socket
import getpass
from urllib.request import urlopen
from colorama import init,Fore,Back,Style


def backend():
    while True:
        init()
        print(" _    ____    ")
        print("| |  |  \ \   ")
        print("| |  | ___|   ")
        print("| |  | |      ")
        print("| |  | |      ")
        print("°°°  °°°°        ")
        print(Fore.LIGHTBLUE_EX+"\n")
        print("1).mis datos")
        print("return:")
        user_input = input(" :")
        if user_input == "return":
            break
        elif user_input == "1":
            print(Fore.LIGHTGREEN_EX+"\n")
            #mybanner
            print(" ___   _  _______  __   __ ")
            print("|   | | ||       ||  | |  |")
            print("|   |_| ||    ___||  |_|  |")
            print("|      _||   |___ |       |")
            print("|     |_ |    ___||_     _|")
            print("|    _  ||   |___   |   |  ")
            print("|___| |_||_______|  |___|  ")
            print("                           ")
            
            while True:
                print("1).mis datos")
                print("(salir)")
                print("  ")
                user_input = input("\n")
                if user_input == "salir":
                    break
                elif user_input == "1":
                    print("\n")
                    username = getpass.getuser()
                    print("\nUSUARIO        ",username)

                    hostname = socket.gethostname()
                    print("\nHOSTNAME       ",hostname)

                    maquinaIP = socket.gethostbyname(hostname)
                    print("\nDireccion IP    ",maquinaIP)

                    
                    url = 'http://ipinfo.io/json'
                    respuesta = urlopen(url)
                    data = json.load(respuesta)

                    print(Fore.GREEN+"---------------------------------")
                    print("\nIP Publica"+":    ",data['ip'])
                    print("\nPAIS"+":          ",data['country'])
                    print("\nCIUDAD"+":        ",data['city'])
                    print("\nDEPARTAMENTO"+":  ",data['region'])
                    print("\nLOCACION"+":      ",data['loc'])
                    #print("\nVENDOR"+":        ",data['name'])
                    #print("\nDIRECCION VENDOR"+":",data['address'])




                else:
                    print("\n")
        else:
            print("\n")
#backend()





  

     
