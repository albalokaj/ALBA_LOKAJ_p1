import socket

serverName = 'localhost'
port = 12000
print("Emri i serverit eshte: " + serverName)
print("Emri i portit eshte: " + str(port))
ndrServ = input("Deshironi te ndryshoni emrin e serverit: 'p' - po,  'j' - jo")
if ndrServ == 'p' or ndrServ == 'P':
    serverName = input("Shrkuaj emrin e serverit: ")
ndrPort = input("Deshironi te ndryshoni emrin e portit: 'p' - po,  'j' - jo")
if ndrPort == 'p' or ndrPort == 'P':
    port = input("Shkruaj emrin e portit: ")

global soketi

try:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soketi.connect((serverName, port))
except socket.error as error:
    print("Error gjate lidhjes se klientit me serverin")

while True:
    print("\nZgjedh njeren nga kerkesat: IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE tekst, PRINTIMI tekst, EMRIIKOMPJUTERIT,\n"
          "KOHA, LOJA, FIBONACCI integer, KONVERTIMI opsion numer, BISEDA, QUIT")
    kerkesa = input("Kerkesa: ")
    format1 = str(kerkesa.strip())
    format = str(format1.upper())

    #Nese thirret metoda BISEDA, ekzekutohet kodi ne vijim
    if format == "BISEDA":
        soketi.sendall(str.encode(format))
        while 1:
            answer = str(soketi.recv(1024), "utf-8")
            if answer == "quit":
                print("Biseda perfundoi...")
                break
            print("Server:  " + answer)
            data = input('You:  ')
            if data == "quit":
                soketi.sendall(str.encode(data))
                print("Biseda perfundoi...")
                break
            if len(str.encode(data)) > 0:
                soketi.sendall(str.encode(data))

    else:
            soketi.sendall(str.encode(format))
            answer = str(soketi.recv(1024), "utf-8")
            print(answer)
            if format == "QUIT":
               break