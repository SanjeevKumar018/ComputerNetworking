from socket import *
serverPort = 12015
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("LAPTOP-Q0L2FP25", serverPort))
print ("The server is ready to receive")
while 1:
     sentence,clientAddress = serverSocket.recvfrom(2048)

     file=open(sentence,"r")
     l=file.read(2048)

     serverSocket.sendto(bytes(l,"utf-8"),clientAddress)
     print("sent back to client",l)
file.close()