# -*- coding: utf-8 -*-

import feedparser
# from datetime import datetime
# from time import mktime

# RSSのURL
RSS_URL = "https://arxiv.org/rss/stat.ML"

# RSSの取得
feed = feedparser.parse(RSS_URL)


print '''<html><head>
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
</head><body>'''

print "<h1>", feed.feed.date, "</h1>"

for entry in range(len(feed.entries)):
    # RSSの内容を一件づつ処理する
    title = feed.entries[entry].title
    link = feed.entries[entry].link
    description = feed.entries[entry].description
    author = feed.entries[entry].author
    a = ""
    l = 0
    for c in author:
        if c == '<':
            l += 1
        if c == '>':
            l -= 1
        if 0 == l and '>' != c:
            a += c
    author = a

    # 表示
    print "<h2>", title, "</h2>"
    # print link
    print "<p>", author, "</p>"
    print description
print "</body></html>"
