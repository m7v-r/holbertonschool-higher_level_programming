import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        # Handle the root endpoint "/"
        if self.path == '/':
            self._set_headers(200, 'text/plain')
            self.wfile.write(b"Hello, this is a simple API!")

        # Handle the "/data" endpoint
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._set_headers(200, 'application/json')
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Handle the "/status" endpoint
        elif self.path == '/status':
            self._set_headers(200, 'application/json')
            self.wfile.write(json.dumps({"status": "OK"}).encode('utf-8'))

        # Handle the "/info" endpoint
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._set_headers(200, 'application/json')
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # Handle undefined endpoints with 404
        else:
            self._set_headers(404, 'application/json')
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

# Run the server on port 8000
PORT = 8000
with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
