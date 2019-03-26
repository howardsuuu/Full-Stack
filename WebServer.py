from http.server import BaseHTTPRequestHandler,HTTPServer
import cgi # let users request data from the server through web browser

# Indicate what code it will listen to based on the type of HTTP request that send to the server
class webserverHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            # look for the URL that end with /hello
            if self.path.endswith("/hello"):
                self.send_response(200)
                # to show replying with text in HTML form to client
                # along with end_headers
                self.send_header('Content-type', 'text/html')# return text in html
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Howard is handsome!</h1>"
                output += '''<form method='POST' enctype='nultipart/form-data'
                action='/hello'><h2>What would you like me to say?</h2>
                <input name='message'type='text' ><input type='Submit' value='Submit> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode(encoding='utf-8', errors = 'strict')) # send message back to the client
                print(output)           # need encode
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data'
                 action='/hello'><h2>What would you like me to say?</h2><input name="message" 
                 type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode(encoding='utf-8', errors='strict'))
                print(output)
                return # exit if statement
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = ''
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data'
             action='/hello'><h2>What would you like me to say?</h2><input 
             name="message" type="text" >
             <input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output.encode(encoding='utf-8', errors = 'strict'))
            print(output)
        except:
            pass

#Specify what port it will listen to
def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler) # make up name(webserverHandler for the request handler class)
        print('Web server running on port %s' % port)
        server.serve_forever() # Handle requests until an explicit shutdown() request

    except KeyboardInterrupt:
        print("Control + C entered, stopping web server...")
        server.socket.close() # shutdown the sever
    

if __name__ == '__main__':
    main()