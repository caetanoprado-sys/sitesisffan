import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_content = """    <!-- Seção 4: Antes do Processo -->
    <section class="before-process-section" id="antes-do-processo">
        <div class="before-process-container">
            
            <div class="before-process-content">
                <span class="section-label">Antes do processo</span>
                <h2>Antes do processo existir, o SISFFAN já está trabalhando.</h2>
                <p>Pareceres, contratos, consultas, respostas a ofício e assessoramento — tudo isso é rotina do escritório antes de virar processo, e a maioria dos sistemas só começa a contar história quando o processo é distribuído. No SISFFAN, a demanda já nasce registrada, com responsável e prazo — e se virar processo judicial, leva o histórico junto, sem redigitar nada.</p>
                <div class="before-process-fecho">
                    Nenhum concorrente cobre o preventivo.<br><span>É aqui que o SISFFAN se separa de "mais um sistema de prazo".</span>
                </div>
            </div>

            <div class="before-process-visual">
                <!-- Parecer / Consulta -->
                <div class="bp-card">
                    <div class="bp-card-icon">
                        <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                    </div>
                    <div class="bp-card-text">
                        <span class="bp-card-title">Parecer / Consulta</span>
                        <span class="bp-card-sub">Nasce registrada, com responsável e prazo</span>
                    </div>
                    <span class="bp-card-badge">Preventivo</span>
                </div>

                <!-- Contrato / Ofício -->
                <div class="bp-card">
                    <div class="bp-card-icon">
                        <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                    </div>
                    <div class="bp-card-text">
                        <span class="bp-card-title">Contrato / Ofício</span>
                        <span class="bp-card-sub">Histórico completo desde o início</span>
                    </div>
                    <span class="bp-card-badge">Preventivo</span>
                </div>

                <!-- Vira Processo -->
                <div class="bp-card highlight">
                    <div class="bp-card-icon" style="background: rgba(30,37,56,0.05); border-color: rgba(30,37,56,0.2);">
                        <svg viewBox="0 0 24 24" style="stroke: var(--color-primary-dark);"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                    </div>
                    <div class="bp-card-text">
                        <span class="bp-card-title">Vira processo judicial</span>
                        <span class="bp-card-sub">Leva o histórico — sem redigitar nada</span>
                    </div>
                    <span class="bp-card-badge">Judicial</span>
                </div>
            </div>

        </div>
    </section>
"""

# Replace lines 1999 to 2134 (0-indexed 1998 to 2134)
lines[1998:2134] = [new_content]

with open("index.html", "w") as f:
    f.writelines(lines)
