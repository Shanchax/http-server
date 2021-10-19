


import os
import socket
import sys
import datetime
 
class makesocket:
    

    def __init__(self, host='127.0.0.1', port=1234):
        self.host = host
        self.port = port

    def start(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.bind((self.host, self.port))
        s.listen()

        print("server is listening ")

        while(1):
            connection, addr = s.accept()
            print("Connected by", connection)
            receive = connection.recv(2048) 

            response = self.handle_request(receive)

            connection.sendall(response)
            connection.close()

    def handle_request(self, data):
        
        return data  

    def stopserver(s):
        s.close()
        sys.exit(1)

class HTTPServer(makesocket):
    

    headers = {
        
        'Content-Type': 'text/html',
        'Connection' : 'keep-alive'
        
    }

    status_codes = {
        200: 'OK',
        204 : "No Content",
        304 : "Not Modified",
        403 : "Forbidden",

        404: 'Cant Fiund',
        501: 'Not Implemented',
    }

    def handle_request(self, data): # handler can be GET, POST, HEAD etc.
       

        request = HTTPRequest(data) 
        handler = getattr(self, '%s' % request.method)

        response = handler(request)
        return response   #thinking of using a 501 not implemented function here with the help of try-except

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
        """Handler for OPTIONS HTTP method"""

        response_line = self.response_line(200)

        extra_headers = {'Allow': 'OPTIONS, GET'}
        response_headers = self.response_headers(extra_headers)

        blank_line = b'\r\n'

        return b''.join([response_line, response_headers, blank_line])

    def GET(self, request):
       

        path = request.uri.strip('/') 

        if not path:
            path = 'index.html'

        if os.path.exists(path) : 
          if(not os.path.isdir(path)):  
            response_line = self.response_line(200)
            content_type = 'text/html'
            extra_headers = {'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

            with open(path, 'rb') as f:
                response_body = f.read()  # reading from index.html
        else:
            response_line = self.response_line(404)
            response_headers = self.response_headers()
            response_body = b'<h1>404 Not Found</h1>'

        blank_line = b'\r\n'

        response = b''.join([response_line, response_headers, blank_line, response_body])

        return response

    def HEAD(self, request):
        path = request.uri.strip('/')
        if not path:
            path = 'index.html'
        if os.path.exists(path) :
            if(os.path.isfile(path)):
                response_line = self.response_line(200)
                content_type = 'text/html'
                extra_headers = {'Content-Type': content_type}
                response_headers = self.response_headers(extra_headers)
                blank_line = b'\r\n'
        response = b''.join([response_line, response_headers, blank_line])
        return response



        





class HTTPRequest:

    def __init__(self, data):
        self.method = None
        self.data =data
        self.uri = None
        self.http_version = '1.1' 
        self.parse(data)

    def parse(self, data):
        lines = data.split(b'\r\n')

        request_line = lines[0] # request line is the first line of the data

        words = request_line.split(b' ') # split request line into seperate words

        self.method = words[0].decode() 

        if len(words) > 1:
            
            self.uri = words[1].decode() 

        if len(words) > 2:
            self.http_version = words[2]



if __name__ == '__main__':
    server = HTTPServer()
    server.start()
