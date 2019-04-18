import socket

serverNameUdp = 'localhost'
portUdp = 12000

ndrServ = input("Deshironi te ndryshoni emrin e serverit: 'p' - po,  'j' - jo")
if ndrServ == 'p' or ndrServ == 'P':
    serverNameUdp = input("Shrkuaj emrin e serverit: ")
ndrPort = input("Deshironi te ndryshoni emrin e portit: 'p' - po,  'j' - jo")
if ndrPort == 'p' or ndrPort == 'P':
    portUdp = input("Shkruaj emrin e portit: ")

global soketi

try:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soketi.connect((serverNameUdp, portUdp))
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
        soketi.sendto(str.encode(format), serverNameUdp)
        while 1:
            answer, serverNameUdp = soketi.recvfrom(1024)
            if answer == "quit":
                print("Biseda perfundoi...")
                break
            print("Server:  " + str(answer))
            data = input('You:  ')
            if data == "quit":
                soketi.sendto(str.encode(data), serverNameUdp)
                print("Biseda perfundoi...")
                break
            if len(str.encode(data)) > 0:
                soketi.sendto(str.encode(data), serverNameUdp)

    else:
            soketi.sendto(str.encode(format), serverNameUdp)
            answer, serverNameUdp = soketi.recvfrom(1024)
            print(answer)
            if format == "QUIT":
               break