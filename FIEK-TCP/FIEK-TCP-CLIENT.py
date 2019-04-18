import socket

serverName = input("Shkruaj hostin: ")
port = int(input("Shkruaj portin: "))


soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soketi.connect((serverName, port))

while True:
    print("Shkruaj njeren nga kerkesat: ")
    kerkesa = input("Kerkesa: ")
    format1 = str(kerkesa.strip())
    format = str(format1.upper())
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