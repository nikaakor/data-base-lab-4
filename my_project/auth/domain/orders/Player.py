from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Player(db.Model, IDto):
    __tablename__ = "player"
    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_name = db.Column(db.String(45), nullable=False)
    player_surname = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "player_id": self.player_id,
            "player_name": self.player_name,
            "player_surname": self.player_surname,
            "position": self.position,
            "number": self.number,
            "age": self.age,
            "team_id": self.team_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Player:
        return Player(**dto_dict)
