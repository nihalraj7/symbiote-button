#!/usr/bin/env python3
"""Local dev server for the Symbiote Button.

symbiote-button.html is written as an artifact body (no doctype/head), so this
wraps it in a proper HTML skeleton at "/" and re-reads it on every request —
edit the file, refresh the browser. "/eats" serves the page-eating version,
"/daemon" the version where it turns into a daemon and devours the page.

    python3 serve.py            # http://localhost:8080
    python3 serve.py 3000       # custom port
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "symbiote-button.html"
# extra pages, each wrapped the same way: /eats → symbiote-eats.html
PAGES = {
    "eats": ROOT / "symbiote-eats.html",
    "symbiote-button": PAGE,
    "symbiote-eats": ROOT / "symbiote-eats.html",
    "daemon": ROOT / "symbiote-daemon.html",
    "symbiote-daemon": ROOT / "symbiote-daemon.html",
}
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

SKELETON = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  :root {{ color-scheme: light; padding-top: env(safe-area-inset-top); padding-bottom: env(safe-area-inset-bottom); }}
  body {{ margin: 0; font: 14px system-ui, sans-serif; }}
  img {{ max-width: 100%; }}
  [hidden] {{ display: none !important; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        route = self.path.split("?")[0].strip("/")
        if route.endswith(".html"):
            route = route[:-5]
        page = PAGE if route in ("", "index") else PAGES.get(route)
        if page:
            html = SKELETON.format(body=page.read_text(encoding="utf-8")).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(html)
            return
        super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Symbiote Button → http://localhost:{PORT}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
