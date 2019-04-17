import socket
import datetime
import random

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
def BASHKETINGELLORE():
    teksti = input("Shkruani nje tekst: ")
    teksti.strip()
    zanoret = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
    num = 0
    for i in range (len(list(teksti))):
        if list(teksti)[i].isaplha == True & list(teksti)[i] not in zanoret:
            num += 1
    print("Numri i bashketingelloreve ne tekstin " + teksti + " eshte " + str(num))


#...........................Metoda PRINTIMI........................................
def PRINTIMI():
    fjalia = input("Shkruani nje fjali: ")
    print(fjalia.strip())


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
    print("Shtate numra te rastesishem nga rangu [1, 49] jane: (", end="")
    for x in range(6):
        print(random.randint(1, 49), end=",")
    print(random.randint(1, 49), end=")")


#...........................Metoda BISEDA...........................................
def BISEDA():
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