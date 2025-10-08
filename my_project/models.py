from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(45), nullable=False)
    player_surname = db.Column(db.String(45), nullable=False)
    number = db.Column(db.String(45), nullable=False)
    date_of_birth = db.Column(db.String(45), nullable=False)
    position = db.Column(db.String(45), nullable=False)
    team_id = db.Column(db.Integer, nullable=False)

class Match(db.Model):
    __tablename__ = 'match'
    match_id = db.Column(db.Integer, primary_key=True)
    # додай інші поля відповідно до твоєї таблиці
