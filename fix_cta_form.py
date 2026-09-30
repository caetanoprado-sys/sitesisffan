import sys

with open("index.html", "r") as f:
    content = f.read()

# Shrink the form padding
content = content.replace('padding: 48px;\n            border-radius: var(--radius-lg);', 'padding: 32px;\n            border-radius: var(--radius-lg);')

# Shrink the textarea height
content = content.replace('min-height: 100px;', 'min-height: 70px;')

# Reduce margin in form groups
content = content.replace('margin-bottom: 18px;', 'margin-bottom: 12px;')

# Reduce CTA block bottom padding
content = content.replace('padding: 100px 20px 80px;', 'padding: 80px 20px 40px;')

# Reduce Blog section top padding
content = content.replace('padding: 100px 20px;\n            background-color: var(--color-light-bg);', 'padding: 60px 20px 100px;\n            background-color: var(--color-light-bg);')

with open("index.html", "w") as f:
    f.write(content)
