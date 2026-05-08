"""
Sachin Portfolio — Local Development Server
============================================
Run this file to serve your portfolio on localhost.

Usage:
    python server.py

Then open: http://localhost:3000
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean log output
        print(f"  → {self.address_string()} [{args[0]}] {args[1]}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("\n" + "="*45)
        print("  🚀  Sachin Portfolio — Dev Server")
        print("="*45)
        print(f"  📂  Serving:  {DIRECTORY}")
        print(f"  🌐  Local:    {url}")
        print(f"  ⛔  Stop:     Ctrl + C")
        print("="*45 + "\n")
        webbrowser.open(url)   # Auto-opens in browser
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  Server stopped. Goodbye! 👋\n")
