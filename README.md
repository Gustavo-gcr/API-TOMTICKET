

# 🧾 TomTicket - Criador Automático de Chamados

Este projeto tem como objetivo **automatizar a criação de chamados** na plataforma [TomTicket](https://www.tomticket.com/) via API, utilizando Python. Ele permite o envio em massa de tickets com informações padronizadas, economizando tempo e esforço em processos repetitivos.

## 📦 Funcionalidades

- Autenticação via token.
- Criação de múltiplos chamados com diferentes assuntos e mensagens.
- Preenchimento automático com data e hora de geração.
- Personalização de prioridade, categoria e departamento.

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- `requests` – para requisições HTTP
- `datetime` – para marcação de data/hora
- `os` – para controle do terminal (ex: `pause`)


## ⚙️ Configuração

Antes de executar o script, edite as seguintes variáveis de configuração com os seus dados:



> 🔒 **Importante:** Nunca compartilhe seu token em repositórios públicos.

## ▶️ Execução

1. Instale o Python e as dependências necessárias:


pip install requests


2. Execute o script:


python criar_chamados.py


O terminal mostrará o status de cada chamado enviado.

## 📌 Exemplo de Chamado Enviado

Cada chamado será criado com o seguinte formato no campo de mensagem:


Favor verificar as contas que não possuem Sitex.

Gerado automaticamente em 30/05/2025 10:30.


## 🧩 Possibilidades Futuras

* Leitura de chamados a partir de um arquivo `.csv` ou Excel.
* Interface gráfica para configuração de chamados.
* Agendamento automático.

## 📝 Licença

Este projeto é de uso interno e educacional. Verifique os termos de uso da API TomTicket antes de utilizá-la em ambientes de produção.


## Autor
- [Gustavo Coelho](https://github.com/Gustavo-gcr)
