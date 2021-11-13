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
from config import *                    # import variables
import signal   
from urllib.parse import *	 # for parsing URL/URI
import os
import time    
import httpfinal
from httpfinal import *















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
