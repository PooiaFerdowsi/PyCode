""" The HTTP Web Server Of Project """
import http.server
def start(address:tuple=("localhost",88))->http.server.HTTPServer:
  """ This is user defined Request Handler function and may be Override """
	httpd = http.server.HTTPServer(
		address,
		http.server.BaseHTTPRequestHandler)
	return httpd

def startBase(address:tuple=("localhost",80))->http.server.HTTPServer:
	httpd = http.server.HTTPServer(
		address,
		http.server.BaseHTTPRequestHandler)
	return httpd

def startSimple(address:tuple=("localhost",88))->http.server.HTTPServer:
	httpd = http.server.HTTPServer(
		address,
		http.server.SimpleHTTPRequestHandler)
	return httpd

def startCGI(address:tuple=("localhost",88))->http.server.HTTPServer:
	httpd = http.server.HTTPServer(
		address,
		http.server.BaseHTTPRequestHandler)
	return httpd
