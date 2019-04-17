import socket

serverName = "localhost"
port = 9999
soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soketi.connect((serverName, port))

while 1:
    answer = str(soketi.recv(1024), "utf-8")
    if answer == "quit":
        print("Socketi u mbyll...")
        soketi.close()
        break
    print("Server:  " + answer)
    data = input('\nYou:  ')
    if data == "quit":
        soketi.sendall(str.encode(data))
        print("Socketi u mbyll...")
        soketi.close()
        break
    if len(str.encode(data)) > 0:
        soketi.sendall(str.encode(data))
