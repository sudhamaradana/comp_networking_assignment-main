#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))
    #Fill in start
    serverSocket.listen(1)
    print('the web server is up on port:', port)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
        try:
            message = connectionSocket.recv(1024)#Fill in start    #Fill in end
            print(message, '::', message.split()[0], ':', message.split()[1])
            filename = message.split()[1]

            print(filename, '||', filename[1:])
            f = open(filename[1:])
            outputdata = f.read() #Fill in start     #Fill in end
            print(outputdata)
            #Send one HTTP header line into socket
            #Fill in start

            connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
            connectionSocket.send(outputdata)
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
            #Fill in end

            #Close client socket
            #Fill in start

            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)