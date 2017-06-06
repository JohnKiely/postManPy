# Code derived from an example found on
# http://stackoverflow.com/questions/12731207
# /how-can-i-debug-post-requests-with-pythons-basehttpserver-simplehttpserver
import http.server #Python3

HOST_NAME = ''
PORT_NUMBER=2000

postVars = ''

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(s):
        global postVars
        s.send_response(200)
        s.end_headers()
        varLen = int(s.headers['Content-Length'])
        postVars = s.rfile.read(varLen)
        print (postVars)

server_class = http.server.HTTPServer
httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)

try:
    httpd.handle_request()
except KeyboardInterrupt:
    pass

print (postVars)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    print ("It's all over!")
