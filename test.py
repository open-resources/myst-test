from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

md = (
    MarkdownIt()
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .disable('image')
    .enable('table')
)
text = ("""
---
a: 1
---

a | b
- | -
1 | 2
3 | 4
5 | 6

A footnote [^1]

[^1]: some details

a
""")
tokens = md.parse(text)
html_text = md.render(text)

text_file = open("output.html", "w")
text_file.write(html_text)
text_file.close()