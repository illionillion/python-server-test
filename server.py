import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # print("serving at port", PORT)
    print(f'serving as http://localhost:{PORT}')
    httpd.serve_forever()