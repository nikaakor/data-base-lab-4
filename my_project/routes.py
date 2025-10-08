from flask import Flask
from flask_restx import Api, Resource
from .models import db, Player, Match

def register_routes(app: Flask):
    api = Api(app, title='Footboom API', description='Players and Matches API')

    @api.route('/players')
    class PlayersResource(Resource):
        def get(self):
            players = Player.query.all()
            result = [
                {
                    "id": p.player_id,
                    "name": p.player_name,
                    "surname": p.player_surname,
                    "number": p.number,
                    "dob": p.date_of_birth,
                    "position": p.position,
                    "team_id": p.team_id
                } for p in players
            ]
            return result, 200

    @api.route('/match')
    class MatchResource(Resource):
        def get(self):
            matches = Match.query.all()
            result = [
                {
                    "id": m.match_id
                    # додати інші поля, якщо потрібно
                } for m in matches
            ]
            return result, 200
