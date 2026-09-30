# SImpleWEBSever
# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
'''python
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
            <p>Register Number: 26002500</p>

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
server.serve_forever()'''


## OUTPUT:
Simple Web Server

Student Details

Name: Dharshan
Register Number: 26002500

Device Specifications

System: Windows
Processor: Intel64 Family 6 Model 186 Stepping 2, GenuineIntel
Machine: AMD64
Platform: Windows-11-10.0.26200-SP0

URL: http://127.0.0.1:8000
## RESULT:
The program for implementing simple webserver is executed successfully.
