import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_css = """
        /* --- CSS Seção: Blog --- */
        .blog-section {
            padding: 100px 20px;
            background-color: var(--color-light-bg);
        }

        .blog-header {
            text-align: center;
            margin-bottom: 56px;
        }
        
        .blog-header .section-label {
            background: rgba(193, 162, 112, 0.1);
            border: 1px solid rgba(193, 162, 112, 0.2);
            color: var(--color-gold);
        }

        .blog-header h2 {
            font-family: var(--font-title);
            font-size: clamp(2rem, 3.2vw, 2.8rem);
            font-weight: 800;
            color: var(--color-primary-dark);
            margin-top: 20px;
            line-height: 1.15;
        }

        .blog-grid {
            max-width: 1200px;
            margin: 0 auto 48px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
        }

        .blog-card {
            background: var(--color-white);
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 1px solid rgba(184, 181, 172, 0.4);
            box-shadow: var(--shadow-sm);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
        }

        .blog-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
        }

        .blog-img {
            height: 200px;
            background: linear-gradient(135deg, var(--color-primary-dark), #2a344a);
            position: relative;
        }

        .blog-img::after {
            content: '';
            position: absolute;
            inset: 0;
            background-image: radial-gradient(circle, rgba(193, 162, 112, 0.2) 1px, transparent 1px);
            background-size: 20px 20px;
            opacity: 0.5;
        }

        .blog-content {
            padding: 24px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .blog-tag {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--color-gold);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 12px;
        }

        .blog-content h3 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--color-primary-dark);
            margin-bottom: 12px;
            line-height: 1.3;
        }

        .blog-content p {
            font-size: 0.95rem;
            color: #4A5568;
            line-height: 1.6;
            margin-bottom: 24px;
            flex: 1;
        }

        .blog-link {
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--color-primary-dark);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: color 0.3s ease;
        }

        .blog-link svg {
            width: 16px;
            height: 16px;
            stroke: currentColor;
            fill: none;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
            transition: transform 0.3s ease;
        }

        .blog-link:hover {
            color: var(--color-gold);
        }

        .blog-link:hover svg {
            transform: translateX(4px);
        }

        .blog-actions {
            text-align: center;
        }

        .btn-outline {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 16px 32px;
            border-radius: var(--radius-md);
            border: 2px solid var(--color-primary-dark);
            color: var(--color-primary-dark);
            font-family: var(--font-title);
            font-size: 1rem;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .btn-outline:hover {
            background: var(--color-primary-dark);
            color: var(--color-white);
        }

        @media (max-width: 992px) {
            .blog-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 640px) {
            .blog-grid {
                grid-template-columns: 1fr;
            }
        }
"""

new_html = """
    <!-- Seção 9: Blog -->
    <section class="blog-section" id="blog">
        <div class="blog-header">
            <span class="section-label">Blog</span>
            <h2>Conteúdo para quem vive a rotina jurídica.</h2>
        </div>

        <div class="blog-grid">
            
            <!-- Post 1 -->
            <article class="blog-card">
                <div class="blog-img"></div>
                <div class="blog-content">
                    <span class="blog-tag">Gestão Jurídica</span>
                    <h3>Como organizar a pauta diária do escritório e evitar perda de prazos</h3>
                    <p>Estratégias práticas para estruturar a rotina da sua equipe, distribuir tarefas com clareza e ter previsibilidade no consultivo e contencioso.</p>
                    <a href="#" class="blog-link">Ler artigo <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
                </div>
            </article>

            <!-- Post 2 -->
            <article class="blog-card">
                <div class="blog-img" style="background: linear-gradient(135deg, #1a2233, #3a4760);"></div>
                <div class="blog-content">
                    <span class="blog-tag">Controladoria</span>
                    <h3>O verdadeiro custo do honorário não cobrado</h3>
                    <p>Por que registrar os atos de forma automatizada e integrada à gestão financeira é o divisor de águas na lucratividade do seu escritório.</p>
                    <a href="#" class="blog-link">Ler artigo <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
                </div>
            </article>

            <!-- Post 3 -->
            <article class="blog-card">
                <div class="blog-img" style="background: linear-gradient(135deg, #0f1524, #2a344a);"></div>
                <div class="blog-content">
                    <span class="blog-tag">Tecnologia</span>
                    <h3>A matriz de risco do passivo na visão da Procuradoria</h3>
                    <p>Como apresentar dados claros e preditivos para os gestores públicos usando relatórios extraídos diretamente da sua plataforma de acompanhamento.</p>
                    <a href="#" class="blog-link">Ler artigo <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
                </div>
            </article>

        </div>

        <div class="blog-actions">
            <a href="#" class="btn-outline">Ver todos os artigos</a>
        </div>
    </section>
"""

# Inject CSS
style_idx = -1
for i, line in enumerate(lines):
    if "</style>" in line:
        style_idx = i
        break

if style_idx != -1:
    lines.insert(style_idx, new_css)

# Inject HTML after pricing section
pricing_end = -1
for i, line in enumerate(lines):
    if 'id="planos"' in line:
        pricing_start = i
    if 'pricing_start' in locals() and "</section>" in line and i > pricing_start:
        pricing_end = i
        break

if pricing_end != -1:
    lines.insert(pricing_end + 1, new_html)

with open("index.html", "w") as f:
    f.writelines(lines)
