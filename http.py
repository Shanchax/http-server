import os
import sys
import threading 
import datetime
import shutil
from shutil import *
from urllib.parse import *
from datetime import *
from threading import Thread
from socket import *
from config import *
from threading import *
from supplement import*



class http:

    def get(self, conn, url , dictionary , query_string , httpmethod , method_info):
        tcpsocket, file_extension, conn, ip, port, status_code, active_threads = method_info
        build_response = ''
        fileflag = os.path.isfile(url)
        dirflag = os.path.isdir(url)
        readflag = os.access(url, os.R_OK)
        writeflag = os.access(url, os.W_OK)

        if( not(fileflag) and not(dirflag)):
            url.rstrip('/')
        if (fileflag):
            status_code = 200
            build_response += 'HTTP/1.1 200 OK'
            if(readflag):
                if(writeflag):
                    pass
                else :
                    ip, active_threads , status_code = status_handler(conn, 403,[ip, active_threads, status_code])
            else:
                ip, active_threads , status_code = status_handler(conn, 403,[ip, active_threads, status_code])
            size = os.path.getsize(url)
            file = open(url, "rb")
            data = file.read(size)        
        elif (dirflag):
            status_code = 200
            build_response += 'HTTP/1.1 200 OK'
            listofdir = os.listdir(url)
            if(readflag):
                if(writeflag):
                    pass
                else:
                    ip, active_threads , status_code = status_handler(conn, 403,[ip, active_threads, status_code])
            else:
                ip, active_threads , status_code = status_handler(conn, 403,[ip, active_threads, status_code])

            for x in listofdir:
                if x.startswith('.'):
                    listofdir.remove(i)


        for header in dictionary:
            if header == 'User-Agent':
                if(fileflag):
                    build_response += '\r\nServer: ' + ip           
                    DATE = (' ').join(time.ctime().split(' ')) 
                    build_response += '\r\nDate: ' + DATE + '\r\n' + last_modified(url)
                elif(dirflag):
                    build_response += '\r\nServer: ' + ip           
                else:
                    pass
            elif header == 'Host':
                pass
            elif header == 'Accept-Language':
                build_response += '\r\nContent-Language: ' + dictionary[header]
            elif header == 'Accept-Encoding':
                if fileflag:
                    build_response += '\r\nContent-Length: ' + str(size)    
            elif header == 'Connection':  
                if(fileflag):
                    connection_status = True
                    build_response += '\r\nConnection: keep-alive'  
                if(dirflag):
                    connection_status = False
                    build_response += '\r\nConnection: close'
            #elif header == 'If-Modified-Since':
               # if_modify(dictionary[state], entity)
                    
            elif header == 'Accept':
                try:
                 if fileflag :
                     file_ext = os.path.splitext(url)
                     if file_ext[1] in file_extension.keys():
                        build_response += '\r\nContent-Type: ' + file_extension[file_ext[1]]
                     else:
                        build_response += '\r\nContent-Type: ' + 'text/plain'
                except :
                    ip,active_threads,status_code = status_handler(conn, 415, [ip,active_threads,status_code])
        


        if(fileflag):
            build_response += '\r\n\r\n'
            if httpmethod == 'GET':
                response = build_response.encode()
                conn.send(response)
                conn.sendfile(file)
            if httpmethod ='HEAD':
                response = build_response.encode()
                conn.send(response)

        return [tcpsocket, file_extension, conditional_get, conn, ip, serverport, scode, IDENTITY]








                  












                         

            

        









    def delete(self,url, conn, entitydata, dictionary, delete_info):
        ip, port,status_code, active_threads = delete_info
        build_response = ''
        #auth = 'Authorization' in dictionary.keys()
        print("Checking authorization")
        options = url.split('/')
        isdeleteallowed = 'delete' in options
        fileflag =  os.path.isfile(url)
        dirflag  = os.path.isdir(url)
        if(entitydata) > 1 or isdeleteallowed or dirflag :
            status_code = 405
            build_response += 'HTTP/1.1 405 Method Not Allowed' + '\r\nAllow: GET, HEAD, POST, PUT'

        elif(fileflag):
            status_code = 200
            build_response += 'HTTP/1.1 200 OK'
            if (os.access(url, os.W_OK)):
                if (os.access(url, os.R_OK)):
                    #can proceed 
                    pass
                else:
                    ip, active_threads, status_code = status_handler(conn, 403, [ip, active_threads, status_code])
            else:
                ip, active_threads, status_code = status_handler(conn, 403, [ip, active_threads, status_code])
                s_flag = shutil.move(url, DELETE)
            if(s_flag == shutil.Error):
                os.remove(url)

        else :
            status_code = 400        
            build_response += 'HTTP/1.1 400 Bad Request'
        build_response += '\r\nServer: ' + ip  + '\r\nConnection: keep-alive' + '\r\n' + date() + '\r\n\r\n'
        response = build_response.encode()
        conn.send(response)
        return [ip, port , status_code] 



httpserver = http()





















def request_handler(conn, addr , start,reqinfo):
    
    tcpsocket, file_extension, connection_status, SIZE, active_threads, status_code, ip,port = reqinfo
    utf_flag = 0
    for _ in iter(int, 1):
        request = conn.receive(SIZE)
        try :
            request = request.decode('utf-8')
            request_split = request.split('\r\n\r\n')
        except (UnicodeDecodeError):
            utf_flag = 1
            req_split = request.split(b'\r\n\r\n')
            req_split[0] = req_split[0].decode(errors = 'ignore')    #the requestline ex GET ....url ..... HTTP 1.1
        #seperatinf status line and header lines from entity body 
        #STATUS LINE
        #HEADER LINE
        #crlfcrlf  we split here
        #entitybody
        if len(req_split) == 1 or not(len(req_split >1)):
            status_handler(conn, 505, [ip, active_threads, status_code])
        entitydata = req_split[1]
        reqlineandheader = req_split.split('\r\n')
        reqline = reqlineandheader[0].split('')
        httpmethod = reqline[0]
        url = reqline[1]
        httpversion = reqline[2]
        if(len(url) > MAX_URL):
            status_handler(conn, 414, [ip, active_threads, status_code])
            conn.close
        else:
            print('url lenght is admissible, can proceed')
            pass
        if(url == '/'):
            url = os.getcwd()
        url,query_string = breakdown(url) #here url is actually just a path
        if(len(url) > MAX_URL):
            status_handler(conn, 414, [ip, active_threads, status_code])
            conn.close()
        
        
        version_num = httpversion.split('/')[1]    
        if not(version_num == '1.1'):
            status_handler (conn , 505 , [ip, active_threads, status_code])
            print("Please enter a valid version_num")

        request_line = reqlineandheader.pop(0)
        i = 0
        dictionary = {}
        while i < len(reqlineandheader):
            headers = reqlineandheader[i]
            list = headers.split(': ')
            dictionary[list[0]] = list[1]
            i = i+1

        method_info = [tcpsocket, file_extension, conn, ip, port, status_code, active_threads]    
        
        if(httpmethod =='GET') or (httpmethod == 'HEAD'):
            recv = httpserver.get(conn, url , dictionary , query_string , httpmethod , method_info)


        elif (httpmethod == 'POST'):
            recv = httpserver.post(entitydata, conn, dictionary [ip,port, status_code])


        elif(httpmethod == 'PUT'):
            file = b""
            recv = httpserver.put(conn, addr, entitydata, file , url, dictionary, utf_flag, status_code, [ip, active_threads, status_code])
        elif(httpmethod == 'DELETE'):
            glob = httpserver.delete(url, conn, entitydata, dictionary, [ip,port, status_code, active_threads])
        else:
             print("No method implemented")   

             status_handler(conn, 505 , [ ip, active_threads, status_code])

        conn.close()
        active_threads.remove(conn)







                




        
        

        


    







''' 
Status_handler : handles status codes of the form 4xx and 5xx that lead 
to unsuccessful actions. FInally, close the connection and remove thread from
active threads list
'''
def status_handler(conn, scode, temp):
    ip, active_threads, status_code = temp
    status_code = scode
    response = ''
    if(scode == 415 or scode):
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
    return [ip, active_threads , scode]

    





    


    


def server(server_info):
    tcpsocket, file_extension, connection_status, SIZE, active_threads, status_code, ip, port = server_info
    for _ in iter(int, 1):
        conn, addr = tcpsocket.accept() # connectionsocket = request, addr = port,ip
        start = 0
        active_threads.append(conn)  # add connections
        if not (len(active_threads) < 20): #at a time server can handle at most 20 threads
            temp = [ip, active_threads, status_code]
            status_handler(conn, 503, temp)
            conn.close() #closing the connection not the socket
        else:
            reqinfo = [tcpsocket, file_extension, conn, SIZE, active_threads, status_code, ip,port]
            new_thread = Thread(request_handler, (conn, addr, start,reqinfo ))
            new_thread.start()

    tcpsocket.close()





if __name__ =='__main__':
    ip = '127.0.0.1'
    status_code = 0
    month = MONTH
    file_type = FORMAT2
    file_extension = FORMAT
    connection_status = True
    active_threads = []
    tcpsocket = socket(AF_INET, SOCK_STREAM)
    port = int(sys.argv[1])
    tcpsocket.bind(('', port))
    tcpsocket.listen(5)
    server_info = [tcpsocket, file_extension,connection_status, SIZE, active_threads, status_code, ip, port]
    server(server_info)
    sys.exit()




