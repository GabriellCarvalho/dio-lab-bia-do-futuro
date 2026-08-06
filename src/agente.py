import requests
import pandas as pd
import json
from config import OLLAMA_URL, MODELO, SYSTEM_PROMPT, DATA_DIR

# Carregar dados
perfis_usuarios = json.load(open(f"{DATA_DIR}\\perfis_usuarios.json"))
limites_orcamento = json.load(open(f"{DATA_DIR}\\limites_orcamento.json"))
gastos_mensais = pd.read_csv(f"{DATA_DIR}\\gastos_mensais.csv")
gastos_detalhados = pd.read_csv(f"{DATA_DIR}\\gastos_detalhados.csv")

# Selecionar usuário
user_id = "u02"
perfil = next(p for p in perfis_usuarios if p['user_id'] == user_id)
limite = next(l for l in limites_orcamento if l['user_id'] == user_id)

# Montar contexto
contexto = f"""
Este é o contexto de um usuário aleatorio para a análise de gastos e orçamento:
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, renda mensal R$ {perfil['renda_mensal']}
PERFIL DO USUÁRIO:
- prioridades financeiras: {", ".join(perfil['prioridades_financeiras'])}
- sensibilidade a risco: {perfil['sensibilidade_a_risco']}
- comentário do perfil: {perfil['comentario_perfil']}

GASTOS DO USUÁRIO:
- mês: {gastos_mensais['mes'].iloc[0]}
- aluguel: R$ {gastos_mensais['aluguel'].iloc[0]}
- alimentação: R$ {gastos_mensais['alimentacao'].iloc[0]}
- saúde: R$ {gastos_mensais['saude'].iloc[0]}
- lazer: R$ {gastos_mensais['lazer'].iloc[0]}

ORÇAMENTO DO USUÁRIO:
- limite aluguel: R$ {limite['limites']['aluguel']}
- limite alimentação: R$ {limite['limites']['alimentacao']}
- limite saúde: R$ {limite['limites']['saude']}
- limite lazer: R$ {limite['limites']['lazer']}
"""

def perguntar(msg: str) -> str:
    """Envia pergunta ao Ollama e retorna resposta tratada"""
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO:
    {contexto}
    
    Pergunta: {msg}"""
    
    r = requests.post(
        OLLAMA_URL,
        json={"model": MODELO, "prompt": prompt, "stream": False}
    )
    try:
        data = r.json()
        if "response" in data:
            return data["response"]
        elif "message" in data:
            return data["message"]
        elif "error" in data:
            return f"Erro do Ollama: {data['error']}"
        else:
            return str(data)
    except ValueError:
        return r.text
