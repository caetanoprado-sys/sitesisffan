import sys

with open("index.html", "r") as f:
    content = f.read()

old_h2 = """        .before-process-content h2 {
            font-family: var(--font-title);
            font-size: clamp(2.2rem, 3.5vw, 2.8rem);
            font-weight: 800;
            color: var(--color-primary-dark);
            margin-bottom: 24px;
            line-height: 1.15;
        }"""

new_h2 = """        .before-process-content h2 {
            font-family: var(--font-title);
            font-size: clamp(2.2rem, 3.5vw, 2.8rem);
            font-weight: 800;
            color: var(--color-primary-dark);
            margin-bottom: 40px;
            line-height: 1.15;
        }"""

content = content.replace(old_h2, new_h2)

with open("index.html", "w") as f:
    f.write(content)
