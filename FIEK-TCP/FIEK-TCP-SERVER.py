import socket
import datetime
import random
import math
from _thread import *

host = "localhost"
port = 9999
global soketi


#Krijimi i soketit
try:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error gjate krijimit te soketit: " + str(error))

#Lidhja e hostit me portin
try:
    soketi.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soketi.bind((host, port))
    print("Serveri eshte startuar ne portin: " + str(port))
    soketi.listen(5)
    print("Serveri eshte i gatshem te pranoj kerkesa...")
except socket.error as error:
    print("Error gjate lidhjes se hostit me portin: " + str(error))



#...........................Metoda IPADRESA......................................
def IPADRESA():
    return "IP adresa e klientit eshte: " + str(address[0])


#...........................Metoda NUMRIIPORTIT...................................
def NUMRIIPORTIT():
    return "Klienti është duke përdorur portin: " + str(address[1])


#...........................Metoda BASHKETINGELLORE...............................
def BASHKETINGELLORE(teksti):
    zanoret = "aeiouyAEIOUY"
    num = 0
    for i in teksti:
        if i.isalpha() & (not i in zanoret):
            num += 1
    return "Teksti i pranuar permban " + str(num) + " bashketingellore"


#...........................Metoda PRINTIMI........................................
def PRINTIMI(fjalia):
    return fjalia.strip()


#...........................Metoda EMRIIKOMPJUTERIT................................
def EMRIIKOMPJUTERIT():
    try:
        return "Emri i klientit është "+ str(socket.gethostbyaddr(host)[0])
    except socket.error as error:
        return "Emri i klientit nuk dihet."


#...........................Metoda KOHA............................................
def KOHA():
    x = datetime.datetime.now()
    return x.strftime("%d.%m.%Y %H:%M:%S %p")


#...........................Metoda LOJA............................................
def LOJA():
    vargu = []
    for x in range(7):
       vargu.append(random.randint(1, 49))
    return str(vargu)


#...........................Metoda FIBONACCI........................................
def FIBONACCI(numri):
    num1 = 0
    num2 = 1
    i = 0
    if int(numri) < 0:
        return "Numri i plote pas funksionit duhet te jete pozitiv"
    elif int(numri) == 0:
        return num1
    elif int(numri) == 1:
        return num2
    while i < int(numri):
        shuma = num1 + num2
        num1 = num2
        num2 = shuma
        i += 1
    return str(num1)


# ...........................Metoda KONVERTIMI......................................
def KONVERTIMI(opsioni, numri):
    numri = float(numri)
    if opsioni == "KILOWATTTOHORSEPOWER":
        return str(numri * 1.341)
    elif opsioni == "HORSEPOWERTOKILOWATT":
        return str(numri / 1.341)
    elif opsioni == "DEGREESTORADIANS":
        return str(numri * math.pi / 180)
    elif opsioni == "RADIANSTODEGREES":
        return str(numri * 180 / math.pi)
    elif opsioni == "GALLONSTOLITERS":
        return str(numri * 3.785)
    elif opsioni == "LITERSTOGALLONS":
        return str(numri / 3.785)
    else:
        return "Opsioni nuk ekziston!"


#...........................Metoda BISEDA...........................................
def BISEDA():
    while 1:
        data = input("You: ")
        if data == 'quit':
            connection.send(str.encode(data))
            print("Biseda perfundoi...")
            break
        if len(str.encode(data)) > 0:
                connection.send(str.encode(data))
                rec = str(connection.recv(1024), "utf-8")
                if rec == "quit":
                    print("Biseda perfundoi...")
                    break
                print("Client:  " + rec)
    return

#...........................Metoda Thread...........................................
def thread(connection, address):
    while True:
        kerkesa = str(connection.recv(1024), "utf-8")
        kerkesa = kerkesa.split(" ")
        if kerkesa[0] == "QUIT":
            print("Klienti ka mbyllur lidhjen...")
            break
        if kerkesa[0] == "IPADRESA":
            connection.send(str.encode(IPADRESA()))
        elif kerkesa[0] == "NUMRIIPORTIT":
            connection.send(str.encode(NUMRIIPORTIT()))
        elif kerkesa[0] == "BASHKETINGELLORE":
            teksti = ""
            teksti = str.join(" ", kerkesa[1:])
            connection.send(str.encode(BASHKETINGELLORE(teksti)))
        elif kerkesa[0] == "PRINTIMI":
            fjalia = ""
            fjalia = str.join(" ", kerkesa[1:])
            connection.send(str.encode(PRINTIMI(fjalia)))
        elif kerkesa[0] == "EMRIIKOMPJUTERIT":
            connection.send(str.encode(EMRIIKOMPJUTERIT()))
        elif kerkesa[0] == "KOHA":
            connection.send(str.encode(KOHA()))
        elif kerkesa[0] == "LOJA":
            connection.send(str.encode(LOJA()))
        elif kerkesa[0] == "FIBONACCI":
            numri = kerkesa[1]
            connection.send(str.encode(FIBONACCI(numri)))
        elif kerkesa[0] == "KONVERTIMI":
            opsioni = kerkesa[1]
            numri = kerkesa[2]
            connection.send(str.encode(KONVERTIMI(opsioni, numri)))
        elif kerkesa[0] == "BISEDA":
            BISEDA()
        else:
            connection.send(str.encode("Kerkesa nuk ekziston!"))
    return

#Lidhja e serverit me klientin
while 1:
    connection, address = soketi.accept()
    print("Serveri u lidh me klientin me IP adrese " + str(address[0]) + " ne portin " + str(address[1]))
    start_new_thread(thread, (connection, address))