from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>TOP SOFTWARE COMAPNIES WITH REVENUE TABLE</title>
</head>
<body bgcolor="PINK" align="left">
<table border="4" cellspacing="1" cellpadding="1" height="300" width="700" bgcolor="white" align="center">
<caption>TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES</caption>
<tr>
<th>COMPANY</th>
<th>REVENUE</th>
<th>RANKING</th>
</tr1>
<tr>
<td>GOOGLE</td>
<td>8000000</td>
<td>1</td>
</tr>
<tr>
<td>MICROSOFT</td>
<td>70000000</td>
<td>2</td>
</tr>
<tr>
<td>APPLE</td>
<td>6000000</td>
<td>3</td>
</tr>
</tr>
<tr>
<td>IBM</td>
<td>5000000</td>
<td>4</td>
</tr>
</tr>
<tr>
<td>SAMSUNG</td>
<td>4000000</td>
<td>5</td>
</tr>
</table>
</body>
    
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()