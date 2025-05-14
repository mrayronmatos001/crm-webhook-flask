from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

contact_campaign = db.Table('contact_campaign',
    db.Column('contact_id', db.Integer, db.ForeignKey('contact.id')),
    db.Column('campaign_id', db.Integer, db.ForeignKey('campaign.id'))
)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    campaigns = db.relationship('Campaign', secondary=contact_campaign, back_populates='contacts')

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    contacts = db.relationship('Contact', secondary=contact_campaign, back_populates='campaigns')
