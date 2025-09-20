from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class MatchStat(db.Model, IDto):
    __tablename__ = "match_stat"
    match_stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    throw_in = db.Column(db.Integer, nullable=False)
    corner_kick = db.Column(db.Integer, nullable=False)
    direct_free_kick = db.Column(db.Integer, nullable=False)
    save = db.Column(db.Integer, nullable=False)
    foul = db.Column(db.Integer, nullable=False)
    home_goals = db.Column(db.Integer, nullable=False)
    away_goals = db.Column(db.Integer, nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "match_stat_id": self.match_stat_id,
            "throw_in": self.throw_in,
            "corner_kick": self.corner_kick,
            "direct_free_kick": self.direct_free_kick,
            "save": self.save,
            "foul": self.foul,
            "home_goals": self.home_goals,
            "away_goals": self.away_goals,
            "match_id": self.match_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MatchStat:
        return MatchStat(**dto_dict)
