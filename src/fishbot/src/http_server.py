import http.server
import socketserver

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/':
            self.path = "num"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def main() -> None:
    handler = MyRequestHandler
    PORT = 8000
    my_server = socketserver.TCPServer(('', PORT), handler)
    my_server.serve_forever()

if __name__ == "__main__":
    main()
