import string
import random
import os
import time
import json

class genKey:
    def generate_random_password(self):
        os.system('cls')

        chars = list(string.ascii_letters + string.digits + '!@#$%^&*()')
        os.system('cls')
        length = int(input("Introduce la longitud de tu contraseña: "))
        
        random.shuffle(chars)

        passwd = []
        for i in range(length):
            passwd.append(random.choice(chars))

        random.shuffle(passwd)
        self.key=("".join(passwd))
        os.system('cls')
        print('\033[1m'+"Tu contraseña aleatoria es: "+'\033[0m'+self.key)
        return self.key
    
    def getKey(self):
        return self.key
        
    def volver_a_generar(self):	
        a = input("¿Quieres volver a generar una contraseña? (Y/N): ")
        
        if a=="Y" or a=="y":
            self.generate_random_password()
            self.volver_a_generar()
        elif a=="N" or a=="n":
            os.system('cls')
            print("Adios")
            time.sleep(2)
            os.system('cls')
            exit()
        else:
            print("Introduce una opción válida")
            self.volver_a_generar()

p1=genKey()
p1.generate_random_password()

class libreta(genKey):
    def __init__(self):
        super().__init__()
        self.key = p1.getKey()

    def datosKey(self):
        self.nombre=input("¿Con qué nombre quiere guardar su clave?\n")
        os.system('cls')
        self.usuario=input("¿Cuál es el usuario para la contraseña?\n")
        os.system('cls')
    
    def incluirKey(self):
        incluir=input("¿Quiere guardar la contraseña creada?\n(Y/N)\n")
        
        if incluir=="Y" or incluir=="y":
            
            try:
                archivo = open('passwd.txt', 'a')
                print("Archivo creado")
                archivo.write("\n" + self.nombre)
                archivo.write('\n   '+self.usuario+' -> '+self.key)
                archivo.close()
                print("Texto guardado")
                time.sleep(3)
                os.system('cls')
            except FileExistsError:
                print("El archivo ya existe")

        else:
            p1.volver_a_generar()
    
    def mirarLibreta(self):
        q = input("¿Quiere mirar la lista de contraseñas?\n(Y/N)")
        if q == "Y" or q == "y":
            masterKey = input("Introduce la contraseña principal para leer las contraseñas: ")
            
            if str(masterKey) == "Martin123":
                os.system('cls')
                k=open('passwd.txt','r')
                showKeys=k.read()
                print(showKeys)
                quit=input("Para salir de la libreta de contraseñas introduce 'q'")
                
                if quit == "Q" or quit == "q":
                    k.close()

            else:
                print("Contraseña incorrecta. Cerrando el programa")
                os.system('cls')
                exit()
        else:
            pass

p2=libreta()
p2.datosKey()
p2.incluirKey()
p2.mirarLibreta()
p1.volver_a_generar()