from flask import Flask, request, jsonify
from models import db, Contact, Campaign
import config
import requests

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

WEBHOOK_URL = 'http://localhost:5001/webhook'

@app.before_request
def create_tables():
    db.create_all()
    # Dados fictícios para teste
    if not Contact.query.first():
        c1 = Contact(name="Ana Paula")
        c2 = Contact(name="João Silva")
        camp1 = Campaign(title="Campanha Dia das Mães")
        camp2 = Campaign(title="Campanha Fim de Ano")
        db.session.add_all([c1, c2, camp1, camp2])
        db.session.commit()

@app.route('/assign', methods=['POST'])
def assign_contact_to_campaign():
    data = request.json
    contact = Contact.query.get(data['contact_id'])
    campaign = Campaign.query.get(data['campaign_id'])

    if not contact or not campaign:
        return jsonify({"error": "Contato ou campanha não encontrados"}), 404

    if campaign not in contact.campaigns:
        contact.campaigns.append(campaign)
        db.session.commit()

        payload = {
            "event": "contact_assigned",
            "contact": {"id": contact.id, "name": contact.name},
            "campaign": {"id": campaign.id, "title": campaign.title}
        }
        requests.post(WEBHOOK_URL, json=payload)

    return jsonify({"message": "Contato atribuído à campanha e webhook enviado."})

if __name__ == '__main__':
    app.run(port=5000)
