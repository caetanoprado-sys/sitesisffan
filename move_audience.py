import sys

with open("index.html", "r") as f:
    lines = f.readlines()

# Find start and end of audience section
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "<!-- Seção 7: Para quem é -->" in line:
        start_idx = i
    if start_idx != -1 and "</section>" in line and i > start_idx:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    # Remove the old section
    del lines[start_idx:end_idx+1]
else:
    print("Could not find the old audience section.")

new_audience_html = """
    <!-- Seção 5: Para quem é o SISFFAN -->
    <section class="audience-section" id="para-quem">
        <div class="audience-header">
            <div>
                <span class="section-label">Para quem é o SISFFAN</span>
                <h2>Feito pra quem precisa otimizar a rotina.</h2>
            </div>
            <div class="audience-fecho-inline">
                <strong>Não é mais um sistema de prazos,</strong><br>é a rotina inteira do seu departamento jurídico, organizada.
            </div>
        </div>

        <div class="audience-cards">

            <!-- Card 1: Advocacia -->
            <div class="audience-card">
                <span class="audience-card-num">01</span>
                <div class="audience-card-icon-wrap">
                    <svg viewBox="0 0 24 24">
                        <path d="M20 7H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/>
                        <path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/>
                        <line x1="12" y1="12" x2="12" y2="17"/>
                        <line x1="9.5" y1="14.5" x2="14.5" y2="14.5"/>
                    </svg>
                </div>
                <div class="audience-card-body">
                    <span class="audience-card-label">Advocacia</span>
                    <h3>Advogados e escritórios de advocacia</h3>
                    <p>Do profissional individual às bancas com várias equipes, com plano para cada porte.</p>
                </div>
                <div class="audience-porte">
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot"></div>
                    <span>Do solo ao escritório de grande porte</span>
                </div>
            </div>

            <!-- Card 2: Departamentos Jurídicos (destaque) -->
            <div class="audience-card">
                <span class="audience-card-num">02</span>
                <div class="audience-card-icon-wrap">
                    <svg viewBox="0 0 24 24">
                        <rect x="2" y="3" width="20" height="14" rx="2"/>
                        <path d="M8 21h8"/>
                        <path d="M12 17v4"/>
                        <path d="M7 10h2"/>
                        <path d="M11 10h6"/>
                        <path d="M7 14h2"/>
                        <path d="M11 14h6"/>
                    </svg>
                </div>
                <div class="audience-card-body">
                    <span class="audience-card-label">Corporativo</span>
                    <h3>Departamentos jurídicos</h3>
                    <p>Empresas que precisam acompanhar o preventivo e o contencioso com visão de gestão.</p>
                </div>
                <div class="audience-porte">
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <span>Preventivo + Contencioso + Relatórios</span>
                </div>
            </div>

            <!-- Card 3: Procuradorias -->
            <div class="audience-card">
                <span class="audience-card-num">03</span>
                <div class="audience-card-icon-wrap">
                    <svg viewBox="0 0 24 24">
                        <path d="M3 22V12l9-9 9 9v10"/>
                        <path d="M9 22v-7h6v7"/>
                        <path d="M3 12h18"/>
                    </svg>
                </div>
                <div class="audience-card-body">
                    <span class="audience-card-label">Setor Público</span>
                    <h3>Procuradorias</h3>
                    <p>Órgãos públicos de qualquer esfera, com grande volume de demandas e múltiplas equipes atuando juntas.</p>
                </div>
                <div class="audience-porte">
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <div class="audience-porte-dot active"></div>
                    <span>Municipal · Estadual · Federal</span>
                </div>
            </div>

        </div>
    </section>
"""

# Find where to insert it: right after `<!-- Seção 4: Antes do Processo -->` block closing tag
insert_idx = -1
for i, line in enumerate(lines):
    if 'id="antes-do-processo"' in line:
        # found start of section 4, now find its end
        for j in range(i, len(lines)):
            if "</section>" in lines[j]:
                insert_idx = j + 1
                break
        break

if insert_idx != -1:
    lines.insert(insert_idx, new_audience_html)
else:
    print("Could not find where to insert.")

with open("index.html", "w") as f:
    f.writelines(lines)
