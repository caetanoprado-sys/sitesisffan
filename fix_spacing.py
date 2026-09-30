import sys

with open("index.html", "r") as f:
    content = f.read()

# Fix unified-section padding
content = content.replace("padding: 80px 20px 120px;", "padding: 80px 20px 80px;")

# Fix before-process-section padding
content = content.replace("padding: 130px 20px;\n            background-color: var(--color-light-bg);", "padding: 80px 20px 100px;\n            background-color: var(--color-light-bg);")

with open("index.html", "w") as f:
    f.write(content)
