# 📬 CRM Webhook com Flask

Este é um mini-projeto de CRM que permite associar contatos a campanhas e, sempre que essa associação ocorre, dispara um webhook com os dados envolvidos. Ideal para aprender e demonstrar o uso de:

- Flask (API REST)
- SQLite + SQLAlchemy
- Webhooks (requests)
- Organização de código backend
- Integração com ferramentas externas

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11
- Flask 3.x
- Flask-SQLAlchemy
- SQLite
- DB Browser for SQLite (visualização opcional)
- Postman (para testar)

---

## ⚙️ Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/crm-webhook-flask.git
cd crm-webhook-flask
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Para Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode os dois servidores (em terminais separados):
```bash
python app.py
python webhook_receiver.py
```