from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Lineup(db.Model, IDto):
    __tablename__ = "lineup"
    lineup_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_starting = db.Column(db.String(45), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "lineup_id": self.lineup_id,
            "is_starting": self.is_starting,
            "match_id": self.match_id,
            "player_id": self.player_id,
            "team_id": self.team_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Lineup:
        return Lineup(**dto_dict)
