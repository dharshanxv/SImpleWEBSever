from http.server import HTTPServer, BaseHTTPRequestHandler
import platform

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        specs = f"""
        <html>
        <head>
            <title>Device Specifications</title>
        </head>
        <body>
            <h1>Simple Web Server</h1>
            <h2>Student Details</h2>
            <p>Name: Dharshan</p>
            <p>Register Number:26002500</p>

            <h2>Device Specifications</h2>
            <p>System: {platform.system()}</p>
            <p>Processor: {platform.processor()}</p>
            <p>Machine: {platform.machine()}</p>
            <p>Platform: {platform.platform()}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(specs.encode())

server = HTTPServer(("127.0.0.1", 8000), MyHandler)

print("Server started at http://127.0.0.1:8000")
server.serve_forever()