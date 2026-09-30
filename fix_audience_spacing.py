import sys

with open("index.html", "r") as f:
    content = f.read()

# Fix before-process-section bottom padding
content = content.replace("padding: 80px 20px 100px;\n            background-color: var(--color-light-bg);", "padding: 80px 20px 80px;\n            background-color: var(--color-light-bg);")

# Fix audience-section top padding
content = content.replace("padding: 130px 20px 140px;\n            background-color: var(--color-white);", "padding: 80px 20px 120px;\n            background-color: var(--color-white);")

with open("index.html", "w") as f:
    f.write(content)
