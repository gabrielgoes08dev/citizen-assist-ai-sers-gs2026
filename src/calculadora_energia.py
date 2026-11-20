"""
Citizen Assist AI - Módulo de Soluções em Energias Renováveis e Sustentáveis (SERS)
Motor de cálculo de consumo residencial, custos, payback e emissões de CO2.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS_DIR = os.path.join(BASE_DIR, "dados")


def carregar_dados():
    with open(os.path.join(DADOS_DIR, "consumo_residencial_base.json"), "r", encoding="utf-8") as f:
        consumo = json.load(f)
    with open(os.path.join(DADOS_DIR, "tarifas_e_premissas.json"), "r", encoding="utf-8") as f:
        tarifas = json.load(f)
    return consumo, tarifas


def calcular_cenario_base(consumo_data, tarifas_data):
    tarifa = tarifas_data["tarifa_residencial_b1_com_impostos_brl_kwh"]
    fator_co2 = tarifas_data["fator_emissao_sin_kg_co2_por_kwh"]
    total_kwh = sum(item["consumo_kwh_mes"] for item in consumo_data["equipamentos"])
    custo_mensal = total_kwh * tarifa
    co2_mensal = total_kwh * fator_co2

    ranking = sorted(
        consumo_data["equipamentos"],
        key=lambda x: x["consumo_kwh_mes"],
        reverse=True
    )
    return {
        "consumo_kwh_mes": round(total_kwh, 2),
        "custo_mensal_brl": round(custo_mensal, 2),
        "co2_mensal_kg": round(co2_mensal, 2),
        "ranking_equipamentos": ranking
    }


def comparar_alternativas(consumo_kwh_mes=300.60, tipo_moradia="apartamento", padrao_rede="bifasico", tarifas_data=None):
    if tarifas_data is None:
        _, tarifas_data = carregar_dados()

    tarifa = tarifas_data["tarifa_residencial_b1_com_impostos_brl_kwh"]
    fator_co2 = tarifas_data["fator_emissao_sin_kg_co2_por_kwh"]
    meses = tarifas_data["horizonte_analise_meses"]
    custo_base_mensal = consumo_kwh_mes * tarifa

    taxa_minima_kwh = (
        tarifas_data["custo_disponibilidade_monofasico_kwh"]
        if padrao_rede == "monofasico"
        else tarifas_data["custo_disponibilidade_bifasico_kwh"]
    )

    # Alternativa A: Eficiência Energética (Chuveiro 8 min + Lâmpadas LED)
    # Proporcional ao consumo informado (base 70.95 kWh em 300.60 kWh -> ~23.6% de economia)
    fator_escala = consumo_kwh_mes / 300.60
    economia_kwh_a = round(70.95 * fator_escala, 2)
    economia_mensal_a = round(economia_kwh_a * tarifa, 2)
    investimento_a = 96.00
    payback_a = round(investimento_a / economia_mensal_a, 1) if economia_mensal_a > 0 else 0
    saldo_5_anos_a = round((economia_mensal_a * meses) - investimento_a, 2)
    co2_evitado_5_anos_a = round(economia_kwh_a * meses * fator_co2, 2)

    # Alternativa B: Energia Solar por Assinatura (Renovável - Geração Compartilhada)
    kwh_compensavel_b = max(0.0, consumo_kwh_mes - taxa_minima_kwh)
    desconto_b = tarifas_data["premissas_alternativas"]["alternativa_b_solar_assinatura"]["percentual_desconto_sobre_energia_compensada"]
    economia_mensal_b = round(kwh_compensavel_b * tarifa * desconto_b, 2)
    investimento_b = 0.00
    saldo_5_anos_b = round(economia_mensal_b * meses, 2)
    co2_evitado_5_anos_b = round(kwh_compensavel_b * meses * fator_co2, 2)

    # Alternativa C: Energia Solar Própria On-Grid (Renovável - Telhado)
    geracao_c = min(consumo_kwh_mes - taxa_minima_kwh, 235.0 * fator_escala)
    geracao_c = max(0.0, round(geracao_c, 2))
    # Considerando ~93% de aproveitamento líquido após encargos Fio B (Lei 14.300)
    economia_mensal_c = round(geracao_c * tarifa * 0.93, 2)
    investimento_c = round(9800.00 * max(0.7, fator_escala), 2)
    manutencao_5_anos_c = 750.00
    payback_c = round(investimento_c / economia_mensal_c, 1) if economia_mensal_c > 0 else 999
    saldo_5_anos_c = round((economia_mensal_c * meses) - investimento_c - manutencao_5_anos_c, 2)
    co2_evitado_5_anos_c = round(geracao_c * meses * fator_co2, 2)

    return {
        "parametros": {
            "consumo_kwh_mes": consumo_kwh_mes,
            "custo_base_mensal_brl": round(custo_base_mensal, 2),
            "tipo_moradia": tipo_moradia,
            "padrao_rede": padrao_rede,
            "horizonte_meses": meses
        },
        "alternativas": [
            {
                "codigo": "A",
                "nome": "Eficiência Energética e Hábito (Banho 8 min + Lâmpadas LED)",
                "tipo": "Eficiência Energética",
                "viavel_para_moradia": True,
                "investimento_inicial_brl": investimento_a,
                "economia_mensal_brl": economia_mensal_a,
                "payback_meses": payback_a,
                "saldo_liquido_5_anos_brl": saldo_5_anos_a,
                "co2_evitado_5_anos_kg": co2_evitado_5_anos_a,
                "limitacoes": "Depende da disciplina dos moradores no tempo de banho e potência do chuveiro."
            },
            {
                "codigo": "B",
                "nome": "Energia Solar por Assinatura (Geração Compartilhada)",
                "tipo": "Fonte Renovável (Solar Remota)",
                "viavel_para_moradia": consumo_kwh_mes >= 150,
                "investimento_inicial_brl": investimento_b,
                "economia_mensal_brl": economia_mensal_b,
                "payback_meses": 0.0,
                "saldo_liquido_5_anos_brl": saldo_5_anos_b,
                "co2_evitado_5_anos_kg": co2_evitado_5_anos_b,
                "limitacoes": "Exige consumo mínimo (~150 kWh/mês), não zera a taxa mínima da distribuidora e possui fidelidade contratual."
            },
            {
                "codigo": "C",
                "nome": "Sistema Solar Fotovoltaico Próprio On-Grid (Telhado)",
                "tipo": "Fonte Renovável (Solar Local)",
                "viavel_para_moradia": (tipo_moradia.lower() == "casa"),
                "investimento_inicial_brl": investimento_c,
                "economia_mensal_brl": economia_mensal_c,
                "payback_meses": payback_c,
                "saldo_liquido_5_anos_brl": saldo_5_anos_c,
                "co2_evitado_5_anos_kg": co2_evitado_5_anos_c,
                "limitacoes": "Inviável para apartamentos individuais; exige telhado próprio sem sombra, capital inicial e incide Fio B (Lei 14.300)."
            }
        ]
    }


if __name__ == "__main__":
    consumo, tarifas = carregar_dados()
    base = calcular_cenario_base(consumo, tarifas)
    print("=== CENÁRIO BASE RESIDENCIAL (ESTIMADO - PROCEL / ENEL SP) ===")
    print(f"Consumo Total: {base['consumo_kwh_mes']} kWh/mês | Custo Estimado: R$ {base['custo_mensal_brl']}/mês")
    print("
Top 3 maiores consumidores da residência:")
    for eq in base["ranking_equipamentos"][:3]:
        pct = (eq["consumo_kwh_mes"] / base["consumo_kwh_mes"]) * 100
        print(f" - {eq['nome']}: {eq['consumo_kwh_mes']} kWh/mês ({pct:.1f}%)")

    print("
=== COMPARAÇÃO DE ALTERNATIVAS (HORIZONTE: 5 ANOS) ===")
    resultado = comparar_alternativas(consumo_kwh_mes=base["consumo_kwh_mes"], tipo_moradia="apartamento", padrao_rede="bifasico", tarifas_data=tarifas)
    for alt in resultado["alternativas"]:
        status = "Viável" if alt["viavel_para_moradia"] else "Não indicado p/ apartamento"
        print(f"
[{alt['codigo']}] {alt['nome']} ({alt['tipo']}) -> {status}")
        print(f"    Investimento: R$ {alt['investimento_inicial_brl']:.2f} | Economia/mês: R$ {alt['economia_mensal_brl']:.2f} | Payback: {alt['payback_meses']} meses")
        print(f"    Saldo líquido em 5 anos: R$ {alt['saldo_liquido_5_anos_brl']:.2f} | CO2 evitado: {alt['co2_evitado_5_anos_kg']:.2f} kg")
