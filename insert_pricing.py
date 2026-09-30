import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_css = """
        /* --- CSS Seção: Planos & Contato --- */
        .pricing-section {
            padding: 120px 20px 0;
            background: linear-gradient(165deg, #2a1a0e 0%, #1E2538 35%, #1E2538 100%);
            position: relative;
            overflow: hidden;
        }

        .pricing-section::before {
            content: '';
            position: absolute;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(193, 162, 112, 0.08) 0%, transparent 70%);
            top: -200px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 0;
            pointer-events: none;
        }

        .pricing-header {
            max-width: 800px;
            margin: 0 auto 72px;
            text-align: center;
            position: relative;
            z-index: 1;
        }

        .pricing-header .section-label {
            background: rgba(193, 162, 112, 0.15);
            border: 1px solid rgba(193, 162, 112, 0.3);
        }

        .pricing-header h2 {
            font-family: var(--font-title);
            font-size: clamp(2.2rem, 3.5vw, 3rem);
            font-weight: 800;
            color: var(--color-white);
            line-height: 1.15;
            margin-top: 20px;
        }

        .pricing-header p {
            font-size: 1rem;
            color: rgba(255,255,255,0.5);
            margin-top: 16px;
        }

        /* Pricing Cards Grid */
        .pricing-grid {
            max-width: 1280px;
            margin: 0 auto 80px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            position: relative;
            z-index: 1;
        }

        .pricing-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: var(--radius-lg);
            padding: 32px 28px;
            backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
            position: relative;
        }

        .pricing-card:hover {
            transform: translateY(-5px);
            border-color: rgba(193, 162, 112, 0.3);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        .pricing-card.featured {
            border-color: rgba(193, 162, 112, 0.4);
            background: rgba(193, 162, 112, 0.08);
        }

        .pricing-card-badge {
            position: absolute;
            top: -14px;
            left: 50%;
            transform: translateX(-50%);
            white-space: nowrap;
            padding: 6px 18px;
            background: var(--color-gold);
            color: var(--color-primary-dark);
            font-family: var(--font-title);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            border-radius: 99px;
        }

        .pricing-card-name {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--color-white);
            padding-left: 14px;
            border-left: 3px solid var(--color-gold);
            margin-bottom: 24px;
            line-height: 1.3;
        }

        .pricing-card-from {
            font-size: 0.82rem;
            color: rgba(255,255,255,0.45);
            margin-bottom: 8px;
        }

        .pricing-card-price {
            display: flex;
            align-items: baseline;
            gap: 2px;
            margin-bottom: 24px;
        }

        .pricing-card-price .currency {
            font-family: var(--font-title);
            font-size: 1rem;
            font-weight: 700;
            color: var(--color-white);
        }

        .pricing-card-price .amount {
            font-family: var(--font-title);
            font-size: 2.8rem;
            font-weight: 800;
            color: var(--color-white);
            line-height: 1;
        }

        .pricing-card-price .cents {
            font-family: var(--font-title);
            font-size: 1.2rem;
            font-weight: 700;
            color: rgba(255,255,255,0.6);
        }

        .pricing-card-features {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .pricing-card-features li {
            font-size: 0.9rem;
            color: rgba(255,255,255,0.65);
            padding-left: 18px;
            position: relative;
        }

        .pricing-card-features li::before {
            content: '+';
            position: absolute;
            left: 0;
            color: var(--color-gold);
            font-weight: 700;
        }

        /* Card de Plano sob medida */
        .pricing-card.custom-plan {
            border-style: dashed;
            border-color: rgba(193, 162, 112, 0.25);
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .custom-plan-icon {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: rgba(193, 162, 112, 0.1);
            border: 1px solid rgba(193, 162, 112, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
        }

        .custom-plan-icon svg {
            width: 28px;
            height: 28px;
            stroke: var(--color-gold);
            fill: none;
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .custom-plan-title {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--color-white);
            margin-bottom: 8px;
        }

        .custom-plan-desc {
            font-size: 0.9rem;
            color: rgba(255,255,255,0.5);
        }

        /* Incluso strip */
        .pricing-includes {
            max-width: 1280px;
            margin: 0 auto 100px;
            position: relative;
            z-index: 1;
        }

        .pricing-includes-title {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 0.85rem;
            color: var(--color-gold);
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 20px;
            text-align: center;
        }

        .pricing-includes-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }

        .pricing-includes-tag {
            padding: 8px 18px;
            border-radius: 99px;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            color: rgba(255,255,255,0.7);
            font-size: 0.85rem;
            font-weight: 500;
        }

        /* Adicionais */
        .pricing-addons {
            max-width: 1280px;
            margin: 0 auto 100px;
            position: relative;
            z-index: 1;
        }

        .pricing-addons-title {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 0.85rem;
            color: rgba(255,255,255,0.45);
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 20px;
            text-align: center;
        }

        .pricing-addons-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }

        .pricing-addons-tag {
            padding: 10px 20px;
            border-radius: var(--radius-md);
            background: rgba(193, 162, 112, 0.06);
            border: 1px solid rgba(193, 162, 112, 0.2);
            color: var(--color-gold);
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .pricing-addons-tag:hover {
            background: rgba(193, 162, 112, 0.12);
            border-color: rgba(193, 162, 112, 0.4);
        }

        /* Implementação - 5 passos */
        .implementation-block {
            max-width: 1200px;
            margin: 0 auto 120px;
            position: relative;
            z-index: 1;
        }

        .implementation-header {
            text-align: center;
            margin-bottom: 64px;
        }

        .implementation-header h3 {
            font-family: var(--font-title);
            font-size: clamp(1.8rem, 2.5vw, 2.4rem);
            font-weight: 800;
            color: var(--color-white);
        }

        .implementation-steps {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 16px;
            position: relative;
        }

        /* Connector line behind steps */
        .implementation-steps::before {
            content: '';
            position: absolute;
            top: 40px;
            left: 40px;
            right: 40px;
            height: 2px;
            background: linear-gradient(to right, var(--color-gold), rgba(193, 162, 112, 0.15));
            z-index: 0;
        }

        .impl-step {
            text-align: center;
            position: relative;
            z-index: 1;
        }

        .impl-step-num {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: var(--color-primary-dark);
            border: 2px solid rgba(193, 162, 112, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            font-family: var(--font-title);
            font-weight: 800;
            font-size: 1.1rem;
            color: var(--color-gold);
            transition: all 0.3s ease;
        }

        .impl-step:hover .impl-step-num {
            background: var(--color-gold);
            color: var(--color-primary-dark);
            box-shadow: 0 0 20px rgba(193, 162, 112, 0.3);
        }

        .impl-step-title {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 0.95rem;
            color: var(--color-white);
            margin-bottom: 8px;
        }

        .impl-step-desc {
            font-size: 0.82rem;
            color: rgba(255,255,255,0.5);
            line-height: 1.5;
        }

        /* CTA + Form */
        .cta-block {
            background: var(--color-white);
            border-radius: 24px 24px 0 0;
            padding: 100px 20px 80px;
            position: relative;
            z-index: 1;
        }

        .cta-container {
            max-width: 1100px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: start;
        }

        .cta-content h2 {
            font-family: var(--font-title);
            font-size: clamp(2rem, 3vw, 2.8rem);
            font-weight: 800;
            color: var(--color-primary-dark);
            margin-bottom: 28px;
            line-height: 1.15;
        }

        .cta-content p {
            font-size: 1.05rem;
            color: #4A5568;
            line-height: 1.7;
            margin-bottom: 40px;
        }

        .cta-contact-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .cta-contact-item {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .cta-contact-item svg {
            width: 20px;
            height: 20px;
            stroke: var(--color-gold);
            fill: none;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
            flex-shrink: 0;
        }

        .cta-contact-item span {
            font-size: 1rem;
            color: var(--color-primary-dark);
            font-weight: 500;
        }

        .cta-contact-item a {
            color: var(--color-primary-dark);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .cta-contact-item a:hover {
            color: var(--color-gold);
        }

        /* Form */
        .cta-form {
            background: var(--color-light-bg);
            padding: 48px;
            border-radius: var(--radius-lg);
            border: 1px solid rgba(184, 181, 172, 0.3);
        }

        .cta-form-title {
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 1.2rem;
            color: var(--color-primary-dark);
            margin-bottom: 28px;
        }

        .cta-form-group {
            margin-bottom: 18px;
        }

        .cta-form-group label {
            display: block;
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--color-primary-dark);
            margin-bottom: 6px;
        }

        .cta-form-group input,
        .cta-form-group textarea {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid rgba(184, 181, 172, 0.5);
            border-radius: var(--radius-md);
            background: var(--color-white);
            font-family: var(--font-body);
            font-size: 0.95rem;
            color: var(--color-primary-dark);
            outline: none;
            transition: border-color 0.3s ease;
            box-sizing: border-box;
        }

        .cta-form-group input:focus,
        .cta-form-group textarea:focus {
            border-color: var(--color-gold);
        }

        .cta-form-group textarea {
            resize: vertical;
            min-height: 100px;
        }

        .cta-form-submit {
            width: 100%;
            padding: 16px;
            background: var(--color-primary-dark);
            color: var(--color-white);
            border: none;
            border-radius: var(--radius-md);
            font-family: var(--font-title);
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 8px;
        }

        .cta-form-submit:hover {
            background: var(--color-gold);
            color: var(--color-primary-dark);
        }

        @media (max-width: 1100px) {
            .pricing-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .implementation-steps {
                grid-template-columns: repeat(3, 1fr);
                row-gap: 40px;
            }
            .implementation-steps::before {
                display: none;
            }
        }

        @media (max-width: 768px) {
            .pricing-grid {
                grid-template-columns: 1fr;
            }
            .implementation-steps {
                grid-template-columns: repeat(2, 1fr);
            }
            .cta-container {
                grid-template-columns: 1fr;
                gap: 60px;
            }
        }
"""

new_html = """
    <!-- Seção 8: Planos & Contato -->
    <section class="pricing-section" id="planos">
        <div class="pricing-header">
            <span class="section-label">Nossos planos</span>
            <h2>Nossos planos</h2>
            <p>Valores mensais · Sem fidelidade</p>
        </div>

        <div class="pricing-grid">
            <!-- Single -->
            <div class="pricing-card">
                <div class="pricing-card-name">Single</div>
                <span class="pricing-card-from">A partir de</span>
                <div class="pricing-card-price">
                    <span class="currency">R$</span>
                    <span class="amount">99</span>
                    <span class="cents">,90</span>
                </div>
                <ul class="pricing-card-features">
                    <li>até 2 usuários</li>
                    <li>até 100 processos</li>
                </ul>
            </div>

            <!-- Intermediário I -->
            <div class="pricing-card">
                <div class="pricing-card-name">Intermediário I</div>
                <span class="pricing-card-from">A partir de</span>
                <div class="pricing-card-price">
                    <span class="currency">R$</span>
                    <span class="amount">389</span>
                    <span class="cents">,90</span>
                </div>
                <ul class="pricing-card-features">
                    <li>até 8 usuários</li>
                    <li>até 1.000 processos</li>
                </ul>
            </div>

            <!-- Intermediário II (Destaque) -->
            <div class="pricing-card featured">
                <span class="pricing-card-badge">Mais procurado</span>
                <div class="pricing-card-name">Intermediário II</div>
                <span class="pricing-card-from">A partir de</span>
                <div class="pricing-card-price">
                    <span class="currency">R$</span>
                    <span class="amount">729</span>
                    <span class="cents">,90</span>
                </div>
                <ul class="pricing-card-features">
                    <li>usuários ilimitados</li>
                    <li>até 2.000 processos</li>
                </ul>
            </div>

            <!-- Premium -->
            <div class="pricing-card">
                <div class="pricing-card-name">Premium</div>
                <span class="pricing-card-from">A partir de</span>
                <div class="pricing-card-price">
                    <span class="currency">R$</span>
                    <span class="amount">919</span>
                    <span class="cents">,90</span>
                </div>
                <ul class="pricing-card-features">
                    <li>usuários ilimitados</li>
                    <li>até 3.000 processos</li>
                </ul>
            </div>
        </div>

        <!-- Plano sob medida -->
        <div class="pricing-grid" style="grid-template-columns: 1fr; max-width: 440px; margin-bottom: 80px;">
            <div class="pricing-card custom-plan">
                <div class="custom-plan-icon">
                    <svg viewBox="0 0 24 24"><path d="M12 20V10"/><path d="M18 20V4"/><path d="M6 20v-4"/></svg>
                </div>
                <div class="custom-plan-title">Acima de 3.000 processos?</div>
                <div class="custom-plan-desc">Plano desenhado sob medida para a sua operação.</div>
            </div>
        </div>

        <!-- O que os planos já incluem -->
        <div class="pricing-includes">
            <div class="pricing-includes-title">Já incluído em todos os planos</div>
            <div class="pricing-includes-tags">
                <span class="pricing-includes-tag">Atendimento</span>
                <span class="pricing-includes-tag">Prazos</span>
                <span class="pricing-includes-tag">Audiências</span>
                <span class="pricing-includes-tag">Finanças</span>
                <span class="pricing-includes-tag">Acervo</span>
                <span class="pricing-includes-tag">Relatórios</span>
                <span class="pricing-includes-tag">Integração de calendário</span>
            </div>
        </div>

        <!-- Adicionais -->
        <div class="pricing-addons">
            <div class="pricing-addons-title">Adicionais disponíveis em qualquer plano</div>
            <div class="pricing-addons-tags">
                <span class="pricing-addons-tag">Domicílio Judicial</span>
                <span class="pricing-addons-tag">Integração de Publicações</span>
                <span class="pricing-addons-tag">Gestão de Pautistas</span>
                <span class="pricing-addons-tag">Plataforma do Cliente</span>
                <span class="pricing-addons-tag">Plataforma do Pautista</span>
            </div>
        </div>

        <!-- Implementação -->
        <div class="implementation-block">
            <div class="implementation-header">
                <h3>Implementação em 5 passos.</h3>
            </div>
            <div class="implementation-steps">
                <div class="impl-step">
                    <div class="impl-step-num">1</div>
                    <div class="impl-step-title">Contato</div>
                    <div class="impl-step-desc">Por telefone, WhatsApp, e-mail ou presencialmente.</div>
                </div>
                <div class="impl-step">
                    <div class="impl-step-num">2</div>
                    <div class="impl-step-title">Pacote e domínio</div>
                    <div class="impl-step-desc">Você escolhe o plano conforme o tamanho da equipe.</div>
                </div>
                <div class="impl-step">
                    <div class="impl-step-num">3</div>
                    <div class="impl-step-title">Capacitação</div>
                    <div class="impl-step-desc">Configuração durante o próprio treinamento.</div>
                </div>
                <div class="impl-step">
                    <div class="impl-step-num">4</div>
                    <div class="impl-step-title">90 dias ao seu lado</div>
                    <div class="impl-step-desc">Até o uso estar fluido.</div>
                </div>
                <div class="impl-step">
                    <div class="impl-step-num">5</div>
                    <div class="impl-step-title">Rotina em uso</div>
                    <div class="impl-step-desc">Acompanhamento contínuo.</div>
                </div>
            </div>
        </div>

        <!-- CTA + Formulário -->
        <div class="cta-block">
            <div class="cta-container">
                <div class="cta-content">
                    <h2>Quer ver funcionando?<br>Agende uma demonstração.</h2>
                    <p>Fale com a gente pelo canal que preferir. Mostramos o sistema rodando de verdade, com a rotina do seu escritório.</p>

                    <div class="cta-contact-list">
                        <div class="cta-contact-item">
                            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            <a href="https://sisffan.com.br" target="_blank">sisffan.com.br</a>
                        </div>
                        <div class="cta-contact-item">
                            <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                            <a href="mailto:contato@sisffan.com.br">contato@sisffan.com.br</a>
                        </div>
                        <div class="cta-contact-item">
                            <svg viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"/></svg>
                            <a href="https://instagram.com/sisffan" target="_blank">@sisffan</a>
                        </div>
                    </div>
                </div>

                <div class="cta-form">
                    <div class="cta-form-title">Solicite uma demonstração</div>
                    <div class="cta-form-group">
                        <label>Nome</label>
                        <input type="text" placeholder="Seu nome completo">
                    </div>
                    <div class="cta-form-group">
                        <label>E-mail</label>
                        <input type="email" placeholder="seu@email.com">
                    </div>
                    <div class="cta-form-group">
                        <label>Telefone</label>
                        <input type="tel" placeholder="(00) 00000-0000">
                    </div>
                    <div class="cta-form-group">
                        <label>Mensagem</label>
                        <textarea placeholder="Conte um pouco sobre sua operação..."></textarea>
                    </div>
                    <button class="cta-form-submit">Agendar demonstração</button>
                </div>
            </div>
        </div>
    </section>
"""

# Find </style> and inject CSS before it
style_idx = -1
for i, line in enumerate(lines):
    if "</style>" in line:
        style_idx = i
        break

if style_idx != -1:
    lines.insert(style_idx, new_css)
else:
    print("Could not find </style>.")
    sys.exit(1)

# Find end of trust/depoimentos section and insert HTML after it
trust_start = -1
trust_end = -1
for i, line in enumerate(lines):
    if 'id="depoimentos"' in line:
        trust_start = i
    if trust_start != -1 and "</section>" in line and i > trust_start:
        trust_end = i
        break

if trust_end != -1:
    lines.insert(trust_end + 1, new_html)
else:
    print("Could not find depoimentos section end.")
    sys.exit(1)

with open("index.html", "w") as f:
    f.writelines(lines)

print("Done!")
