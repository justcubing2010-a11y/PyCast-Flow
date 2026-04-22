import http.server
import socketserver 
import os
import re


class RangeRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
            
        range_header = self.headers.get('Range')
        if not range_header:
            return super().send_head()

        size = os.path.getsize(path)
        m = re.search(r'bytes=(\d+)-(\d*)', range_header)
        if not m:
            return super().send_head()

        start = int(m.group(1))
        end = m.group(2)
        end = int(end) if end else size - 1

        if start >= size:
            self.send_error(416, "Requested Range Not Satisfiable")
            return None

        self.send_response(206)
        self.send_header('Content-type', self.guess_type(path))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Last-Modified', self.date_time_string(os.path.getmtime(path)))
        self.end_headers()

        f = open(path, 'rb')
        f.seek(start)
        return f


class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


PORT = 8000
handler = RangeRequestHandler

with ThreadedHTTPServer(("", PORT), handler) as httpd:
    print(f"Server active at http://[Your-Phone-IP]:{PORT}")
    print("Keep Pydroid open while streaming!")
    httpd.serve_forever()
