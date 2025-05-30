import requests
from datetime import datetime
import os

# === CONFIGURAÇÕES ===
API_URL = "https://api.tomticket.com/v2.0/ticket/new"
TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo seu token de autenticação
CUSTOMER_ID = "seu_email" #substitua pelo ID do cliente ou email
DEPARTMENT_ID = "Id_departamento"  # Substitua pelo ID do departamento desejado
CATEGORY_ID = "Categoria_id"  # Substitua pelo ID da categoria desejada
PRIORITY = 2 # Substitua pela prioridade desejada (2=normal)

# === HEADERS ===
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# === LISTA DE CHAMADOS ===
chamados = [
    {
        "subject": "Retorno- Fulano",
        "message": "Favor realizar o retorno."
    },
    {
        "subject": "Contas sem Sitex- Fulano2",
        "message": "Favor verificar as contas que não possuem Sitex."
    },
    {
        "subject": "Análise de credito- Fulano3",
        "message": "Favor realizar a análise de crédito do cliente."
    },
    {
        "subject": "Fechamento Geral de contas- Fulano4",
        "message": "Favor realizar o fechamento geral de contas." 
    }
]

# === ENVIO DE CHAMADOS ===
for chamado in chamados:
    data = {
        "customer_id": CUSTOMER_ID,
        "customer_id_type": "I_ou_E",  # I-chamado interno, E-via email
        "department_id": DEPARTMENT_ID,
        "subject": chamado["subject"],
        "message": f"{chamado['message']}\n\nGerado automaticamente em {datetime.now().strftime('%d/%m/%Y %H:%M')}.",
        "category_id": CATEGORY_ID,
        "priority": PRIORITY
    }

    print(f"Enviando chamado: {chamado['subject']} ...")
    response = requests.post(API_URL, headers=headers, data=data)

    if response.status_code == 200:
        resp_json = response.json()
        if resp_json.get("success"):
            print("✅ Chamado criado com sucesso!")
        else:
            print("❌ Erro na criação do chamado:", resp_json.get("message"))
    else:
        print("❌ Erro na requisição:", response.status_code, response.text)

print("Todos os chamados foram processados.")
os.system("pause")
