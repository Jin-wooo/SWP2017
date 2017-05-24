import sys, socket


IP = "127.0.0.1"
PORT = 8888

print ("Start Client")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sa = (IP, PORT)
s.connect(sa)

while True :
    msg = input("Input MSG Here : ")
    s.sendall(msg.encode())
    data = s.recv(1024)
    print ("Data from server : %s" % data.decode())
    if msg == "stop" :
        break

s.close()