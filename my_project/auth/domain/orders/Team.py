from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Team(db.Model, IDto):
    __tablename__ = "team"
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coach_name = db.Column(db.String(45), nullable=False)
    coach_surname = db.Column(db.String(45), nullable=False)
    team_name = db.Column(db.String(45), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "team_id": self.team_id,
            "coach_name": self.coach_name,
            "coach_surname": self.coach_surname,
            "team_name": self.team_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Team:
        return Team(**dto_dict)
