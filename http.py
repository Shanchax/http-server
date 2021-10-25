

import os
import socket
import mimetypes
import shutil
import datetime
from datetime import date

 
class makesocket:
    

    def __init__(self, host='127.0.0.1', port=1234):
        self.host = host
        self.port = port

    def start(self):
        

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen()

        print("server is listening  at", s.getsockname())

        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            data = conn.recv(2048) 

            response = data

            conn.sendall(response)
            conn.close()

    


class HTTPServer(makesocket):
    

    headers = {
       
        'Content-Type': 'text/html',
        'Connection type' : 'keep-alive'
    }

    status_codes = {
        200: 'OK',
        201	: "Created",
        202	: "Accepted",
        204 : "No Content",
        304 : "Not Modified",
        400 : "Bad Request",
        401 : "Unauthorized",
        403 : "Forbidden",
        404: 'Not Found',
        501: 'Not Implemented',

    }

    def handle_request(self, data):

        request = HTTPRequest(data) 

        try:
            handler = getattr(self, '%s' % request.method)
        except AttributeError:
            handler = self.HTTP_501_handler

        response = handler(request)
        return response

    def response_line(self, status_code):
        reason = self.status_codes[status_code]
        response_line = 'HTTP/1.1 %s %s\r\n' % (status_code, reason)

        return response_line.encode() 

    def response_headers(self, extra_headers=None):
        headers_copy = self.headers.copy() 
        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ''

        for h in headers_copy:
            headers += '%s: %s\r\n' % (h, headers_copy[h])

        return headers.encode()
        
    def OPTIONS(self, request):

        response_line = self.response_line(200)

        extra_headers = {'Allow': 'OPTIONS, GET'}
        response_headers = self.response_headers(extra_headers)

        blank_line = b'\r\n'

        return b''.join([response_line, response_headers, blank_line])

    def GET(self, request):

        path = request.uri.strip('/') 

        if not path:
            path = 'index.html'

        if os.path.exists(path) and not os.path.isdir(path):
            response_line = self.response_line(200)
            content_type  = mimetypes.guess_type(path)[0] or 'text/html'
            
            extra_headers = {'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

            with open(path, 'rb') as f:
                response_body = f.read()
        else:
            response_line = self.response_line(404)
            response_headers = self.response_headers()
            response_body = b'<h1>404 Not Found</h1>'

        blank_line = b'\r\n'

        response = b''.join([response_line, response_headers, blank_line, response_body])

        return response

    def HTTP_501_handler(self, request):

        response_line = self.response_line(status_code=501)

        response_headers = self.response_headers()

        blank_line = b'\r\n'

        response_body = b'<h1>501 Not Implemented</h1>'

        return b"".join([response_line, response_headers, blank_line, response_body])
    

    def DELETE( self , request):
        path = request.uri.strip('/')
        isItDir = os.path.isdir(path)
        isItFile = os.path.isfile(path)
        option_list = path.split('/')
        response = ''
        if( isItFile):
            scode = 200
            response += 'HTTP/1.1 200 OK'
            try:
                if (os.access(path, os.W_OK)):
                    if (os.access(path, os.R_OK)):
                        pass
                    
                else:
                    print('execute sudo chmod 777 ' + path)
            except(shutil.Error):
                os.remove(path)
        else:
            scode = 400
            response += 'HTTP/1.1 400 Bad Request'
        response += '\r\nServer: ' + self.s.gethostbyname()
        response += '\r\nConnection: keep-alive'
        response += '\r\n' + date.today()
        response += '\r\n\r\n'
        response = response.encode()
        return response
        
        
        
class HTTPRequest:
    

    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = '1.1' 

        
        self.parse(data)

    def parse(self, data):
        lines = data.split(b'\r\n')

        request_line = lines[0] 

        words = request_line.split(b' ') 

        self.method = words[0].decode() 
        if len(words) > 1:
    
            self.uri = words[1].decode() 

        if len(words) > 2:
        
            self.http_version = words[2]



if __name__ == '__main__':
    server = HTTPServer()
    server.start()
