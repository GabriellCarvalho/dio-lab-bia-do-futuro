# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto
Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para agentes inteligentes e proativos. Neste projeto, foi desenvolvido um **Agente Financeiro de Gastos Mensais**, que utiliza IA Generativa para:

- Antecipar necessidades ao invés de apenas responder perguntas  
- Personalizar sugestões com base no perfil e nos dados de cada cliente  
- Cocriar soluções financeiras de forma consultiva e acessível  
- Garantir segurança e confiabilidade nas respostas (anti-alucinação)  

---

## ✅ Entregáveis

### 1. Documentação do Agente [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)
- **Caso de Uso:** Controle e análise de gastos mensais, com alertas de estouro de orçamento.  
- **Persona e Tom de Voz:** Informal, direto, claro e acessível, sem “economês”.  
- **Arquitetura:**  
  - Interface em **Streamlit**  
  - Integração com **Ollama** para geração de respostas  
  - Base de dados mockada em CSV/JSON  
- **Segurança:**  
  - Não inventa valores ou transações  
  - Admite quando não possui informação  
  - Evita dados sensíveis  

---

### 2. Base de Conhecimento [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)
- **Arquivos utilizados:**  
  - `gastos_mensais.csv`  
  - `gastos_detalhados.csv`  
  - `perfis_usuarios.json`  
  - `limites_orcamento.json`  
- **Função:** Alimentar o agente com dados fictícios de clientes, limites de orçamento e histórico de gastos.  

---

### 3. Prompts do Agente [`docs/03-prompts.md`](./docs/03-prompts.md)
- **System Prompt:** Define comportamento seguro, claro e objetivo.  
- **Exemplos de Interação:**  
  - Pergunta: *"Quanto gastei com alimentação?"* → Resposta: valor baseado no CSV.  
  - Pergunta: *"Estourei meu limite de lazer?"* → Resposta: comparação com limite definido.  
- **Edge Cases:**  
  - Perguntas fora do escopo → agente informa que só trata de finanças.  
  - Dados inexistentes → agente admite e pede apenas o necessário.  

---

### 4. Aplicação Funcional [`src/app.py`](./src/)
- Protótipo funcional em **Streamlit**  
- Integração com **Ollama** via API  
- Conexão com base de conhecimento mockada  
- Interface de chat interativo com histórico de mensagens  

---

### 5. Avaliação e Métricas [`docs/04-metricas.md`](./docs/04-metricas.md)
- **Métricas aplicadas:**  
  - Assertividade  
  - Segurança (anti-alucinação)  
  - Coerência com perfil do cliente  
  - Clareza e utilidade  
- **Cenários de Teste:**  
  - Consulta de gastos por categoria  
  - Comparação com limite de orçamento  
  - Pergunta fora do escopo  
  - Informação inexistente  
  - Sugestão prática de ajuste  
- **Resultados:**  
  - Funcionou bem: respostas diretas, seguras e contextualizadas  
  - Melhorias: tempo de resposta e detalhamento das sugestões  

---

## 🛠️ Ferramentas Utilizadas
- **LLMs:** Ollama (modelo DeepSeek-R1)  
- **Desenvolvimento:** Streamlit  
- **Orquestração:** Prompts customizados  
- **Diagramas:** Documentação em Markdown  

---

## 📂 Estrutura do Repositório
```
lab-agente-financeiro/
│
├── README.md                        # Documento inicial do projeto
├── data/                            # Dados mockados para o agente
│   ├── gastos_mensais.csv           # Dados agregados por categoria
│   ├── gastos_detalhados.csv        # Dados transacionais detalhados
│   ├── perfis_usuarios.json         # Perfis fictícios de clientes
│   └── limites_orcamento.json       # Limites de orçamento por categoria para cada usuário
├── docs/                            # Documentação do projeto
│   ├── 01-documentacao-agente.md    # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md      # Estratégia de dados
│   ├── 03-prompts.md                # Engenharia de prompts
│   ├── 04-metricas.md               # Avaliação e métricas
├── src/                             # Código da aplicação
|   ├── app.py                       # Aplicação principal (Streamlit)
|   ├── agente.py                    # Lógica do agente
|   ├── config.py                    # Configurações (API keys, etc.)
|   └── requirements.txt             # Dependências
```

---

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```



