import os
import sys
import threading 
import datetime
from datetime import *
from threading import Thread
import socket
from socket import *
from config import *
from threading import *


"""using the concept of 501_handler in prevous code to 
create a handler for status codes related to forbidden, etc ."""
def status_handler(conn, scode, temp):
    ip, client_thread, status_code = temp
    status_code = scode
    response = ''
    if(scode == 415):
        response += 'HTTP/1.1 {} Unsupported Media Type'.format(scode)
    elif(scode == 404):
        response += 'HTTP/1.1 {} Not founf'.format(scode)
    elif(scode == 414):
        response += 'HTTP/1.1 {} uri exceeds permissible length'.format(scode)
    elif(scode == 503):
        response += 'HTTP/1.1 {} server is busy ie thread limit reached'.format(scode)
    elif(scode == 505):
        response += 'HTTP/1.1 {} version not supported'.format(scode)    

    elif(scode == 501):
        response += 'HTTP/1.1 {} method not implemented'

    response = '\r\nServer: ' + ip + '\r\n' + TODAY + '\r\n\r\n'
    conn.send(response.encode())
    active_threads.remove(conn) 
    conn.close()
    server(server_info)
    return [ip, client_thread, scode]



    


    


def server(server_info):
    socket, file_extension, connection_status, SIZE, active_threads, status_code, ip, port = server_info
    for _ in iter(int, 1):
        conn, addr = socket.accept() # connectionsocket = request, addr = port,ip
        start = 0
        active_threads.append(conn)  # add connections
        if not (len(active_threads) < 20): #at a time server can handle at most 20 threads
            temp = [ip, active_threads, status_code]
            status_handler(conn, 503, temp)
            conn.close() #closing the connection not the socket
        else:
            temp2 = [socket, file_extension, conn, SIZE, active_threads, status_code, ip,port]
            new_thread = Thread(bridgeFunction, (conn, addr, start,temp2 ))
            new_thread.start()

    socket.close()





if __name__ =='__main__':
    ip = '127.0.0.1'
    status_code = 0
    month = MONTH
    file_type = FORMAT2
    file_extension = FORMAT
    connection_status = True
    active_threads = []
    socket = socket(AF_INET, SOCK_STREAM)
    port = int(sys.argv[1])
    socket.bind(('', port))
    socket.listen(5)
    server_info = [socket, file_extension,connection_status, SIZE, active_threads, status_code, ip, port]
    server(server_info)
    sys.exit()




