import socket
import datetime
import random
import math
from _thread import *


udpHost = 'localhost'
udpPort = 12000
global soketi

#Krijimi i soketit
try:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as error:
    print("Error gjate krijimit te soketit: " + str(error))


#Lidhja e hostit me portin
try:
    soketi.bind((udpHost, udpPort))
    print("Serveri eshte startuar ne portin: " + str(udpPort))
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
        return "Emri i klientit është "+ str(socket.gethostbyaddr(udpHost)[0])
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
def BISEDA(address):
    while 1:
        data = input("You: ")
        if data == 'quit':
            soketi.sendto(data.encode(), address)
            print("Biseda perfundoi...")
            break
        if len(str.encode(data)) > 0:
                soketi.sendto(data.encode(), address)
                recv, address = soketi.recvfrom(1024)
                rec = recv.decode()
                if rec == "quit":
                    print("Biseda perfundoi...")
                    break
                print("Client:  " + str(rec))
    return


#...........................Metoda MAX..............................................
def MAX(num1, num2):
    return max(num1, num2)

#...........................Metoda Perpunimi........................................
def Perpunimi(kerkesa1, address):
    kerkesa2 = kerkesa1.decode()
    kerkesa = kerkesa2.split(" ")
    if kerkesa[0] == "QUIT":
        print("Klienti ka mbyllur lidhjen...")
        soketi.sendto(str.encode("Lidhja u mbyll"), address)
        soketi.close()
    if kerkesa[0] == "IPADRESA":
        soketi.sendto(str.encode(IPADRESA()), address)
    elif kerkesa[0] == "NUMRIIPORTIT":
        soketi.sendto(str.encode(NUMRIIPORTIT()), address)
    elif kerkesa[0] == "BASHKETINGELLORE":
        teksti = ""
        teksti = str.join(" ", kerkesa[1:])
        soketi.sendto(str.encode(BASHKETINGELLORE(teksti)), address)
    elif kerkesa[0] == "PRINTIMI":
        fjalia = ""
        fjalia = str.join(" ", kerkesa[1:])
        soketi.sendto(str.encode(PRINTIMI(fjalia)), address)
    elif kerkesa[0] == "EMRIIKOMPJUTERIT":
        soketi.sendto(str.encode(EMRIIKOMPJUTERIT()), address)
    elif kerkesa[0] == "KOHA":
        soketi.sendto(str.encode(KOHA()), address)
    elif kerkesa[0] == "LOJA":
        soketi.sendto(str.encode(LOJA()), address)
    elif kerkesa[0] == "FIBONACCI":
        numri = kerkesa[1]
        soketi.sendto(str.encode(FIBONACCI(numri)), address)
    elif kerkesa[0] == "KONVERTIMI":
        opsioni = kerkesa[1]
        numri = kerkesa[2]
        soketi.sendto(str.encode(KONVERTIMI(opsioni, numri)), address)
    elif kerkesa[0] == "BISEDA":
        BISEDA(address)
    elif kerkesa[0] == "MAX":
        num1 = kerkesa[1]
        num2 = kerkesa[2]
        soketi.sendto(str.encode(MAX(num1, num2)), address)
    else:
        soketi.sendto(str.encode("Kerkesa nuk ekziston!"), address)

#Lidhja e serverit me klientin
try:
    while 1:
        kerkesa1, address = soketi.recvfrom(1024)
        print("Serveri u lidh me klientin me IP adrese " + str(address[0]) + " ne portin " + str(address[1]))
        start_new_thread(Perpunimi, (kerkesa1, address))
except socket.error as err:
    print("Error gjate pranimit te kerkeses")