# Análise de Consumo, Cálculos e Comparação de Alternativas Energéticas

## 1. Metodologia e Fórmulas Utilizadas

Para calcular o consumo mensal de cada equipamento residencial, aplicamos a relação física fundamental entre potência e energia:

$$E_{kWh} = \frac{P_{W} \times t_{horas/dia} \times d_{dias/mês}}{1000}$$

Onde:
* $E_{kWh}$: Energia elétrica consumida no mês (quilowatt-hora);
* $P_{W}$: Potência nominal do aparelho (Watts);
* $t_{horas/dia}$: Tempo médio diário de funcionamento (horas);
* $d_{dias/mês}$: Número de dias de utilização no mês.

Para o custo financeiro mensal e emissões de gases de efeito estufa (GEE):
* **Custo Mensal ($R\$$):** $C = E_{kWh} \times T_{tarifa}$ (adotando $T_{tarifa} = R\$\ 0,88/kWh$, valor estimado com tributos para consumidor Residencial B1 em São Paulo).
* **Emissões de $CO_2$ ($kg\ CO_2$):** $M_{CO_2} = E_{kWh} \times F_{SIN}$ (adotando $F_{SIN} = 0,058\ kg\ CO_2/kWh$, fator médio do Sistema Interligado Nacional segundo o MCTI).

---

## 2. Diagnóstico do Consumo Base (Cenário Atual)

Considerando uma família de **3 pessoas** morando em apartamento ou casa urbana na Grande São Paulo (dados estimados com base na tabela PROCEL):

| Equipamento | Potência (W) | Uso Diário (h) | Dias/Mês | Consumo (kWh/mês) | Participação (%) | Custo Mensal (R$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Chuveiro Elétrico (5500W) | 5.500 | 0,75 | 30 | 123,75 | 41,17% | R$ 108,90 |
| Geladeira Duplex Antiga | 150 | 12,00 | 30 | 54,00 | 17,96% | R$ 47,52 |
| Computador + Roteador Wi-Fi | 110 | 8,00 | 30 | 26,40 | 8,78% | R$ 23,23 |
| Stand-by e Carregadores | 33,6 | 24,00 | 30 | 24,20 | 8,05% | R$ 21,30 |
| Iluminação (8 lâmpadas 20W) | 160 | 5,00 | 30 | 24,00 | 7,98% | R$ 21,12 |
| TV LED 43" + Decodificador | 120 | 5,00 | 30 | 18,00 | 5,99% | R$ 15,84 |
| Air Fryer | 1.500 | 0,50 | 15 | 11,25 | 3,74% | R$ 9,90 |
| Micro-ondas | 1.200 | 0,25 | 30 | 9,00 | 2,99% | R$ 7,92 |
| Máquina de Lavar (10 kg) | 500 | 1,00 | 12 | 6,00 | 2,00% | R$ 5,28 |
| Ferro de Passar | 1.000 | 1,00 | 4 | 4,00 | 1,33% | R$ 3,52 |
| **TOTAL MENSAL** | — | — | — | **300,60 kWh** | **100,0%** | **R$ 264,53** |

**Principais gargalos identificados:** Apenas o **chuveiro elétrico (41,2%)** e a **geladeira (18,0%)** representam quase **60% de toda a conta de luz**.

---

## 3. Comparação Detalhada das Alternativas (Período: 5 Anos / 60 Meses)

### Alternativa A: Eficiência Energética e Mudança de Hábito (Chuveiro + LED)
* **Ação:** Reduzir o tempo médio de banho de 15 min para 8 min por morador (total de 24 min/dia = 0,40 h/dia) e substituir 8 lâmpadas fluorescentes de 20W por 8 lâmpadas LED de 9W (potência total cai de 160W para 72W).
* **Cálculo da redução:**
  * Chuveiro novo: $\frac{5500 \times 0,40 \times 30}{1000} = 66,00\ kWh/mês$ (economia de $57,75\ kWh/mês$).
  * Iluminação nova: $\frac{72 \times 5,0 \times 30}{1000} = 10,80\ kWh/mês$ (economia de $13,20\ kWh/mês$).
  * **Economia total:** $70,95\ kWh/mês$ ($23,6\%$ da fatura) = **R$ 62,44/mês**.
  * *(Obs.: Caso também desligue aparelhos em stand-by via filtro de linha, economiza mais ~15 kWh/mês = R$ 13,20/mês).*
* **Investimento:** R$ 96,00 (compra das 8 lâmpadas LED).
* **Payback simples:** $\frac{96,00}{62,44} \approx 1,54\ mês$ (menos de 2 meses).
* **Economia líquida em 5 anos:** $(62,44 \times 60) - 96,00 = \mathbf{R\$\ 3.650,40}$.
* **Impacto Ambiental:** $70,95 \times 60 \times 0,058 = \mathbf{246,91\ kg\ CO_2}$ evitados em 5 anos.
* **Viabilidade:** Altíssima. Funciona em qualquer casa ou apartamento, inclusive alugado.

---

### Alternativa B: Fonte Renovável — Energia Solar por Assinatura (Geração Compartilhada)
* **Ação:** O morador adere a uma cooperativa ou consórcio de geração distribuída solar (regulado pela Lei 14.300/2022) e recebe créditos de energia limpa diretamente na fatura da Enel, sem precisar instalar painéis no telhado.
* **Cálculo financeiro:**
  * Consumo total: $300,60\ kWh/mês$.
  * Parcela mínima obrigatória da distribuidora (padrão bifásico = 50 kWh): $50 \times 0,88 = R\$\ 44,00$.
  * Energia compensável via usina solar: $300,60 - 50,00 = 250,60\ kWh/mês$ ($R\$\ 220,53$).
  * Com desconto contratual médio de **15%** sobre a energia compensada: $220,53 \times 0,15 = \mathbf{R\$\ 33,08/mês}$ de economia real.
* **Investimento inicial:** **R$ 0,00** (sem obra e sem taxa de adesão).
* **Payback:** Imediato (economia desde a primeira fatura compensada, após prazo de homologação de 30 a 60 dias).
* **Economia líquida em 5 anos:** $33,08 \times 60 = \mathbf{R\$\ 1.984,80}$.
* **Impacto Ambiental:** $250,60\ kWh/mês$ passam a ser supridos por fonte 100% solar fotovoltaica, evitando $\mathbf{872,09\ kg\ CO_2}$ em 5 anos (considerando a substituição da energia média da rede).
* **Viabilidade:** Muito alta para moradores de apartamentos e imóveis alugados.

---

### Alternativa C: Fonte Renovável — Sistema Solar Fotovoltaico Próprio On-Grid (2,20 kWp)
* **Ação:** Instalação de 4 painéis solares de 550 Wp + inversor conectado à rede no telhado da residência.
* **Cálculo de geração:**
  * Geração estimada em São Paulo (irradiação média $4,45\ kWh/m^2\cdot dia$, eficiência global $80\%$):
    $$E_{gerada} = 2,20\ kWp \times 4,45 \times 30 \times 0,80 \approx 235,0\ kWh/mês$$
  * Custo antes: R$ 264,53/mês. Com geração de 235 kWh/mês, o morador paga apenas o residual de $65,60\ kWh$ + encargos da Lei 14.300 (Fio B), resultando em economia líquida estimada de **R$ 192,00/mês**.
* **Investimento inicial:** **R$ 9.800,00** (equipamentos + projeto + homologação).
* **Manutenção estimada:** R$ 150,00/ano (limpeza e inspeção = R$ 750,00 em 5 anos).
* **Payback simples:** $\frac{9.800,00}{192,00} \approx \mathbf{51,0\ meses}$ (~4,25 anos).
* **Saldo líquido em 5 anos:** $(192,00 \times 60) - 9.800,00 - 750,00 = \mathbf{+R\$\ 970,00}$ (passa a dar lucro expressivo a partir do 5º ano, já que os painéis duram 25 anos).
* **Impacto Ambiental:** $235,0 \times 60 \times 0,058 = \mathbf{817,80\ kg\ CO_2}$ evitados em 5 anos.
* **Viabilidade:** Restrita a **casas próprias** com telhado sem sombreamento e estrutura adequada. Inviável para apartamentos individuais.

---

## 4. Condições e Limitações das Estimativas

O assistente digital sempre informa explicitamente ao usuário as seguintes condições:
1. **Valores são estimativas, não garantias:** O consumo real varia conforme a temperatura da água desejada no chuveiro, estado das borrachas da geladeira, hábitos da família e bandeiras tarifárias vigentes da ANEEL.
2. **Regras da Lei 14.300/2022 (Marco Legal da GD):** Sistemas fotovoltaicos instalados após 2023 pagam gradualmente o custo de uso da rede de distribuição (Fio B) sobre a energia injetada, o que reduz ligeiramente a compensação integral.
3. **Condições climáticas:** A geração solar varia entre verão (maior irradiação) e inverno/dias nublados em São Paulo.
4. **Restrições contratuais e estruturais:** Energia solar por assinatura exige fidelidade contratual mínima (geralmente 12 meses) e consumo acima de 150–200 kWh/mês; já a instalação própria exige aprovação do condomínio ou propriedade exclusiva do telhado.
