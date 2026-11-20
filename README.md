# Citizen Assist AI - Módulo de Eficiência Energética e Energias Renováveis (SERS)

**Disciplina:** Soluções em Energias Renováveis e Sustentáveis (1CC - Global Solution 2026.2)  
**Instituição:** FIAP - Faculdade de Informática e Administração Paulista

## Integrantes do Grupo
* **Gabriel Góes Nunes Pereira** — RM: 571735
* **Bernardo Zauza Amorim** — RM: 568808
* **Bruno Almeida de Oliveira** — RM: 572648

---

## 1. Contextualização do Problema e Público-Alvo

* **Público-alvo:** Famílias residentes em apartamentos e residências urbanas de pequeno/médio porte (faixa de consumo entre 220 kWh/mês e 350 kWh/mês) na Região Metropolitana de São Paulo, atendidas pela distribuidora Enel SP.
* **Necessidade energética abordada:** Muitas famílias sofrem com o alto custo da conta de luz devido ao uso intensivo de chuveiro elétrico e eletrodomésticos antigos, mas desconhecem o peso real de cada aparelho na fatura e têm dúvidas sobre como reduzir gastos sem perder conforto — especialmente quando moram em apartamentos ou imóveis alugados onde não podem instalar painéis solares no telhado.
* **Contribuição do Citizen Assist AI:** O módulo de energia permite que o cidadão consulte, em linguagem simples, quanto cada aparelho pesa na conta, compare alternativas reais de economia e geração renovável (incluindo opções viáveis para quem mora em apartamento) e entenda os custos, o tempo de retorno (*payback*), o impacto ambiental ($CO_2$ evitado) e as limitações de cada escolha.

---

## 2. Estrutura do Repositório

```text
├── README.md                                  # Documentação principal do projeto
├── dados/
│   ├── consumo_residencial_base.json          # Levantamento de equipamentos, potências (W) e consumo mensal (kWh)
│   └── tarifas_e_premissas.json               # Tarifas Enel SP, fatores de emissão SIN e parâmetros técnicos
├── docs/
│   ├── analise_e_comparacao_alternativas.md   # Cálculos detalhados, comparação entre 3 alternativas e limitações
│   └── testes_com_usuarios.md                 # Registro dos 4 testes realizados, feedbacks e ajustes no código
└── src/
    ├── calculadora_energia.py                 # Motor de cálculo de consumo, custos, payback e emissões
    └── assistente_energia.py                  # Módulo conversacional do Citizen Assist AI com base fundamentada
```

---

## 3. Resumo da Análise e Alternativas Comparadas

Analisamos uma residência padrão com consumo mensal de **300,60 kWh/mês** (custo estimado de **R$ 264,53/mês** considerando tarifa residencial B1 com impostos de R$ 0,88/kWh) e comparamos **3 alternativas** para o horizonte de **5 anos (60 meses)**:

1. **Alternativa A (Eficiência + Hábito — Sem Investimento Inicial):** Redução do tempo de banho no chuveiro elétrico (de 15 min para 8 min/dia por pessoa) + troca de 8 lâmpadas antigas/fluorescentes por LED 9W.
2. **Alternativa B (Fonte Renovável — Energia Solar por Assinatura / Geração Compartilhada):** Adesão a cooperativa/usina solar remota (GD compartilhada), ideal para apartamentos e imóveis alugados, sem obras ou compra de placas.
3. **Alternativa C (Fonte Renovável — Sistema Solar Fotovoltaico Próprio On-Grid 2,2 kWp):** Instalação de 4 módulos fotovoltaicos de 550 Wp no telhado (para casas próprias).

| Critério (Horizonte 5 anos) | Cenário Atual (Base) | Alt. A: Eficiência + Hábito | Alt. B: Solar por Assinatura (Renovável) | Alt. C: Solar Próprio On-Grid (Renovável) |
| :--- | :---: | :---: | :---: | :---: |
| **Investimento Inicial** | R$ 0,00 | R$ 96,00 (lâmpadas LED) | R$ 0,00 | R$ 9.800,00 |
| **Economia Mensal Média** | R$ 0,00 | R$ 81,58 / mês | R$ 34,39 / mês (15% na parcela compensável) | R$ 220,53 / mês (mantendo taxa mínima) |
| **Tempo de Retorno (Payback)** | — | ~1,2 mês | Imediato (sem aporte) | ~44,4 meses (3,7 anos) |
| **Saldo Líquido em 5 anos** | -R$ 15.871,68 | +R$ 4.798,80 | +R$ 2.063,40 | +R$ 3.431,80 |
| **CO₂ Evitado (5 anos)** | 0 kg | ~321,3 kg CO₂ | ~954,0 kg CO₂ | ~1.038,0 kg CO₂ |
| **Indicado para Apartamento?** | — | Sim | Sim | Não (exige telhado próprio) |

*Nota: Os cálculos detalhados, fórmulas, premissas e limitações estão documentados em `docs/analise_e_comparacao_alternativas.md`.*

---

## 4. Como Executar e Testar a Solução

### Pré-requisitos
* Python 3.10 ou superior instalado (não requer bibliotecas externas pesadas; utiliza apenas biblioteca padrão `json`, `math`, `os`).

### Passo a passo para rodar no terminal
1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd citizen-assist-ai-sers
   ```
2. Execute o motor de cálculos para visualizar a tabela comparativa completa no terminal:
   ```bash
   python src/calculadora_energia.py
   ```
3. Execute o assistente interativo (Citizen Assist AI - Módulo Energia):
   ```bash
   python src/assistente_energia.py
   ```
4. No menu do assistente, você pode testar:
   * Perguntas prontas ou digitar dúvidas livres (ex: *"Moro em apartamento e gasto 300 kWh, vale a pena energia solar?"*, *"Quanto gasta meu chuveiro?"*, *"Quais as limitações dos cálculos?"*).
   * Simulação personalizada informando seu consumo mensal em kWh e tipo de moradia (casa ou apartamento).

---

## 5. Referências Utilizadas

1. **PROCEL / ELETROBRAS.** *Tabela de Consumo e Eficiência Energética de Equipamentos Residenciais.* Disponível em: http://www.procelinfo.com.br
2. **EPE (Empresa de Pesquisa Energética).** *Balanço Energético Nacional (BEN) e Anuário Estatístico de Energia Elétrica.* Disponível em: https://www.epe.gov.br
3. **ANEEL (Agência Nacional de Energia Elétrica).** *Resolução Normativa nº 1.000/2021 e Regras de Micro e Minigeração Distribuída (Lei 14.300/2022).* Disponível em: https://www.gov.br/aneel
4. **MCTI (Ministério da Ciência, Tecnologia e Inovação).** *Fatores de Emissão de CO₂ do Sistema Interligado Nacional (SIN).* Disponível em: https://www.gov.br/mcti
5. **Enel Distribuição São Paulo.** *Tarifas de Energia Elétrica - Grupo B (Residencial B1).* Disponível em: https://www.enel.com.br
