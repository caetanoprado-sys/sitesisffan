import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_css = """
        /* --- CSS Seção 7: Social Proof (Depoimentos em Grid) --- */
        .trust-section {
            padding: 120px 20px;
            background-color: var(--color-light-bg);
            position: relative;
        }

        .trust-header {
            max-width: 800px;
            margin: 0 auto 80px;
            text-align: center;
        }

        .trust-header h2 {
            font-family: var(--font-title);
            font-size: clamp(2.2rem, 3.5vw, 3rem);
            font-weight: 800;
            color: var(--color-primary-dark);
            line-height: 1.15;
        }

        .trust-grid {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
        }

        .trust-card {
            background: var(--color-white);
            border-radius: var(--radius-lg);
            padding: 40px 32px;
            position: relative;
            box-shadow: var(--shadow-sm);
            border: 1px solid rgba(184, 181, 172, 0.4);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .trust-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
            border-color: rgba(193, 162, 112, 0.4);
        }

        .trust-quote-icon {
            position: absolute;
            top: 32px;
            right: 32px;
            opacity: 0.05;
        }
        
        .trust-quote-icon svg {
            width: 80px;
            height: 80px;
            fill: var(--color-primary-dark);
        }

        .trust-author {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
            position: relative;
            z-index: 2;
        }

        .trust-author-img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(193, 162, 112, 0.2);
        }

        .trust-author-info {
            display: flex;
            flex-direction: column;
        }

        .trust-author-name {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 1rem;
            color: var(--color-primary-dark);
            margin-bottom: 2px;
        }

        .trust-author-role {
            font-size: 0.85rem;
            color: #718096;
            line-height: 1.3;
        }

        .trust-text {
            font-size: 1rem;
            color: #4A5568;
            line-height: 1.7;
            font-style: italic;
            position: relative;
            z-index: 1;
        }

        @media (max-width: 1024px) {
            .trust-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .trust-grid {
                grid-template-columns: 1fr;
            }
        }
"""

new_html = """
    <!-- Seção 7: Trust / Depoimentos em Grid -->
    <section class="trust-section" id="depoimentos">
        <div class="trust-header">
            <h2>No mercado desde 2018. Na rotina de quem confia.</h2>
        </div>

        <div class="trust-grid">
            
            <!-- Card 1 -->
            <div class="trust-card">
                <div class="trust-quote-icon">
                    <svg viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                </div>
                <div class="trust-author">
                    <img src="Rodrigo Moraes - foto.jpeg" alt="Rodrigo Silva" class="trust-author-img">
                    <div class="trust-author-info">
                        <span class="trust-author-name">Rodrigo Silva</span>
                        <span class="trust-author-role">Postos RPB</span>
                    </div>
                </div>
                <p class="trust-text">"Acompanho, em tempo real, tudo o que o Jurídico executa para o grupo, tanto no consultivo quanto no contencioso. Sei em que etapa está cada demanda sem precisar solicitar atualizações à equipe."</p>
            </div>

            <!-- Card 2 -->
            <div class="trust-card">
                <div class="trust-quote-icon">
                    <svg viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                </div>
                <div class="trust-author">
                    <img src="JOSEANE - ADVOGADA E PROCURADORA UMBAUBA.jpeg" alt="Joseane dos Santos" class="trust-author-img">
                    <div class="trust-author-info">
                        <span class="trust-author-name">Joseane dos Santos</span>
                        <span class="trust-author-role">Procuradoria Municipal</span>
                    </div>
                </div>
                <p class="trust-text">"Os relatórios e gráficos que apresento ao gestor do município e aos meus clientes saem prontos da plataforma, além das publicações e comunicações do domicílio judicial chegarem direto na plataforma."</p>
            </div>

            <!-- Card 3 -->
            <div class="trust-card">
                <div class="trust-quote-icon">
                    <svg viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                </div>
                <div class="trust-author">
                    <img src="BRUNA ARAGAO - ADVOGADA E PROCURADORA ITAPORANGA.jpeg" alt="Bruna Aragão Barroso" class="trust-author-img">
                    <div class="trust-author-info">
                        <span class="trust-author-name">Bruna Aragão Barroso</span>
                        <span class="trust-author-role">Procuradoria Municipal</span>
                    </div>
                </div>
                <p class="trust-text">"Na Procuradoria, delego tarefas aos servidores e acompanho, em um único ambiente, os prazos dos órgãos de controle, as respostas a ofícios, os pareceres e todo o contencioso do município."</p>
            </div>

        </div>
    </section>
"""

# Find </style>
style_idx = -1
for i, line in enumerate(lines):
    if "</style>" in line:
        style_idx = i
        break

if style_idx != -1:
    lines.insert(style_idx, new_css)
else:
    print("Could not find </style>.")

# Find end of customization section
cust_start = -1
cust_end = -1
for i, line in enumerate(lines):
    if 'id="feito-sob-medida"' in line:
        cust_start = i
    if cust_start != -1 and "</section>" in line and i > cust_start:
        cust_end = i
        break

if cust_end != -1:
    lines.insert(cust_end + 1, new_html)
else:
    print("Could not find customization section end.")

with open("index.html", "w") as f:
    f.writelines(lines)
