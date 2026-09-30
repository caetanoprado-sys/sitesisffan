with open("index.html", "r") as f:
    content = f.read()

# Fix text repetition
content = content.replace('<span class="section-label">Nossos planos</span>', '<span class="section-label">Investimento</span>')

# Fix spacing in CSS
content = content.replace('padding: 120px 20px 0;', 'padding: 80px 20px 0;')
content = content.replace('margin: 0 auto 72px;', 'margin: 0 auto 48px;')
content = content.replace('margin: 0 auto 80px;', 'margin: 0 auto 40px;')
content = content.replace('max-width: 440px; margin-bottom: 80px;', 'max-width: 440px; margin-bottom: 48px;')
content = content.replace('margin: 0 auto 100px;', 'margin: 0 auto 56px;') # This matches both includes and addons
content = content.replace('margin: 0 auto 120px;', 'margin: 0 auto 64px;')
content = content.replace('margin-bottom: 64px;', 'margin-bottom: 40px;') # implementation-header

with open("index.html", "w") as f:
    f.write(content)
print("Done")
