from socket import *
import datetime 
import os
import time
import random
import threading
from _thread import *
import shutil		            		 # to implement delete method
import csv          					 # used in put and post method to insert data
import gzip
import brotli
import zlib	            		
import sys
import logging
from tkinter.constants import LEFT
from config import *                    # import variables
import signal   
from urllib.parse import *	 # for parsing URL/URI
import os
import time    
import hashlib                    # signal to handle Ctrl+C and other SIGNALS

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
 

        build_response += '\r\n' + 'Set-Cookie: id=' + str(cookie_id) + MAXLIFE
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
            
            # elif header == 'Accept-Encoding':
            #    if isItFile:
            #        req_temp = '\r\nContent-Length: ' + str(size)
            #        build_response += req_temp
            #    else:
            #        pass
            

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
                

            elif header == 'Accept-Language':
                req_temp = '\r\nContent-Language: ' + headers_dict[header]
                build_response += req_temp
            

            elif header == 'Accept-Encoding':
                convo = accept_enc(headers_dict[header])
                print(convo)
                build_response += 'Content-Encoding:' + convo
                
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
                w
                build_response += 'HTTP/1.1 201 Created'
                status_code = 201
                build_response.append('Location: ' + url)
                csvwriter = csv.writer(fi)
                csvwriter.writerow(fields)
                csvwriter.writerow(row)
            fi.close()
            build_response += '\r\nServer: ' + ip + '\r\n'+ date()
            f = open(NEWFILE, "rb")
            with open(url,"rb") as f:
                body = f.read()
            build_response += '\r\nContent-Language: en-US,en'
            size = os.path.getsize(NEWFILE)
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
                print(encoded)
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

        # Etag = '{}'.format(hashlib.md5((date(last_modified(url))).encode()).hexdigest()) 
        # build_response += '\r\n' + 'Etag : ' + Etag
        if (not(os.access(url, os.W_OK))):
            status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])

        if os.path.isfile(url):
            fi = open(url, "a")
            status_code = 200
            build_response += 'HTTP/1.1 {} OK'.format(status_code)
            fi.write(ent_body)
            fi.close()
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
        f = open(NEWFILE, "rb")
        size = os.path.getsize(NEWFILE)
        build_response += '\r\nContent-Language: en-US,en' + '\r\nContent-Type: text/html'+ '\r\n' + 'Content-Length: ' + str(size) + '\r\n' + last_modified(url) + '\r\n\r\n'
        response = build_response.encode()
        print(build_response)
        tcpconnection.send(response)
        tcpconnection.sendfile(f)
        return [ip, portnum, status_code]

    def PUT(self,tcpconnection, addr, ent_body, filedata, url, headers_dict, f_flag, status_code, arg_list):
        ip, activethreads, status_code = arg_list
        build_response = ''
        
        try:
            length = int(headers_dict['Content-Length'])
        except:
            status_code = 411
            dummy = status_hanlder(tcpconnection, 411, [ip, activethreads, status_code])
            ip, activethreads, status_code = dummy
        
        
        i = len(ent_body)
        size = length - i
        isItDir = os.path.isdir(url)
        isItFile = os.path.isfile(url)
        #############################################
        
        
            #ent_body = tcpconnection.recv(SIZE)
        try:
            filedata = filedata + ent_body
            print("heyzzaa")
                
        except TypeError:
            ent_body = ent_body.encode()
            filedata = filedata + ent_body
                
        
        size -= len(ent_body)
        
           
        mode_f, r_201, move_p = True, False, False
        limit = len(ROOT)
        l = len(url)
        
        if not l < limit:
            
            if isItFile:
                if os.access(url, os.W_OK) and  os.access(url, os.R_OK):
                    pass     
                else:
                    glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                    ip, activethreads, status_code = glob
                # writing File mode ON
                mode_f = True
                if f_flag == 1:
                    f = open(url, "wb")
                    
                    f.write(filedata)                    
                elif f_flag == 0:	
                    print("hi")
                    f = open(url, "w")
                    f.write(filedata.decode())
                else:
                    f = open(url, "wb")
                    f.write(filedata)
                f.close()
            elif isItDir:
                move_p = True
                loc = ROOT + '/' + str(addr[1])
                if os.access(url, os.W_OK):
                    # no need for read access
                    if os.access(url, os.R_OK):
                        pass
                    else:
                        pass
                else:
                    dummy = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                    ip, activethreads, status_code = dummy
                try:
                    loc = loc + f_type[headers_dict['Content-Type'].split(';')[0]]
                except:
                    dummy = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                    ip, activethreads, status_code = dummy
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
                if ROOT in url:
                    url = ROOT + '/' + str(addr[1])
                    try:
                        url = url + f_type[headers_dict['Content-Type'].split(';')[0]]
                    except:
                        # error in header
                        glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                        ip, activethreads, status_code = glob
                    if f_flag:
                        f = open(url, "wb")
                        f.write(filedata)                        
                    elif f_flag == 0:	
                        # open the file in write mode
                        f = open(url, "w")
                        f.write(filedata.decode())
                    else:
                        # open the file in write binary mode
                        f = open(url, "wb")
                        f.write(filedata)
                    f.close()
                    r_201 = True
                else:
                    mode_f = False
        else:
            
            move_p = True
            loc = ROOT + '/' + str(addr[1])
            try:
                loc = loc + f_type[headers_dict['Content-Type']]
            except:
                glob = status_hanlder(tcpconnection, 403, [ip, activethreads, status_code])
                ip, activethreads, status_code = glob
            if f_flag == 0:	
                f = open(loc, "w")
            else:
                f = open(loc, "wb")
            f.write(filedata)
            f.close()
        if move_p:
            status_code = 301
            build_response += 'HTTP/1.1 301 Moved Permanently' + '\r\nLocation: ' + loc + '\r\nConnection: keep-alive' + '\r\n\r\n'
        elif mode_f:
            status_code = 204
            build_response += 'HTTP/1.1 204 No Content' + '\r\n\Content-Location: ' + url + '\r\nConnection: keep-alive' + '\r\n\r\n'
        elif r_201:
            status_code = 201
            build_response += 'HTTP/1.1 201 Created' + '\r\nContent-Location: ' + url + '\r\nConnection: keep-alive' + '\r\n\r\n'
        elif not mode_f:
            status_code = 501
            build_response += 'HTTP/1.1 501 Not Implemented'
        #build_response += '\r\nConnection: keep-alive' + '\r\n\r\n'
        response = build_response.encode()
        tcpconnection.send(response)
        tcpconnection.close()
        return None

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


def accept_enc(state):
    
    content_enc = ''
    maxq = 0.0
    
    if(state == ""):
        return 'Identity'
    temp_list = state.split(',')
    if(len(temp_list)== 1):

        return temp_list.split(';')[0]
    
    for element in temp_list:
        temp1 = element.split(';')
        tempq = float(temp1[1].split('=')[1])
        if(maxq < tempq):
            content_enc = temp1[0]
            maxq = tempq

    return content_enc
        
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
        if (len(url) > 250 and urlflag == 0):
            status_hanlder(tcpconnection, 414, [ip, activethreads, status_code])
            tcpconnection.close()
            break
        elif len(url) <= 250:  #max length of url is 250
            # print("working Fine")
            urlflag = 1
            pass
        else:
            urlflag = 1
        version = request_line[2]
        try:
            version_num = version.split('/')[1]
            if (version_num == '1.1'):
                
                pass
            elif not (version_num == '1.1'):
                status_hanlder(tcpconnection, 505, [ip, activethreads, status_code])
        except IndexError:
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

if __name__ == '__main__':
                  
    connection_status = True					
                     
    cget_flag = False    	 
    month = { 'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

    f_type = FTYPE        # Dictionary to convert content types into the file extentions eg. text/html to .html
    f_x = FEXTENSION    # Dictionary to convert file extentions into the content types eg. .html to text/html

    activethreads = []		     
    tcpsocket = socket(AF_INET, SOCK_STREAM)
    status_code = 0                   
    cookie_id = 0  
    #2021-11-09 14:49:23,449:http.py:	127.0.0.1	46552	GET /home/shantanu/http-server/NEWFILE.html HTTP/1.1	/home/shantanu/http-server/NEWFILE.html	200

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







