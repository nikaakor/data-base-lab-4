from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class PlayerStat(db.Model, IDto):
    __tablename__ = "player_stat"
    player_stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    offside = db.Column(db.Integer, nullable=False)
    yellow_card = db.Column(db.Integer, nullable=False)
    red_card = db.Column(db.Integer, nullable=False)
    goals_scored = db.Column(db.Integer, nullable=False)
    minutes_played = db.Column(db.Integer, nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "player_stat_id": self.player_stat_id,
            "offside": self.offside,
            "yellow_card": self.yellow_card,
            "red_card": self.red_card,
            "goals_scored": self.goals_scored,
            "minutes_played": self.minutes_played,
            "match_id": self.match_id,
            "player_id": self.player_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PlayerStat:
        return PlayerStat(**dto_dict)
