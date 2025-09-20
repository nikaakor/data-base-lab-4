from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Goal(db.Model, IDto):
    __tablename__ = "goal"
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goal_time = db.Column(db.Time, nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "goal_id": self.goal_id,
            "goal_time": self.goal_time,
            "match_id": self.match_id,
            "player_id": self.player_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Goal:
        return Goal(**dto_dict)
