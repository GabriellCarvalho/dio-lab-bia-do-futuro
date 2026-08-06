# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação este mês?"
- **Resposta esperada:** Valor baseado no `gastos_mensais.csv`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Comparação com limite de orçamento
- **Pergunta:** "Estourei meu limite de lazer?"
- **Resposta esperada:** Agente compara gasto atual com limite definido em `limites_orcamento.json` e informa se ultrapassou ou não
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo amanhã?"
- **Resposta esperada:** Agente informa que só trata de finanças/gastos e redireciona educadamente
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto gastei com viagens internacionais?"
- **Resposta esperada:** Agente admite que não possui essa informação nos dados e pede apenas o necessário se for relevante
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Comparou de forma clara os valores reais com os limites de orçamento definidos.
- Identificou riscos de estouro de orçamento e destacou a categoria afetada.
- O agente conseguiu responder corretamente perguntas sobre categorias de gastos.

**O que pode melhorar:**
- Melhorar a clareza quando os dados estão incompletos, pedindo apenas a informação necessária.
- Em alguns casos, o tempo de resposta foi maior do que o esperado.
- Melhorar o contexto.

---
