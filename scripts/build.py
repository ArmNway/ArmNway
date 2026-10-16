"""Build a small static bundle for hosting (Vercel): dist/ with minified
markup, CSS split in two files, one JS file, and the assets.

Usage: python3 scripts/build.py   (needs npx html-minifier-terser on PATH or MINIFIER env)
"""
import os, re, shutil, subprocess, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
MIN = os.environ.get("MINIFIER", "npx --yes html-minifier-terser@7.2.0")

shutil.rmtree(DIST, ignore_errors=True)
os.makedirs(DIST)
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
for f in ("manifest.webmanifest", "vercel.json"):
    shutil.copy(os.path.join(ROOT, f), DIST)

tmp = os.path.join(DIST, "_min.html")
subprocess.run(MIN.split() + [
    "--collapse-whitespace", "--conservative-collapse", "--remove-comments",
    "--minify-css", "true", "--minify-js", '{"compress":{"passes":2},"mangle":true}',
    "--remove-redundant-attributes", "--remove-attribute-quotes",
    "-o", tmp, os.path.join(ROOT, "index.html")], check=True)
html = open(tmp, encoding="utf-8").read()
os.remove(tmp)

css = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
js = re.search(r"<script>(.*?)</script>", html, re.S).group(1)

# split CSS at a rule boundary near the middle (order is preserved by the two <link>s)
mid = len(css) // 2
cut = css.find("}", mid) + 1
while css[:cut].count("{") != css[:cut].count("}"):
    cut = css.find("}", cut) + 1
parts = [css[:cut], css[cut:]]
for i, part in enumerate(parts, 1):
    open(os.path.join(DIST, f"app-{i}.css"), "w", encoding="utf-8").write(part)
open(os.path.join(DIST, "app.js"), "w", encoding="utf-8").write(js)

html = html.replace("<style>" + css + "</style>", '<link rel=stylesheet href=app-1.css><link rel=stylesheet href=app-2.css>')
html = html.replace("<script>" + js + "</script>", "<script src=app.js></script>")
open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(html)

for dirpath, _, files in os.walk(DIST):
    for f in sorted(files):
        p = os.path.join(dirpath, f)
        print(f"{os.path.getsize(p):>7}  {os.path.relpath(p, DIST)}")
