import socket
import threading
import random


def ClientThread(connection, addr):
    global indexer
    while True:

        with open('received_file' + str(indexer)+str(random.random()), 'wb') as f:
            print('file opened')
            while True:

                data = connection.recv(1024)

                print('data=%s', (data))
                if not data or 'endofdata' in str(data):
                    break
                f.write(data)
        if not data:
            break
        f.close()
        indexer = indexer + 1

        print('finished')


port = 1235
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
mysocket.bind((host, port))
mysocket.listen(5)
indexer = 1
while True:
    connection, addr = mysocket.accept()
    print("got connection from", addr[0])
    data = connection.recv(1024)
    print("server recvd", repr(data))
    threading.Thread(target=ClientThread, args=(connection, addr)).start()
