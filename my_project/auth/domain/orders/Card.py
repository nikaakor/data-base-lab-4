from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Card(db.Model, IDto):
    __tablename__ = "card"
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_type = db.Column(db.String(45), nullable=False)
    card_time = db.Column(db.Time, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "card_id": self.card_id,
            "card_type": self.card_type,
            "card_time": self.card_time,
            "player_id": self.player_id,
            "match_id": self.match_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Card:
        return Card(**dto_dict)
