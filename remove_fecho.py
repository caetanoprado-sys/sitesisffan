import sys

with open("index.html", "r") as f:
    content = f.read()

fecho_html = """                <div class="before-process-fecho">
                    Nenhum concorrente cobre o preventivo.<br><span>É aqui que o SISFFAN se separa de "mais um sistema de prazo".</span>
                </div>"""

if fecho_html in content:
    content = content.replace(fecho_html, "")
else:
    print("Fecho HTML not found exactly as specified.")

with open("index.html", "w") as f:
    f.write(content)
