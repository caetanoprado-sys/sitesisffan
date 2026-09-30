import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_css = """
        /* --- CSS Seção: Feito Sob Medida --- */
        .customization-section {
            padding: 120px 20px;
            background-color: var(--color-primary-dark);
            position: relative;
            overflow: hidden;
        }

        .customization-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1.1fr;
            gap: 80px;
            align-items: center;
        }

        .customization-content .section-label {
            background: rgba(193, 162, 112, 0.15);
            border: 1px solid rgba(193, 162, 112, 0.3);
            display: inline-flex;
            margin-bottom: 24px;
        }

        .customization-content h2 {
            font-family: var(--font-title);
            font-size: clamp(2.2rem, 3.5vw, 3rem);
            font-weight: 800;
            color: var(--color-white);
            margin-bottom: 24px;
            line-height: 1.15;
        }

        .customization-content p {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.7);
            line-height: 1.7;
            margin-bottom: 40px;
        }

        .custom-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .custom-tag {
            padding: 8px 16px;
            border-radius: 99px;
            border: 1px solid rgba(193, 162, 112, 0.4);
            color: var(--color-gold);
            font-size: 0.9rem;
            font-family: var(--font-title);
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            background: rgba(193, 162, 112, 0.05);
            transition: all 0.3s ease;
        }

        .custom-tag:hover {
            background: rgba(193, 162, 112, 0.15);
            border-color: var(--color-gold);
        }

        /* Testimonial Card */
        .testimonial-card {
            background: var(--color-white);
            border-radius: var(--radius-lg);
            padding: 48px;
            position: relative;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .testimonial-quote-icon {
            position: absolute;
            top: -24px;
            left: 40px;
            width: 48px;
            height: 48px;
            background: var(--color-gold);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 16px rgba(193, 162, 112, 0.3);
        }

        .testimonial-quote-icon svg {
            width: 24px;
            height: 24px;
            fill: var(--color-primary-dark);
        }

        .testimonial-text {
            font-size: 1.1rem;
            line-height: 1.7;
            color: var(--color-primary-dark);
            font-style: italic;
            margin-bottom: 32px;
            margin-top: 8px;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
            gap: 16px;
            border-top: 1px solid rgba(184, 181, 172, 0.3);
            padding-top: 24px;
        }

        .testimonial-author-img {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(193, 162, 112, 0.3);
        }

        .testimonial-author-info {
            flex: 1;
        }

        .testimonial-author-name {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--color-primary-dark);
            margin-bottom: 4px;
        }

        .testimonial-author-role {
            font-size: 0.85rem;
            color: #718096;
        }

        .testimonial-author-logo {
            max-width: 100px;
            max-height: 40px;
            object-fit: contain;
        }

        @media (max-width: 992px) {
            .customization-container {
                grid-template-columns: 1fr;
                gap: 80px;
            }
        }
"""

new_html = """
    <!-- Seção 6: Feito Sob Medida -->
    <section class="customization-section" id="feito-sob-medida">
        <div class="customization-container">
            
            <div class="customization-content">
                <span class="section-label">Feito sob medida</span>
                <h2>Se adapta à sua área do direito.</h2>
                <p>Tipologias de atos, processos, demandas, audiências e diligências configuráveis pelo próprio cliente, sem custo extra de suporte.</p>
                <div class="custom-tags">
                    <span class="custom-tag">Cível</span>
                    <span class="custom-tag">Trabalhista</span>
                    <span class="custom-tag">Penal</span>
                    <span class="custom-tag">Administrativo</span>
                </div>
            </div>

            <div class="customization-testimonial">
                <div class="testimonial-card">
                    <div class="testimonial-quote-icon">
                        <svg viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                    </div>
                    <p class="testimonial-text">"Do primeiro atendimento ao honorário recebido, o escritório inteiro roda dentro do SISFFAN. Gerenciamos tarefas, pautas, publicações com alerta de vencimento, contratos e fluxo de caixa em um só lugar. E ainda conseguimos customizar as tipologias e nomenclaturas dos atos de acordo com a área de atuação de cada equipe."</p>
                    <div class="testimonial-author">
                        <img src="fotopaulofraga.png" alt="Paulo Fraga" class="testimonial-author-img">
                        <div class="testimonial-author-info">
                            <div class="testimonial-author-name">Paulo Fraga</div>
                            <div class="testimonial-author-role">Costanza & Fiel Advocacia</div>
                        </div>
                        <img src="logocostanzaefiel.png" alt="Costanza & Fiel Logo" class="testimonial-author-logo">
                    </div>
                </div>
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

# Find end of audience section
# Since we just moved it, let's look for `id="para-quem"`
audience_start = -1
audience_end = -1
for i, line in enumerate(lines):
    if 'id="para-quem"' in line:
        audience_start = i
    if audience_start != -1 and "</section>" in line and i > audience_start:
        audience_end = i
        break

if audience_end != -1:
    lines.insert(audience_end + 1, new_html)
else:
    print("Could not find audience section end.")

with open("index.html", "w") as f:
    f.writelines(lines)
