from socket import *
import datetime 
import os
import time
import random
import threading
from _thread import *
import shutil		            		 # to implement delete method
import csv          					 # used in put and post method to insert data
import base64		            		 # used for decoding autherization header in delete method
import sys
import logging
<<<<<<< HEAD
=======
from tkinter.constants import X
>>>>>>> 40cde4bd6fe98f9f5ed89c3a2f9e22400bdd7e5b
from config import *                    # import variables
import signal   
from urllib.parse import *	 # for parsing URL/URI
import os
<<<<<<< HEAD
import time    
import httpfinal
from httpfinal import *




=======
import time                        # signal to handle Ctrl+C and other SIGNALS

SIZE = 8192 

class http_methods:

    def GET_HEAD(self,tcpconnection, url, headers_dict, query, method, arg_list):
        tcpsocket, f_x, cget_flag, connection_status, ip, portnum, status_code, cookie_id, activethreads = arg_list
        isItFile = os.path.isfile(url)
        isItDir = os.path.isdir(url)
        build_response = ''
        if isItFile:
            build_response += 'HTTP/1.1 200 OK'
            status_code = 200
            if (os.access(url, os.R_OK)):
                if (os.access(url, os.W_OK)):
                    pass
            else:
                glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                ip, activethreads, status_code = glob
            try:
                size = os.path.getsize(url)
                f = open(url, "rb")
                data = f.read(size)
            except:
                glob = status_hanlder(tcpconnection, 500, [ip, activethreads, status_code])
                ip, activethreads, status_code = glob
        elif isItDir:
            dir_list = os.listdir(url)
            build_response += 'HTTP/1.1 200 OK'
            status_code = 200
            # if it is a directory
            if os.access(url, os.R_OK):
                if (os.access(url, os.W_OK)):
                    pass
                else:
                    glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                    ip, activethreads, status_code = glob
            else:
                glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                ip, activethreads, status_code = glob
            for i in dir_list:
                if i.startswith('.'):
                    dir_list.remove(i)
                else:
                    pass
        
        build_response += '\r\n' + 'Set-Cookie: id=' + str(cookie_id) + MAXAGE
        cookie_id += random.randint(1,10)
        for header in headers_dict:
            if header == 'User-Agent':
                if isItDir:
                    build_response += '\r\nServer: ' + ip
                elif isItFile:
                    l = time.ctime().split(' ')
                    l[0] = l[0] + ','
                    build_response += '\r\nServer: ' + ip
                    build_response += '\r\nDate: ' + (' ').join(l)
                    build_response += '\r\n' + last_modified(url)
                else:
                    pass
            elif header == 'Host':
                pass
            elif header == 'Accept':
                if isItFile:
                    try:
                        file_ext = os.path.splitext(url)
                        if file_ext[1] in f_x.keys():
                            req_temp = f_x[file_ext[1]]
                            temp = 0
                        else:
                            req_temp = 'text/plain'
                            temp = 1
                        req_temp = '\r\nContent-Type: '+ req_temp
                        build_response += req_temp
                    except:
                        glob = status_hanlder(tcpconnection, 415, [ip, activethreads, status_code])
                        ip, activethreads, status_code = glob
                        # status_code = 415
                elif isItDir:
                    req_temp = '\r\nContent-Type: text/html'
                    build_response += req_temp
                else:
                    pass
            
            elif header == 'Accept-Encoding':
                if isItFile:
                    req_temp = '\r\nContent-Length: ' + str(size)
                    build_response += req_temp
                else:
                    pass


            elif header == 'Connection':
                if isItFile:
                    connection_status = True
                    build_response += '\r\nConnection: keep-alive'
                elif isItDir:
                    connection_status = False
                    build_response += '\r\nConnection: close'
                else:
                    pass
            elif header == 'If-Modified-Since':
                if_modify(headers_dict[header], url)
            
>>>>>>> 40cde4bd6fe98f9f5ed89c3a2f9e22400bdd7e5b

            elif header == 'Accept-Language':
                req_temp = '\r\nContent-Language: ' + headers_dict[header]
                build_response += req_temp

<<<<<<< HEAD









class http_methods:

    def response_get_head(self,connectionsocket, entity, switcher, query, method, glob):
        serversocket, file_extension, conditional_get, conn, ip, serverport, scode, IDENTITY, client_thread = glob
        isItFile = os.path.isfile(entity)
        isItDir = os.path.isdir(entity)
        show_response = ''
        if isItFile:
            show_response += 'HTTP/1.1 200 OK'
            scode = 200
            if (os.access(entity, os.R_OK)):
                if (os.access(entity, os.W_OK)):
                    pass
                else:
                    glob = status(connectionsocket, 403,[ip, client_thread, scode])
                    ip, client_thread, scode = glob
            else:
                glob = status(connectionsocket, 403, [ip, client_thread, scode])
                ip, client_thread, scode = glob
            try:
                size = os.path.getsize(entity)
                f = open(entity, "rb")
                data = f.read(size)
            except:
                glob = status(connectionsocket, 500, [ip, client_thread, scode])
                ip, client_thread, scode = glob
        elif isItDir:
            dir_list = os.listdir(entity)
            show_response += 'HTTP/1.1 200 OK'
            scode = 200
            # if it is a directory
            if os.access(entity, os.R_OK):
                if (os.access(entity, os.W_OK)):
                    pass
                else:
                    glob = status(connectionsocket, 403, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
            else:
                glob = status(connectionsocket, 403, [ip, client_thread, scode])
                ip, client_thread, scode = glob
            for i in dir_list:
                if i.startswith('.'):
                    dir_list.remove(i)
                else:
                    pass
        else:
            entity = entity.rstrip('/')
            isItDir = os.path.isdir(entity)
            isItFile = os.path.isfile(entity)
            if isItDir:
                scode = 200
                show_response += 'HTTP/1.1 200 OK'
                dir_list = os.listdir(entity)
                entity = entity.rstrip('/')
                if (os.access(entity, os.W_OK)):
                    if (os.access(entity, os.R_OK)):
                        pass
                    else:
                        glob = status(connectionsocket, 403, [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                else:
                    glob = status(connectionsocket, 403, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                for i in dir_list:
                    if i.startswith('.'):
                        dir_list.remove(i)
                    else:
                        pass
            elif isItFile:
                show_response += 'HTTP/1.1 200 OK'
                scode = 200
                if (os.access(entity, os.R_OK)):
                    if (os.access(entity, os.W_OK)):
                        pass
                else:
                    glob = status(connectionsocket, 403,[ip, client_thread, scode])
                    ip, client_thread, scode = glob
                try:
                    size = os.path.getsize(entity)
                    f = open(entity, "rb")
                    data = f.read(size)
                except:
                    # error while accesing the file
                    glob = status(connectionsocket, 500, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
            else:	
                glob = status(connectionsocket, 404, [ip, client_thread, scode])
                ip, client_thread, scode = glob
        show_response += '\r\n' + COOKIE + str(IDENTITY) + MAXAGE
        IDENTITY += random.randint(1,10)
        for state in switcher:
            if state == 'User-Agent':
                if isItDir:
                    show_response += '\r\nServer: ' + ip
                elif isItFile:
                    l = time.ctime().split(' ')
                    l[0] = l[0] + ','
                    conversation = (' ').join(l)
                    show_response += '\r\nServer: ' + ip
                    conversation = '\r\nDate: ' + conversation
                    show_response += conversation
                    show_response += '\r\n' + last_modified(entity)
                else:
                    pass
            elif state == 'Host':
                pass
            elif state == 'Accept':
                if isItFile:
                    try:
                        file_ext = os.path.splitext(entity)
                        if file_ext[1] in file_extension.keys():
                            conversation = file_extension[file_ext[1]]
                            temp = 0
                        else:
                            conversation = 'text/plain'
                            temp = 1
                        conversation = '\r\nContent-Type: '+ conversation
                        show_response += conversation
                    except:
                        glob = status(connectionsocket, 415, [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                        # scode = 415
                elif isItDir:
                    conversation = '\r\nContent-Type: text/html'
                    show_response += conversation
                else:
                    pass
            elif state == 'Accept-Language':
                conversation = '\r\nContent-Language: ' + switcher[state]
                show_response += conversation
            elif state == 'Accept-Encoding':
                if isItFile:
                    conversation = '\r\nContent-Length: ' + str(size)
                    show_response += conversation
                else:
                    pass
            elif state == 'Connection':
                if isItFile:
                    conn = True
                    show_response += '\r\nConnection: keep-alive'
                elif isItDir:
                    conn = False
                    show_response += '\r\nConnection: close'
                else:
                    pass
            elif state == 'If-Modified-Since':
                if_modify(switcher[state], entity)
            else:
                continue
        if isItDir and method == 'GET':
            show_response += '\r\n\r\n'
            show_response += '\r\n<!DOCTYPE html>'
            show_response += '\r\n<html>\n<head>'
            show_response += '\r\n<title>Directory listing</title>'
            show_response += '\r\n<meta http-equiv="Content-type" content="text/html;charset=UTF-8" /></head>'
            show_response += '\r\n<body><h1>Directory listing..</h1><ul>'
            for line in dir_list:
                if entity == '/':
                    link = 'http://' + ip + ':' + str(serverport) + entity + line
                    l = '\r\n<li><a href ="'+link+'">'+line+'</a></li>'
                    show_response += l
                else:
                    link = 'http://' + ip + ':' + str(serverport) + entity + '/'+ line
                    l = '\r\n<li><a href ="'+link+'">'+line+'</a></li>'
                    show_response += l
            show_response += '\r\n</ul></body></html>'
            encoded = show_response.encode()
            connectionsocket.send(encoded)
            connectionsocket.close()
        elif len(query) > 0 and not isItFile and not isItDir:
            show_response = ''
            row = ''
            entity = CSVFILE
            fields = ''
            for d in query:
                fields += d + ','
                for i in query[d]:
                    row += i + ','
            file_exists = os.path.exists(entity)
            if file_exists:
                scode = 200
                show_response += 'HTTP/1.1 200 OK'
                fi = open(entity, "a")
                row = list(row.split(",")) 
                csvwriter = csv.writer(fi)
                csvwriter.writerow(row)
            else:
                fi = open(entity, "w")
                show_response += 'HTTP/1.1 201 Created'
                scode = 201
                show_response.append('Location: ' + entity)
                csvwriter = csv.writer(fi)
                csvwriter.writerow(fields)
                csvwriter.writerow(row)
            fi.close()
            show_response += '\r\nServer: ' + ip
            show_response += '\r\n'+ date()
            f = open(WORKFILE, "rb")
            show_response += '\r\nContent-Language: en-US,en'
            size = os.path.getsize(WORKFILE)
            conversation = '\r\nContent-Length: ' + str(size)
            show_response += '\r\nContent-Type: text/html'
            show_response += conversation
            show_response += '\r\n' +last_modified(entity)
            show_response += '\r\n\r\n'
            encoded = show_response.encode()
            connectionsocket.send(encoded)
            connectionsocket.sendfile(f)
        elif isItFile:
            show_response += '\r\n\r\n'
            if conditional_get == False and method == 'GET':
                encoded = show_response.encode()
                connectionsocket.send(encoded)
                connectionsocket.sendfile(f)
            elif conditional_get == False and method == 'HEAD':
                encoded = show_response.encode()
                connectionsocket.send(encoded)
            elif conditional_get == True and (method == 'GET' or method == 'HEAD'):
                status_304(connectionsocket, entity, [ip, scode])
        else:
            glob = status(connectionsocket, 400, [ip, client_thread, scode])
            ip, client_thread, scode = glob
        return [serversocket, file_extension, conditional_get, conn, ip, serverport, scode, IDENTITY]
        
    def response_post(self,ent_body, connectionsocket, switcher, glob):
        ip, serverport,scode = glob
        show_response = ''
        entity = CSVFILE
        query = parse_qs(ent_body)
        if os.access(entity, os.W_OK):
            pass
        else:
            status(connectionsocket, 403, [ip, client_thread, scode])
        fields = ''
        row = ''
        for d in query:
            fields += d + ', '
            for i in query[d]:
                row += i + ', '
        file_exists = os.path.exists(entity)
        if file_exists:
            fi = open(entity, "a")
            show_response += 'HTTP/1.1 200 OK'
            scode = 200
            csvwriter = csv.writer(fi)
            csvwriter.writerow(row)
        else:
            fi = open(entity, "w")
            show_response += 'HTTP/1.1 201 Created'
            scode = 201
            show_response += '\r\nLocation: ' + entity
            csvwriter = csv.writer(fi)
            csvwriter.writerow(fields)
            csvwriter.writerow(row)
        fi.close()
        show_response += '\r\nServer: ' + ip
        show_response += date()
        f = open(WORKFILE, "rb")
        show_response += '\r\nContent-Language: en-US,en'
        size = os.path.getsize(WORKFILE)
        conversation = 'Content-Length: ' + str(size)
        show_response += '\r\nContent-Type: text/html'
        show_response += '\r\n' + conversation
        show_response += '\r\n' + last_modified(entity)
        show_response += '\r\n\r\n'
        encoded = show_response.encode()
        connectionsocket.send(encoded)
        connectionsocket.sendfile(f)
        return [ip, serverport, scode]

    def response_put(self,connectionsocket, addr, ent_body, filedata, entity, switcher, f_flag, scode, glob):
        ip, client_thread, scode = glob
        try:
            length = int(switcher['Content-Length'])
        except:
            scode = 411
            glob = status(connectionsocket, 411, [ip, client_thread, scode])
            ip, client_thread, scode = glob
        show_response = ''
        try:
            filedata = filedata + ent_body
        except TypeError:
            ent_body = ent_body.encode()
            filedata = filedata + ent_body
        isItFile = os.path.isfile(entity)
        isItDir = os.path.isdir(entity)
        i = len(ent_body)
        size = length - i
        # r = length % SIZE
        # q = int(length // SIZE)
        # isItDir = os.path.isdir(entity)
        # isItFile = os.path.isdir(entity)
        for _ in iter(int, 1):
            if not size > 0:
                break
            ent_body = connectionsocket.recv(SIZE)
            try:
                filedata = filedata + ent_body
            except:
                ent_body = ent_body.encode()
                print("encoding...")
                filedata = filedata + ent_body
            size -= len(ent_body)
        mode_f, r_201, move_p = True, False, False
        limit = len(ROOT)
        l = len(entity)
        if not l < limit:
            if isItFile:
                if os.access(entity, os.W_OK):
                    # no need for read access
                    if os.access(entity, os.R_OK):
                        pass
                    else:
                        pass
                else:
                    glob = status(connectionsocket, 403, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                # writing File mode ON
                mode_f = True
                if f_flag == 1:
                    f = open(entity, "wb")
                    f.write(filedata)                    
                elif f_flag == 0:	
                    f = open(entity, "w")
                    f.write(filedata.decode())
                else:
                    f = open(entity, "wb")
                    f.write(filedata)
                f.close()
            elif isItDir:
                move_p = True
                loc = ROOT + '/' + str(addr[1])
                if os.access(entity, os.W_OK):
                    # no need for read access
                    if os.access(entity, os.R_OK):
                        pass
                    else:
                        pass
                else:
                    glob = status(connectionsocket, 403, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                try:
                    loc = loc + file_type[switcher['Content-Type'].split(';')[0]]
                except:
                    glob = status(connectionsocket, 403, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                if f_flag == 1:
                    f = open(loc, "wb")
                    f.write(filedata)                    
                elif f_flag == 0:	
                    f = open(loc, "w")
                    f.write(filedata.decode())
                else:
                    f = open(loc, "wb")
                    f.write(filedata)
                f.close()
            
            else:
                if ROOT in entity:
                    entity = ROOT + '/' + str(addr[1])
                    try:
                        entity = entity + file_type[switcher['Content-Type'].split(';')[0]]
                    except:
                        # error in header
                        glob = status(connectionsocket, 403, [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                    if f_flag:
                        f = open(entity, "wb")
                        f.write(filedata)                        
                    elif f_flag == 0:	
                        # open the file in write mode
                        f = open(entity, "w")
                        f.write(filedata.decode())
                    else:
                        # open the file in write binary mode
                        f = open(entity, "wb")
                        f.write(filedata)
                    f.close()
                    r_201 = True
                else:
                    mode_f = False
        else:
            move_p = True
            loc = ROOT + '/' + str(addr[1])
            try:
                loc = loc + file_type[switcher['Content-Type']]
            except:
                glob = status(connectionsocket, 403, [ip, client_thread, scode])
                ip, client_thread, scode = glob
            if f_flag == 0:	
                f = open(loc, "w")
            else:
                f = open(loc, "wb")
            f.write(filedata)
            f.close()
        if move_p:
            scode = 301
            show_response += 'HTTP/1.1 301 Moved Permanently'
            show_response += '\r\nLocation: ' + loc
        elif mode_f:
            scode = 204
            show_response += 'HTTP/1.1 204 No Content'
            show_response += '\r\n\Content-Location: ' + entity
        elif r_201:
            scode = 201
            show_response += 'HTTP/1.1 201 Created'
            show_response += '\r\nContent-Location: ' + entity
        elif not mode_f:
            scode = 501
            show_response += 'HTTP/1.1 501 Not Implemented'
        show_response += '\r\nConnection: keep-alive'
        show_response += '\r\n\r\n'
        encoded = show_response.encode()
        connectionsocket.send(encoded)
        connectionsocket.close()
        return None

    def response_delete(self,entity, connectionsocket, ent_body, switcher, glob):
        ip, serverport,scode, client_thread = glob
        isItDir = os.path.isdir(entity)
        isItFile = os.path.isfile(entity)
        # print(f"deleting {entity} ")
        # print(isItFile)
        option_list = entity.split('/')
        show_response = ''
        if 'Authorization' in switcher.keys():
            conversation = switcher['Authorization']
            # print("Auth process started:")
            if conversation:
                conversation = conversation.split(' ')
                conversation = base64.decodebytes(conversation[1].encode()).decode()
                conversation = conversation.split(':')
            else:
                scode = 401
                show_response += 'HTTP/1.1 401 Unauthorized'
                show_response += '\r\nWWW-Authenticate: Basic'
                show_response += '\r\n\r\n'
                encoded = show_response.encode()
                connectionsocket.send(encoded)
                return [ip, serverport, scode]


            if conversation[0] == USERNAME:
                if conversation[1] == PASSWORD:
                    pass
                else:
                    scode = 401
                    show_response += 'HTTP/1.1 401 Unauthorized'
                    show_response += '\r\nWWW-Authenticate: Basic'
                    show_response += '\r\n\r\n'
                    encoded = show_response.encode()
                    connectionsocket.send(encoded)
                    return [ip, serverport, scode]
            else:
                scode = 401
                show_response += 'HTTP/1.1 401 Unauthorized'
                show_response += '\r\nWWW-Authenticate: Basic'
                show_response += '\r\n\r\n'
                encoded = show_response.encode()
                connectionsocket.send(encoded)
                return [ip, serverport, scode]
        else:
            scode = 401
            show_response += 'HTTP/1.1 401 Unauthorized'
            show_response += '\r\nWWW-Authenticate: Basic'
            show_response += '\r\n\r\n'
            encoded = show_response.encode()
            connectionsocket.send(encoded)
            return [ip, serverport, scode]
        if len(ent_body) > 1 or 'delete' in option_list or isItDir:
            scode = 405
            show_response += 'HTTP/1.1 405 Method Not Allowed'
            show_response += '\r\nAllow: GET, HEAD, POST, PUT'
        elif isItFile:
            scode = 200
            show_response += 'HTTP/1.1 200 OK'
            try:
                if (os.access(entity, os.W_OK)):
                    if (os.access(entity, os.R_OK)):
                        pass
                    else:
                        glob = status(connectionsocket, 403, [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                else:
                    glob = status(connectionsocket, 403, [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                shutil.move(entity, DELETE)
            except shutil.Error:
                os.remove(entity)
        else:
            scode = 400
            show_response += 'HTTP/1.1 400 Bad Request'
        show_response += '\r\nServer: ' + ip
        show_response += '\r\nConnection: keep-alive'
        show_response += '\r\n' + date()
        show_response += '\r\n\r\n'
        encoded = show_response.encode()
        connectionsocket.send(encoded)
        return [ip, serverport, scode]
=======
            else:
                continue

        if isItDir and method == 'GET':
            build_response += '\r\n\r\n'
            build_response += '\r\n<!DOCTYPE html>'
            build_response += '\r\n<html>\n<head>'
            build_response += '\r\n<title>Directory listing</title>'
            build_response += '\r\n<meta http-equiv="Content-type" content="text/html;charset=UTF-8" /></head>'
            build_response += '\r\n<body><h1>Directory listing..</h1><ul>'
            for line in dir_list:
                if url == '/':
                    link = 'http://' + ip + ':' + str(portnum) + url + line
                    l = '\r\n<li><a href ="'+link+'">'+line+'</a></li>'
                    build_response += l
                else:
                    link = 'http://' + ip + ':' + str(portnum) + url + '/'+ line
                    l = '\r\n<li><a href ="'+link+'">'+line+'</a></li>'
                    build_response += l
            build_response += '\r\n</ul></body></html>'
            encoded = build_response.encode()
            tcpconnection.send(encoded)
            tcpconnection.close()
        elif len(query) > 0 and not isItFile and not isItDir:
            build_response = ''
            row = ''
            url = CSVFILE
            fields = ''
            for d in query:
                fields += d + ','
                for i in query[d]:
                    row += i + ','
            file_exists = os.path.exists(url)
            if file_exists:
                status_code = 200
                build_response += 'HTTP/1.1 200 OK'
                fi = open(url, "a")
                row = list(row.split(",")) 
                csvwriter = csv.writer(fi)
                csvwriter.writerow(row)
            else:
                fi = open(url, "w")
                build_response += 'HTTP/1.1 201 Created'
                status_code = 201
                build_response.append('Location: ' + url)
                csvwriter = csv.writer(fi)
                csvwriter.writerow(fields)
                csvwriter.writerow(row)
            fi.close()
            build_response += '\r\nServer: ' + ip + '\r\n'+ date()
            f = open(WORKFILE, "rb")
            build_response += '\r\nContent-Language: en-US,en'
            size = os.path.getsize(WORKFILE)
            req_temp = '\r\nContent-Length: ' + str(size)
            build_response += '\r\nContent-Type: text/html'
            build_response += req_temp + '\r\n' +last_modified(url) + '\r\n\r\n'
            encoded = build_response.encode()
            tcpconnection.send(encoded)
            tcpconnection.sendfile(f)
        elif isItFile:
            build_response += '\r\n\r\n'
            if cget_flag == False and method == 'GET':
                encoded = build_response.encode()
                tcpconnection.send(encoded)
                tcpconnection.sendfile(f)
            elif cget_flag == False and method == 'HEAD':
                encoded = build_response.encode()
                tcpconnection.send(encoded)
            elif cget_flag == True and (method == 'GET' or method == 'HEAD'):
                status_304(tcpconnection, url, [ip, status_code])
        else:
            gl = status_hanlder(tcpconnection, 400, [ip, activethreads, status_code])
            ip, activethreads, status_code = gl
        return [tcpsocket, f_x, cget_flag, connection_status, ip, portnum, status_code, cookie_id]
        
    def POST(self,ent_body, tcpconnection, headers_dict, arg_list):
        ip, portnum,status_code = arg_list
        build_response = ''
        url = os.getcwd() + '/post.txt'
        #query_string = parse_qs(ent_body)
        if (not(os.access(url, os.W_OK))):
            status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
        print("No, I'm here")

        if os.path.isfile(url):
            fi = open(url, "a")
            status_code = 200
            build_response += 'HTTP/1.1 {} OK'.format(status_code)
            fi.write(ent_body)
            fi.close()
            print("I'm here")
        else:
            print("creating file")
            fi = open(url, "a")
            status_code = 201
            build_response += 'HTTP/1.1 {} Created'.format(status_code)
            
            build_response += '\r\nLocation: ' + url
            fi.write(ent_body)
            fi.close()
        
        build_response += '\r\nServer: ' + ip
        build_response += date()
        f = open(WORKFILE, "rb")
        size = os.path.getsize(WORKFILE)
        build_response += '\r\nContent-Language: en-US,en' + '\r\nContent-Type: text/html'+ '\r\n' + 'Content-Length: ' + str(size) + '\r\n' + last_modified(url) + '\r\n\r\n'+                                                 
        response = build_response.encode()
        print(build_response)
        tcpconnection.send(response)
        tcpconnection.sendfile(f)
        return [ip, portnum, status_code]

    
    def DELETE(self,url, tcpconnection, ent_body, headers_dict, arg_list):
        ip, portnum,status_code, activethreads = arg_list
        isItDir = os.path.isdir(url)
        isItFile = os.path.isfile(url)
        print(f"deleting {url} ")
        # print(isItFile)
        options= url.split('/')
        build_response = ''
        '''
        if  not('DELETE' in options) 
            status_code = 405
            build_response += 'HTTP/1.1 405 Method Not Allowed'
            build_response += '\r\nAllow: GET, HEAD, POST, PUT'
        '''    
        if isItFile:
            status_code = 200
            build_response += 'HTTP/1.1 200 OK'
            try:
                if (os.access(url, os.W_OK)):
                    if (os.access(url, os.R_OK)):
                        pass
                    else:
                        glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                        ip, activethreads, status_code = glob
                else:
                    glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                    ip, activethreads, status_code = glob
                shutil.move(url, DELETE)
            except shutil.Error:
                os.remove(url)
        else:
            status_code = 400
            build_response += 'HTTP/1.1 400 Bad Request'
        build_response += '\r\nServer: ' + ip
        build_response += '\r\nConnection: keep-alive'
        build_response += '\r\n' + date()
        build_response += '\r\n\r\n'
        encoded = build_response.encode()
        tcpconnection.send(encoded)
        return [ip, portnum, status_code]

httpserver = http_methods()

#function to check if the resource has been modified or not since the date in HTTP request 
def if_modify(state, url):
    global cget_flag, month
    valid = False
    day = state.split(' ')
    if len(day) == 5:
        valid = True
    if valid:
        m = month[day[1]]
        date = int(day[2])
        t = day[3].split(':')
        t[0], t[1], t[2] = int(t[0]), int(t[1]), int(t[2])
        y = int(day[4])
        ti = datetime.datetime(y, m, date, t[0], t[1], t[2])
        hsec = int(time.mktime(ti.timetuple()))
        fsec = int(os.path.getmtime(url))
        if hsec == fsec:
            cget_flag = True
        elif hsec < fsec:
            cget_flag = False
    return cget_flag

#function to return current date
def date():
    #  Sun, 06 Nov 1994 08:49:37 GMT  ; RFC 822, updated by RFC 1123
    now = datetime.datetime.now()
    datenow = now.strftime('%A,%d %B %Y %H:%M:%S ')
    datenow += "GMT"
    datestring = 'Date: ' + datenow
    return datestring

#function to give response if server is busy
def status_hanlder(tcpconnection, code, arg_list):
    ip, activethreads, status_code = arg_list
    status_code = code
    build_response = ''
    if (code == '505') or (code == 505):
        build_response += 'HTTP/1.1 505 HTTP version not supported'
    elif (code == '415') or (code == 415):
        build_response += 'HTTP/1.1 415 Unsupported Media Type'
    elif (code == '403') or (code == 403):
        build_response += 'HTTP/1.1 403 Forbidden'
    elif (code == '404') or (code == 404):
        build_response += 'HTTP/1.1 404 Not Found'
    elif (code == '414') or (code == 414):
        build_response += 'HTTP/1.1 414 Request-URI Too Long'
    elif (code == '500') or (code == 500):
        build_response += 'HTTP/1.1 500 Internal Server Error'
    elif (code == '503') or (code == 503):
        build_response += 'HTTP/1.1 503 Server Unavailable'
    elif (code == '411') or (code == 411):
        build_response += 'HTTP/1.1 411 length required'

    build_response += '\r\nServer: ' + ip
    build_response += '\r\n' + date()
    build_response += '\r\n\r\n'
    if code == 505:
        build_response += '\r\nSupported Version - HTTP/1.1 \n Rest Unsupported'
    encoded = build_response.encode()
    tcpconnection.send(encoded)
    logging.info('	{}	{}\n'.format(tcpconnection, status_code))
    try:
        activethreads.remove(tcpconnection)
        tcpconnection.close()
    except:
        pass
    server_runner([tcpsocket, f_x, cget_flag, connection_status, SIZE, activethreads, status_code, ip, cookie_id, portnum])
    return [ip, activethreads, status_code]


#function for conditional get implementation
def status_304(tcpconnection, url, arg_list):
    ip, status_code = arg_list
    status_code = 304
    build_response = ''
    build_response += 'HTTP/1.1 304 Not Modified' + '\r\n' + date() + '\r\n' + last_modified(url) + '\r\nServer: ' + ip + '\r\n\r\n'
    response = build_response.encode()
    tcpconnection.send(response)


#function which operates between response and requests
def request_handler(tcpconnection, addr, start, glob):
    tcpsocket, f_x, cget_flag, conn, SIZE, activethreads, status_code, ip, cookie_id, portnum = glob
    cget_flag = False
    urlflag = 0
    f_flag = 0
    filedata = b""
    connection_status = True
    for _ in iter(int, 1):
        if not connection_status:
            # print("Connection not established")
            break
        if SIZE > 0:
            pass
        else:
            break
        try:
            message = tcpconnection.recv(SIZE)
            print(message)
        except OSError:
            message = tcpconnection.recv(SIZE)
        try:
            f_flag = 0
            message = message.decode('utf-8')
            req_list = message.split('\r\n\r\n')
            # print(req_list)
        except UnicodeDecodeError:
            f_flag = 1
            # if you're using non UTF-8 chars
            req_list = message.split(b'\r\n\r\n')
            req_list[0] = req_list[0].decode(errors = 'ignore')
            # print(req_list)
        if len(req_list) == 1:
            status_hanlder(tcpconnection, 505, [ip, activethreads, status_code])
            print("\nBlank line expected at the end\n")
            break
        elif len(req_list) > 1:
            # every line ends with a \r\n so for only headers it'll create ['req', '']
            pass
        else:
            status_hanlder(tcpconnection, 505, [ip, activethreads, status_code])
            print("Error in headers\n")
            break
        try:
            LOG.write(((addr[0]) + '\n' + req_list[0] + '\n\n'))
        except:
            pass
        # build_response = ''
        # header_len = len(header_list)
        ent_body = req_list[1]
        header_list = req_list[0].split('\r\n')
        request_line = header_list[0].split(' ')
        if len(req_list) < 2:
            status_hanlder(tcpconnection, 505, [ip, activethreads, status_code])
        else:
            pass
        url = request_line[1]
        method = request_line[0]
        if url == '/':
            url = os.getcwd()
        #elif (url == favicon) or (url == 'favicon') or (url == 'favicon.ico'):
        #    url = FAVICON
        url, query = urlbreak(url)
        if (len(url) > MAX_URL and urlflag == 0):
            status_hanlder(tcpconnection, 414, [ip, activethreads, status_code])
            tcpconnection.close()
            break
        elif len(url) <= MAX_URL:
            # print("working Fine")
            urlflag = 1
            pass
        else:
            urlflag = 1
        version = request_line[2]
        try:
            version_num = version.split('/')[1]
            if (version_num == RUNNING_VERSION):
                # print("using HTTP 1.1")
                pass
            elif not (version_num == RUNNING_VERSION):
                status_hanlder(tcpconnection, 505, [ip, activethreads, status_code])
        except IndexError:
            # print("EXPECTED HTTP version number")
            status_hanlder(tcpconnection, 505, [ip, activethreads, status_code])
        request_line = header_list.pop(0)
        headers_dict = {}
        i = 0
        while i < len(header_list):
            line = header_list[i]
            line_list = line.split(': ')
            headers_dict[line_list[0]] = line_list[1]
            i += 1
        if  (method == 'HEAD') or (method == 'GET'):
            # tcpconnection, url, headers_dict, query, method, glob
            glob = httpserver.GET_HEAD(tcpconnection, url, headers_dict, query, method, 
            [tcpsocket, f_x, cget_flag, connection_status, ip, portnum, status_code, cookie_id, activethreads])

            tcpsocket, f_x, cget_flag, connection_status, ip, portnum, status_code, cookie_id = glob
        elif method == 'POST':
            glob = httpserver.POST(ent_body, tcpconnection, headers_dict, [ip,portnum, status_code])
            ip,portnum, status_code = glob
        elif method == 'DELETE':
            glob = httpserver.DELETE(url, tcpconnection, ent_body, headers_dict, [ip,portnum, status_code, activethreads])
            ip, portnum, status_code = glob
            connection_status = False
            tcpconnection.close()
        elif method == 'PUT':
            httpserver.PUT(tcpconnection, addr, ent_body, filedata, url, headers_dict, f_flag, status_code, [ip, activethreads, status_code])
        else:
            method = 'Not Defined'
            break
        # use the logging formatting
        logging.info('	{}	{}	{}	{}	{}\n'.format(addr[0], addr[1], request_line, url, status_code))
    try:
        tcpconnection.close()
        activethreads.remove(tcpconnection)
    except:
        pass

#function handling multiple requests
def server_runner(temp):
    tcpsocket, f_x, cget_flag, connection_status, SIZE, activethreads, status_code, ip, cookie_id, portnum = temp
    for _ in iter(int, 1):
        tcpconnection, addr = tcpsocket.accept() # tcpconnection = request, addr = port,ip
        start = 0
        activethreads.append(tcpconnection)  # add connections
        if not (len(activethreads) < 20 ):
            status_hanlder(tcpconnection, 503, [ip, activethreads, status_code])
            tcpconnection.close()
        else:
            start_new_thread(request_handler, (tcpconnection, addr, start, [tcpsocket, f_x, cget_flag, connection_status, SIZE, activethreads, status_code, ip, cookie_id, portnum]))
    tcpsocket.close()

def urlbreak(url):
    u = urlparse(url)
    url = unquote(u.path)
    if url == '/':
        url = os.getcwd()
    query = parse_qs(u.query)
    return (url, query)

def last_modified(url):
    try:
        l = time.ctime(os.path.getmtime(url)).split(' ')
    except OSError:
        pass    

    
    for i in l:
        if len(i) == 0:
            l.remove(i)
    l[0] = l[0] + ','
    string = (' ').join(l)
    string = 'Last-Modified: ' + string
    return string    
'''
Function to handle the exit ( Ctrl+C and other signals )
'''




if __name__ == '__main__':
                  
    connection_status = True					
                     
    cget_flag = False    	 
    month = { 'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

    f_type = FORMAT2          # Dictionary to convert content types into the file extentions eg. text/html to .html
    f_x = FORMAT      # Dictionary to convert file extentions into the content types eg. .html to text/html

    activethreads = []		     
    tcpsocket = socket(AF_INET, SOCK_STREAM)
    status_code = 0                   
    cookie_id = 0  
    #2021-11-09 14:49:23,449:http.py:	127.0.0.1	46552	GET /home/shantanu/http-server/workfile.html HTTP/1.1	/home/shantanu/http-server/workfile.html	200

    logging.basicConfig(filename = os.getcwd() + '/http.log', level = logging.INFO, format = '%(asctime)s:%(filename)s:%(message)s')
    ip = '127.0.0.1'
    # print(ip)
    try:
        portnum = int(sys.argv[1])
    except:
        print("Port Number missing\n\nTO RUN\nType: python3 httpserver.py port_number")
        sys.exit()
    try:
        tcpsocket.bind(('', portnum))
    except:
        print('\nformat for running:python3 httpserver.py port_number')
        sys.exit()
    tcpsocket.listen(5)
    print('HTTP server running on localhost, Visit for list of files : (http://' + ip + ':' + str(portnum) + '/)')
    temp = [tcpsocket, f_x, cget_flag, connection_status, SIZE, activethreads, status_code, ip, cookie_id, portnum]
    server_runner(temp)            # IMP calling the main server Function
    sys.exit()
>>>>>>> 40cde4bd6fe98f9f5ed89c3a2f9e22400bdd7e5b
