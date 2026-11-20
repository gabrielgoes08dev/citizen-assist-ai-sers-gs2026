"""
Citizen Assist AI - Assistente Digital de Orientação Energética e Sustentabilidade
Integra a análise de dados, cálculos de consumo e comparação de fontes renováveis
às respostas oferecidas ao cidadão, explicitando fontes e limitações.
"""

from calculadora_energia import carregar_dados, calcular_cenario_base, comparar_alternativas

REFERENCIAS_TEXTO = (
    "Fontes utilizadas: PROCEL/Eletrobras (potência e consumo médio), "
    "Enel SP (tarifa residencial B1 estimada em R$ 0,88/kWh), "
    "MCTI (fator de emissão SIN: 0,058 kg CO2/kWh) e Lei 14.300/2022 (Marco Legal da Geração Distribuída)."
)

AVISO_LIMITACOES = (
    "Condições e limitações: Os valores apresentados são estimativas baseadas em perfis médios de uso "
    "e tarifas vigentes em São Paulo, não constituindo garantia financeira. O retorno real depende "
    "dos hábitos da família, temperatura ambiente, bandeiras tarifárias da ANEEL e regras contratuais."
)


def responder_consulta(pergunta_usuario, consumo_kwh=300.60, moradia="apartamento", padrao="bifasico"):
    pergunta = pergunta_usuario.lower()
    consumo_data, tarifas_data = carregar_dados()
    base = calcular_cenario_base(consumo_data, tarifas_data)
    comp = comparar_alternativas(consumo_kwh, moradia, padrao, tarifas_data)

    resposta = []
    resposta.append("=" * 72)
    resposta.append("CITIZEN ASSIST AI — ORIENTAÇÃO SOBRE ENERGIA E SUSTENTABILIDADE")
    resposta.append("=" * 72)

    if any(p in pergunta for p in ["chuveiro", "aparelho", "gasta mais", "vilao", "vilão", "consumo"]):
        resposta.append("DIAGNÓSTICO DE CONSUMO RESIDENCIAL (Base: 3 moradores / 300,60 kWh/mês):")
        for i, eq in enumerate(base["ranking_equipamentos"][:5], start=1):
            pct = (eq["consumo_kwh_mes"] / base["consumo_kwh_mes"]) * 100
            custo_eq = eq["consumo_kwh_mes"] * tarifas_data["tarifa_residencial_b1_com_impostos_brl_kwh"]
            resposta.append(f"  {i}. {eq['nome']}: {eq['consumo_kwh_mes']} kWh/mês (~R$ {custo_eq:.2f} | {pct:.1f}% da conta)")
        resposta.append("
Dica prática imediata:")
        resposta.append("  - Reduzir o banho de 15 min para 8 min por pessoa economiza ~57,75 kWh/mês (R$ 50,82/mês).")
        resposta.append("  - Mudar a chave do chuveiro de 'Inverno' (5.500W) para 'Verão' (~3.200W) reduz em ~35% o gasto por minuto.")

    elif any(p in pergunta for p in ["solar", "apartamento", "renovavel", "renovável", "painel", "placa", "comparar", "vale a pena"]):
        resposta.append(f"ANÁLISE COMPARATIVA PARA {moradia.upper()} (Consumo: {consumo_kwh:.1f} kWh/mês | Custo est.: R$ {comp['parametros']['custo_base_mensal_brl']:.2f}/mês):")
        for alt in comp["alternativas"]:
            viabilidade = "RECOMENDADA" if alt["viavel_para_moradia"] else "NÃO INDICADA PARA ESTE IMÓVEL"
            resposta.append(f"
  [{alt['codigo']}] {alt['nome']} — [{viabilidade}]")
            resposta.append(f"      • Investimento inicial: R$ {alt['investimento_inicial_brl']:.2f}")
            resposta.append(f"      • Economia estimada: R$ {alt['economia_mensal_brl']:.2f}/mês (Payback: {alt['payback_meses']} meses)")
            resposta.append(f"      • Resultado líquido em 5 anos: R$ {alt['saldo_liquido_5_anos_brl']:.2f}")
            resposta.append(f"      • Impacto ambiental: {alt['co2_evitado_5_anos_kg']:.2f} kg de CO2 evitados em 5 anos")
            resposta.append(f"      • Condição/Limitação: {alt['limitacoes']}")

        if moradia.lower() == "apartamento":
            resposta.append("
Recomendação do Assistente para Apartamento:")
            resposta.append("  Combine a Alternativa A (Eficiência no chuveiro + LED) com a Alternativa B (Energia Solar por Assinatura).")
            resposta.append("  Você reduz o desperdício dentro de casa e ainda usa energia limpa sem precisar de telhado ou obras.")
        else:
            resposta.append("
Recomendação do Assistente para Casa Própria:")
            resposta.append("  Comece pela Alternativa A (retorno em ~1,5 mês) e avalie a Alternativa C (Solar Próprio) se tiver capital")
            resposta.append("  para investir visando retorno de longo prazo (25 anos de vida útil dos painéis).")

    else:
        resposta.append(f"RESUMO GERAL PARA SEU PERFIL ({moradia.capitalize()} | {consumo_kwh:.1f} kWh/mês):")
        resposta.append("  1. Eficiência Energética (Banho 8 min + LED): economia de R$ {:.2f}/mês com investimento de R$ 96,00.".format(
            comp["alternativas"][0]["economia_mensal_brl"]
        ))
        resposta.append("  2. Energia Solar por Assinatura (Renovável): economia de R$ {:.2f}/mês sem investir nada.".format(
            comp["alternativas"][1]["economia_mensal_brl"]
        ))
        resposta.append("  3. Energia Solar Própria no Telhado (Renovável): economia de R$ {:.2f}/mês (indicado apenas para casas próprias).".format(
            comp["alternativas"][2]["economia_mensal_brl"]
        ))

    resposta.append("
" + "-" * 72)
    resposta.append(REFERENCIAS_TEXTO)
    resposta.append(AVISO_LIMITACOES)
    resposta.append("=" * 72)
    return "
".join(resposta)


def executar_demo():
    print("
>>> DEMONSTRAÇÃO AUTOMÁTICA DO CITIZEN ASSIST AI (MÓDULO ENERGIA) <<<
")
    exemplos = [
        ("Quais aparelhos gastam mais energia na minha casa?", 300.60, "apartamento", "bifasico"),
        ("Moro em apartamento e gasto 300 kWh, vale a pena energia solar?", 300.60, "apartamento", "bifasico"),
        ("Tenho casa própria e gasto 350 kWh, compensa instalar painel solar?", 350.00, "casa", "bifasico"),
    ]
    for pergunta, kwh, moradia, padrao in exemplos:
        print(f"PERGUNTA DO CIDADÃO: "{pergunta}"")
        print(responder_consulta(pergunta, kwh, moradia, padrao))
        print("
")


if __name__ == "__main__":
    executar_demo()
    while True:
        opcao = input("Deseja fazer uma consulta personalizada? (s/n): ").strip().lower()
        if opcao != "s":
            print("Encerrando Citizen Assist AI - Módulo Energia. Até logo!")
            break
        pergunta_user = input("Digite sua dúvida sobre energia: ").strip()
        moradia_user = input("Você mora em 'casa' ou 'apartamento'? ").strip().lower()
        if moradia_user not in ["casa", "apartamento"]:
            moradia_user = "apartamento"
        padrao_user = input("Seu relógio é 'monofasico' (30 kWh) ou 'bifasico' (50 kWh)? ").strip().lower()
        if padrao_user not in ["monofasico", "bifasico"]:
            padrao_user = "bifasico"
        try:
            kwh_user = float(input("Qual seu consumo médio mensal em kWh (ex: 300)? ").strip().replace(",", "."))
        except ValueError:
            kwh_user = 300.60
        print("
" + responder_consulta(pergunta_user, kwh_user, moradia_user, padrao_user) + "
")
