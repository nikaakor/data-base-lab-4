from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class TeamStat(db.Model, IDto):
    __tablename__ = "team_stat"
    team_stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    matches_played = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    draws = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    goals_scored = db.Column(db.Integer, nullable=False)
    shots = db.Column(db.Integer, nullable=False)
    shots_on_target = db.Column(db.Integer, nullable=False)
    missed_shots = db.Column(db.Integer, nullable=False)
    blocked_shots = db.Column(db.Integer, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "team_stat_id": self.team_stat_id,
            "matches_played": self.matches_played,
            "wins": self.wins,
            "draws": self.draws,
            "losses": self.losses,
            "goals_scored": self.goals_scored,
            "shots": self.shots,
            "shots_on_target": self.shots_on_target,
            "missed_shots": self.missed_shots,
            "blocked_shots": self.blocked_shots,
            "team_id": self.team_id,
            "match_id": self.match_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TeamStat:
        return TeamStat(**dto_dict)
