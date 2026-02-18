#!/usr/bin/python3
"""Simple HTTP API: /, /data (JSON), /status (OK), 404 else."""
import http.server
import json

PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    """Handles GET requests for a simple API with endpoints:
    /, /data, /status, /info.
    """

    def do_GET(self):
        """Route GET requests based on self.path and
        return the appropriate response.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            status = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(status).encode('utf-8'))

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    """Start the HTTP server on port 8000."""
    PORT = 8000
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, Handler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
