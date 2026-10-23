#!/usr/bin/env python3
"""Build a static site for hosting (Vercel, Netlify, any static host).

The page files are written as artifact bodies (no doctype/head), so this wraps
each one in the same HTML skeleton serve.py uses and writes clean URLs:

    dist/index.html          ← symbiote-daemon.html   (the main page)
    dist/eats/index.html     ← symbiote-eats.html
    dist/button/index.html   ← symbiote-button.html

    python3 build.py
"""
import shutil
from pathlib import Path

from serve import ROOT, SKELETON

ROUTES = {
    "": "symbiote-daemon.html",
    "eats": "symbiote-eats.html",
    "button": "symbiote-button.html",
}

DIST = ROOT / "dist"


def main():
    # clear old pages but keep dist/.vercel, which links this folder to its Vercel project
    for route in ROUTES:
        shutil.rmtree(DIST / route, ignore_errors=True) if route else (DIST / "index.html").unlink(missing_ok=True)
    (DIST / "vercel.json").parent.mkdir(parents=True, exist_ok=True)
    (DIST / "vercel.json").write_text('{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n', encoding="utf-8")
    # never upload the CLI's local token file
    (DIST / ".vercelignore").write_text(".env*\n.vercel\n", encoding="utf-8")
    for route, name in ROUTES.items():
        out = DIST / route / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        body = (ROOT / name).read_text(encoding="utf-8")
        out.write_text(SKELETON.format(body=body), encoding="utf-8")
        print(f"/{route:<8} ← {name}")


if __name__ == "__main__":
    main()
