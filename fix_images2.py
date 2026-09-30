import sys

with open("index.html", "r") as f:
    content = f.read()

old_css = """        .testimonial-author-img {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(193, 162, 112, 0.3);
        }"""

new_css = """        .testimonial-author-img {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            object-fit: cover;
            object-position: top;
            border: 2px solid rgba(193, 162, 112, 0.3);
        }"""

content = content.replace(old_css, new_css)

with open("index.html", "w") as f:
    f.write(content)
