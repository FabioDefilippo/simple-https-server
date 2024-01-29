from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('./cert.pem', './key.pem')
with HTTPServer(('', 443), SimpleHTTPRequestHandler) as httpd:
  httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
  httpd.serve_forever()
