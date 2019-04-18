import socket
import datetime
import random
import math

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

#Lidhja e serverit me klientin
while 1:
    connection, address = soketi.accept()
    print("Serveri u lidh me klientin me IP adrese " + str(address[0]) + " ne portin " + str(address[1]))



#...........................Metoda IPADRESA......................................
def IPADRESA():
    print("IP adresa e klientit eshte: " + str(address[0]))


#...........................Metoda NUMRIIPORTIT...................................
def NUMRIIPORTIT():
    print("Numri i portit te klientit eshte: " + str(address[1]))


#...........................Metoda BASHKETINGELLORE...............................
def BASHKETINGELLORE(teksti):
    teksti = input("Shkruani nje tekst: ")
    teksti.strip()
    zanoret = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
    num = 0
    for i in range (len(list(teksti))):
        if list(teksti)[i].isaplha == True & list(teksti)[i] not in zanoret:
            num += 1
    print("Numri i bashketingelloreve ne tekstin " + teksti + " eshte " + str(num))


#...........................Metoda PRINTIMI........................................
def PRINTIMI(fjalia):
    fjalia = input("Shkruani nje fjali: ")
    return fjalia.strip()


#...........................Metoda EMRIIKOMPJUTERIT................................
def EMRIIKOMPJUTERIT():
    try:
        print("Emri i hostit eshte "+ str(socket.gethostbyaddr(host)))
    except socket.error as error:
        print("Emri i hostit nuk mund te gjendet")


#...........................Metoda KOHA............................................
def KOHA():
    x = datetime.datetime.now()
    print("Koha aktuale ne server eshte " + x.strftime("%H:%M:%S"))


#...........................Metoda LOJA............................................
def LOJA():
    print("(", end="")
    for x in range(6):
        print(random.randint(1, 49), end=",")
    print(random.randint(1, 49), end=")")


#...........................Metoda FIBONACCI........................................
def FIBONACCI(numri):
    num1 = 0
    num2 = 1
    i = 0
    if numri < 0:
        print("Numri i plote pas funksionit duhet te jete pozitiv")
    elif numri == 0:
        print(num1)
    elif numri == 1:
        print(num2)
    else:
        while i <= numri:
            shuma = num1 + num2
            num1 = num2
            num2 = shuma
            i += 1
    return num2


# ...........................Metoda KONVERTIMI......................................
def KONVERTIMI(opsioni, numri):
        numri = float(numri)
        if opsioni == "KilowattToHorsepower":
            return numri * 1.341
        elif opsioni == "HorsepowerToKilowatt":
            return numri / 1.341
        elif opsioni == "DegreesToRadians":
            return numri * math.pi / 180
        elif opsioni == "RadiansToDegrees":
            return numri * 180 / math.pi
        elif opsioni == "GallonsToLiters":
            return numri * 3.785
        elif opsioni == "LitersToGallons":
            return numri / 3.785
        else:
            print("Opsioni nuk ekziston!")


#...........................Metoda BISEDA...........................................
def BISEDA(connection):
    while 1:
        data = input("\nYou: ")
        if data == 'quit':
            print("Lidhja me klientit u mbyll...")
            connection.send(str.encode(data))
            connection.close()
            break
        if len(str.encode(data)) > 0:
                connection.send(str.encode(data))
                rec = str(connection.recv(1024), "utf-8")
                if rec == "quit":
                    print("Klienti ka mbyllur lidhjen...")
                    connection.close()
                    break
                print("Client:  " + rec)


