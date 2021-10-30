import os
SIZE = 2048
MONTH = { 'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }
VERSION = '1.1' # by default 1.1 version unless mentioned otherwise
MAX_NO_REQUEST = 20        
URLMAX = 2083 # max url size for a get request
HTTP_METHODS = ["GET", "POST", "HEAD", "PUT", "DELETE", "TRACE", "OPTIONS"]
STATUSCODES = {
		200 : "Ok",
		201	: "Created",
		202	: "Accepted",
		204 : "No Content",
		304 : "Not Modified",
		400 : "Bad Request",
		403 : "Forbidden",
		404 : "Not Found",
		411 : "Length required",
		412 : "Precondition Failed",
		414 : "URI too long",
		415 : "Unsupported media Type",
        500 : "Internal Server Error",
		501 : "Not Implemented",
        503 : "Server Unavailable",
		505 : "HTTP version not supported",
	}
    
TRASH = os.getcwd+ '/deleted'    
os.mkdir(TRASH)


