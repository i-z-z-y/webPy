# http.server is meant for demo purposes and does not implement the stringent security checks needed of real production HTTP server.
# It is not recommend to use this directly in production.

import http.server
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
