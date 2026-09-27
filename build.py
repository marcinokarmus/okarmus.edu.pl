"""src.html -> index.html: jednoliterowe słowa sklejone twardą spacją z następnym (tylko w tekście, nie w tagach)."""
import re

src = open("src.html", encoding="utf-8").read()
head, body = src.split("<body>", 1)
fix = lambda t: re.sub(r"(?<![\w.&;-])([aiouwzAIOUWZ]) ", "\\1\u00a0", t)
body = re.sub(r">([^<]+)<", lambda m: ">" + fix(m.group(1)) + "<", body)
head = re.sub(r'(content="[^"]*")', lambda m: fix(m.group(1)), head)
open("index.html", "w", encoding="utf-8").write(head + "<body>" + body)
print("OK")
