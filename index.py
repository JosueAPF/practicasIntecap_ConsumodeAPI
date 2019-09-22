#!/usr/bin/python3
from colorama import init,Fore,Back,Style
import os
import backend

while True:
    init()
    print("1. ip scan")
    print("2. puertos abiertos")
    print("salir")
    user_input = input(" :")
    if user_input == "salir":
        break
    elif user_input == "1":
        backend.backend()
    elif user_input == "2":

    else:
        print("\n")
        
    
