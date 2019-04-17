import socket

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


def IPADRESA():
    print("IP adresa e klientit eshte: " + str(address[0]))

def NUMRIIPORTIT():
    print("Numri i portit te klientit eshte: " + str(address[1]))



def CONVERSATION():
    while 1:
        data = input("\nYou:  ")
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