# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `gastos_mensais.csv` | CSV | Históricos de gastos mensais por categoria (aluguel, alimentação, saúde, lazer) |
| `perfis_usuarios.json` | JSON | Perfis de usuários com renda, ocupação e prioridades financeiras para personalizar recomendações |
| `limites_orcamento.json` | JSON | Limites mensais de gastos por categoria para cada usuário  |
| `gastos_detalhados.csv` | CSV | Transações individuais com data, categoria, descrição e valor |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados originais do laboratório, que eram voltados para investimentos e produtos financeiros, foram substituídos por uma base focada em gastos pessoais. Para isso, foram criados novos arquivos em CSV e JSON com informações de gastos mensais, transações detalhadas, perfis de usuários e limites de orçamento por categoria.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Carrega os arquivos via código, como o exemplo abaixo:
```python
import pandas as pd
import json

perfil_usuario = json.load(open('./data/perfis_usuarios.json'))
limites_orcamento = json.load(open('./data/limites_orcamento.json'))
gastos_mensais = pd.read_csv('./data/gastos_mensais.csv')
gastos_detalhados = pd.read_csv('./data/gastos_detalhados.csv')
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O system prompt define o comportamento do agente, o tom de resposta e as regras de segurança, enquanto os dados dos arquivos CSV e JSON entram como contexto adicional em cada interação.

Exemplo de contexto enviado ao modelo:
```text
DADOS DO USUÁRIO:
- user_id: u01
- salário: R$ 5.500

PERFIL DO USUÁRIO:
- nome: Ana
- ocupação: Desenvolvedora júnior
- prioridades: guardar para reserva de emergência, organizar gastos com alimentação

GASTOS DO USUÁRIO:
- aluguel: R$ 1.200
- alimentação: R$ 950
- saúde: R$ 420
- lazer: R$ 280

ORÇAMENTO DO USUÁRIO:
- limite aluguel: R$ 1.500
- limite alimentação: R$ 1.000
- limite saúde: R$ 500
- limite lazer: R$ 400
```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Exemplo de como os dados podem ser organizados e enviados ao agente em uma interação real:

```text
DADOS DO USUÁRIO
user_id: u01
nome: Ana
idade: 27
ocupacao: Desenvolvedora júnior
cidade: Belo Horizonte
salario: 5500

PERFIL DO USUÁRIO
prioridades_financeiras:
- guardar para reserva de emergência
- organizar gastos com alimentação

GASTOS MENSAIS
mes: 2025-02
aluguel: 1200
alimentacao: 950
saude: 420
lazer: 280

LIMITES DE ORÇAMENTO
aluguel: 1500
alimentacao: 1000
saude: 500
lazer: 400

TRANSAÇÕES RECENTES
- 2025-02-04 | alimentação | Supermercado mês | 400 | débito
- 2025-02-15 | lazer | Bar com amigos | 200 | crédito
- 2025-02-20 | saúde | Farmácia | 120 | débito

INSTRUÇÃO PARA O AGENTE
Analise os gastos do usuário, compare com os limites definidos e informe se existe risco de estouro do orçamento em alguma categoria. Responda de forma clara, objetiva e sem inventar valores fora da base.
```
