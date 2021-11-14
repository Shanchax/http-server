
import os
from datetime import date

TODAY = date.today()



ROOT = os.getcwd()


LOG = ROOT + '/http.log'
w = open(LOG, "a") 
w.close()


NEWFILE = ROOT + '/ newfile.html' # path

w = open(NEWFILE, "w")
d = '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Response Recieved</title>
<body>
    <h1>Yeah We got the response!</h1>
    </br>
    <h1>Your Response was Saved Succesfully!</h1>
</body>
</html>'''
w.write(d)
w.close()

'''
All data entered by the client is stored here for checking Purpose.
'''
CSVFILE = ROOT + '/output.csv'
w = open(CSVFILE, "a") # only appending not writing
w.close()

'''
all the files which are deleted using DELETE are getting moved here.
'''
DELETE = ROOT + '/DELETE'
'''
the /deleted folder mentioned above is created here.
For the DELETE req purpose
'''
try:
	os.mkdir(DELETE)
except:
	pass

'''
username and password for approval of delete request method
'''
USERNAME = 'shan' # delete can only be done after checking Auth
PASSWORD = '3096' # Keep this secret folks
MAX_THREADS = 20


'''
cookie details
'''
COOKIE = 'Set-Cookie: id=' # id will be given in the program
MAXLIFE = '; max-age=3600' # 3600 sec is 60min

'''Following is the file formats supported by the server'''
FEXTENSION = {
		".aac"	: "audio/aac",
		".abw"	: "application/x-abiword",
		".arc"	: "application/x-freearc",
		".avi"	: "video/x-msvideo",
		".azw"	: "application/vnd.amazon.ebook",
		".bin"	: "application/octet-stream",
		".bmp"	: "image/bmp",
		".bz"	: "application/x-bzip",
		".bz2"	: "application/x-bzip2",
		".csh"	: "application/x-csh",
		".css"	: "text/css",
		".csv"	: "text/csv",
		".doc"	: "application/msword",
		".docx"	: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
		".eot"	: "application/vnd.ms-fontobject",
		".epub" : "application/epub+zip",
		".gz"	: "application/gzip",
		".gif"	: "image/gif",
		".htm"	: "text/html",
		".html" : "text/html",
		".ico" 	: "image/vnd.microsoft.icon",
		".ics"	: "text/calendar",
		".jar"	: "application/java-archive",
		".jpeg"	: "image/jpeg",
		".jpg"	: "image/jpeg",
		".js"	: "text/javascript",
		".json"	: "application/json",
		".jsonld": "application/ld+json",
		".mid"	: "audio/midi",
		" .midi": "audio/midi",
		".mjs"	: "text/javascript",
		".mp3"	: "audio.mpeg",
		".mpeg"	: "video/mpeg",
		".mpkg"	: "application/vnd.apple.installer+xml",
		".odp"	: "application/vnd.oasis.opendocument.presentation",
		".ods"	: "application/vnd.oasis.opendocument.spreadsheet",
		".oga"	: "audio/ogg",
		".ogv"	: "video/ogg",
		".ogx"	: "application/ogg",
		".otf"	: "font/otf",
		".png"	: "image/png",
		".pdf"	: "application/pdf",
		".php"	: "appliction/php",
		".ppt"	: "application/vnd.ms-powerpoint",
		".pptx"	: "application/vnd.openxmlformats-officedocument.presentationml.presentation",
		".rar"	: "application/x-rar-compressed",
		".rtf"	: "application/rtf",
		".sh"	: "application/x-sh",
		".svg"	: "image/svg+xml",
		".swf"	: "application/x-shockwave-flash",
		".tar"	: "application/x-tar",
		".tif"	: "image/tiff",
		" .tiff": "image/tiff",
		".ts"	: "video/mp2t",
		".ttf"	: "font/ttf",
		".txt" 	: "text/html",
		".vsd"	: "application/vnd.visio",
		".wav"	: "audio/wav",
		".weba"	: "audio/webm",
		".webm"	: "video/webm",
		".webp"	: ".webp",
		".woff" : "font/woff",
		".woff2": "font/woff2",
		".xhtml": "application/xhtml+xml",
		".xls"	: "application/vnd.ms-excel",
		".xlsx"	: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
		".xml"	: "application/xml",
		".xul"	: "application/vnd.mozilla.xul+xml",
		".zip"	: "application/zip",
		".3gp"	: "video/3gpp",
		".3g2"	: "video/3gpp2",
		".7z"	: "application/x-7z-compressed",
	}
    
'''Following is the file formats supported by the server'''
FTYPE = {
		"audio/aac"                     : ".aac"    ,
		"application/x-abiword"         : ".abw"	,
		"application/x-freearc"         : ".arc"	,
		"video/x-msvideo"               : ".avi"    ,
        "application/vnd.amazon.ebook"  : ".azw"    ,
		"application/octet-stream"      : ".bin"	,
		"image/bmp"                     : ".bmp"    ,
		"application/x-bzip"            : ".bz"	    ,
		"application/x-bzip2"           : ".bz2"    ,
		"application/x-csh"             : ".csh"    ,
		"text/css"                      : ".css"    ,
		"text/csv"                      : ".csv"	,
		"application/msword"            : ".doc"    ,
		"application/vnd.openxmlformats-officedocument.wordprocessingml.document":".docx"	 ,
		"application/vnd.ms-fontobject" : ".eot"	,
		"application/epub+zip"          : ".epub"   ,
		"application/gzip"              : ".gz"	    ,
		"image/gif"                     : ".gif"	,
		"text/html"                     : ".html"   ,
		"image/vnd.microsoft.icon"      : ".ico" 	,
		"text/calendar"                 : ".ics"	,
		"application/java-archive"      : ".jar"	,
		"image/jpeg"                    : ".jpeg"	,
		"text/javascript"               : ".js"	    ,
		"application/json"              : ".json"	,
		"application/ld+json"           : ".jsonld" ,
		"audio/midi"                    : ".mid"	,
		"audio.mpeg"                    : ".mp3"	,
		"video/mpeg"                    : ".mpeg"	,
		"application/vnd.apple.installer+xml":".mpkg"	 ,
		"application/vnd.oasis.opendocument.presentation"   :   ".odp"	 ,
		"application/vnd.oasis.opendocument.spreadsheet"    :   ".ods"	 ,
		"audio/ogg"                     : ".oga"	,
		"video/ogg"                     : ".ogv"	,
		"application/ogg"               : ".ogx"	,
		"font/otf"                      : ".otf"	,
		"image/png"                     : ".png"	,
		"application/pdf"               : ".pdf"	,
		"appliction/php"                : ".php"	,
		"application/vnd.ms-powerpoint" : ".ppt"	,
		"application/vnd.openxmlformats-officedocument.presentationml.presentation":".pptx"	 ,
		"application/x-rar-compressed"  : ".rar"	,
		"application/rtf"               : ".rtf"	,
		"application/x-sh"              : ".sh"	    ,
		"image/svg+xml"                 : ".svg"	,
		"application/x-shockwave-flash" : ".swf"	,
		"application/x-tar"             : ".tar"	,
		"image/tiff"                    : ".tif"	,
		"video/mp2t"                    : ".ts"	    ,
		"font/ttf"                      : ".ttf"	,
		"application/vnd.visio"         : ".vsd"	,
		"audio/wav"                     : ".wav"	,
		"audio/webm"                    : ".weba"	,
		"video/webm"                    : ".webm"	,
		".webp"                         : ".webp"	,
		"font/woff"                     : ".woff"   ,
		"font/woff2"                    : ".woff2"  ,
		"application/xhtml+xml"         : ".xhtml"  ,
		"application/vnd.ms-excel"      : ".xls"	,
		"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":".xlsx"	 ,
		"application/xml"               : ".xml"	,
		"application/vnd.mozilla.xul+xml":".xul"    ,
		"application/zip"               : ".zip"	,
		"video/3gpp"                    : ".3gp"	,
		"video/3gpp2"                   : ".3g2"    ,
		"application/x-7z-compressed"   : ".7z"	    ,
	}

'''Response status codes'''
status_codes = {
		200 : "Ok",
		201	: "Created",
		202	: "Accepted",
		204 : "No Content",
		304 : "Not Modified",
		400 : "Bad Request",
		401 : "Unauthorized",
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


methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "TRACE", "OPTIONS"]