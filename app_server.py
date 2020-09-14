import socket
import sys

# using the usual host
# change it to your ip address if doesn't work
host = ''
port = input(str("Enter a valid port number in which to host your file."))
try:
    port = int(port)
    available = 1 <= port <= 65535
    if not available:
        print("Please enter a valid port next time. The port '8080' is used now.")
        port = 8080

except:
    print("Please enter valid number. For example, <8080>")
    sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)

print("Take care to save your html file here first.\n")
filename = input(str("Enter the name of the file.\n"))

print("\nTo check out your html page, go to the following page on your browser: 'localhost:" + "%d'" % port)
# Loop forever, listening for requests:
while True:
    csock, caddr = s.accept()
    print("\nConnection from: " + str(caddr) + "successful!\n")
    req = csock.recv(4096)

    # filename = 'index.html'
    f = open(filename, 'r')

    csock.sendall(str.encode("HTTP/1.0 200 OK\n", 'iso-8859-1'))
    csock.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
    csock.send(str.encode('\r\n'))
    # send data per line
    for l in f.readlines():
        csock.sendall(str.encode("" + l + "", 'iso-8859-1'))
        l = f.read(4096)
    f.close()

    print("Served your html page successfully!\n To exit the server, enter <exit>.")
    command = input(str())

    if command == 'exit':
        print("\nThe server has been closed! Please refresh the page and exit your browser.")
        csock.close()
        sys.exit()
