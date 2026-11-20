# Registro de Testes com Usuários — Citizen Assist AI (Módulo Energia)

Para validar a clareza, a linguagem acessível e a utilidade prática das respostas do assistente, realizamos **4 sessões de teste** com perfis representativos do público-alvo (moradores de apartamento e casa em São Paulo, sem formação técnica na área elétrica). Nenhum dado pessoal sensível foi coletado.

---

### Teste 01 — Morador de Apartamento Alugado (Consumo ~290 kWh/mês)
* **Situação testada:** O usuário perguntou: *"Moro em apartamento alugado e minha conta vem quase 260 reais. Vale a pena colocar placa solar?"*
* **Resposta inicial do assistente:** Apresentou os cálculos das três alternativas e explicou que placas próprias não são viáveis em apartamento alugado, recomendando eficiência no chuveiro + energia solar por assinatura.
* **Comentário do usuário:** *"Gostei porque não me mandou comprar placa solar sem poder instalar, mas achei confuso o termo 'Fio B e GD compartilhada'. Queria saber direto quanto sobra no bolso."*
* **Ajuste realizado no sistema:** Simplificamos o vocabulário nas respostas do `assistente_energia.py`, traduzindo "GD compartilhada" para *"energia solar por assinatura (sem obra)"* e destacando o valor em Reais economizado por mês logo nas primeiras linhas.

---

### Teste 02 — Dona de Casa Preocupada com o Chuveiro e Geladeira
* **Situação testada:** A usuária perguntou: *"Qual aparelho gasta mais na minha casa e como faço para baixar a conta sem gastar dinheiro agora?"*
* **Resposta inicial do assistente:** Listou o ranking de consumo mostrando que o chuveiro elétrico (41,2%) e a geladeira (18%) lideram os gastos, sugerindo reduzir o banho de 15 para 8 minutos e trocar lâmpadas por LED.
* **Comentário da usuária:** *"Muito claro! Só senti falta de saber o que acontece se eu apenas mudar a chave do chuveiro de 'Inverno' para 'Verão' sem diminuir o tempo do banho."*
* **Ajuste realizado no sistema:** Adicionamos uma nota prática no módulo de dicas informando que mudar a chave seletora de Inverno (5.500W) para Verão (~3.200W) reduz cerca de 30% a 40% da potência instantânea do chuveiro.

---

### Teste 03 — Estudante Universitário (Simulação Personalizada)
* **Situação testada:** O usuário inseriu um consumo mensal personalizado de **180 kWh/mês** (morando sozinho em kitnet) na opção de simulação.
* **Resposta inicial do assistente:** Calculou a economia da energia solar por assinatura usando a taxa mínima bifásica (50 kWh), o que subestimou a economia de quem tem padrão monofásico (30 kWh).
* **Comentário do usuário:** *"Aqui no meu prédio o relógio é monofásico, a taxa mínima é 30 kWh, não 50 kWh."*
* **Ajuste realizado no sistema:** Atualizamos a função `simular_cenario_personalizado()` em `calculadora_energia.py` para permitir escolher o tipo de padrão de entrada (**Monofásico = 30 kWh** ou **Bifásico = 50 kWh**).

---

### Teste 04 — Morador de Casa Própria Avaliando Investimento Solar
* **Situação testada:** O usuário perguntou: *"Tenho casa própria e gasto 350 kWh por mês. Se eu investir em painel solar próprio, em quanto tempo o dinheiro volta e isso é garantido?"*
* **Resposta inicial do assistente:** Apresentou o payback estimado (~4 anos) e o impacto ambiental em kg de $CO_2$.
* **Comentário do usuário:** *"Achei ótimo o aviso no final dizendo que o retorno depende do clima e da tarifa da Enel, passa mais confiança do que promessa de vendedor."*
* **Ajuste realizado no sistema:** Mantivemos e destacamos o bloco obrigatório de **"Condições e Limitações"** em todas as respostas geradas pelo assistente.
