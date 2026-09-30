import sys

with open("index.html", "r") as f:
    content = f.read()

old_css = """        .trust-author-img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(193, 162, 112, 0.2);
        }"""

new_css = """        .trust-author-img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            object-position: top;
            border: 2px solid rgba(193, 162, 112, 0.2);
        }"""

content = content.replace(old_css, new_css)

with open("index.html", "w") as f:
    f.write(content)
