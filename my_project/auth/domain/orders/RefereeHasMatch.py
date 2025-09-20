from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class RefereeHasMatch(db.Model, IDto):
    __tablename__ = "referee_has_match"
    referee_referee_id = db.Column(
        db.Integer, db.ForeignKey("referee.referee_id"), primary_key=True
    )
    match_match_id = db.Column(
        db.Integer, db.ForeignKey("match.match_id"), primary_key=True
    )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "referee_referee_id": self.referee_referee_id,
            "match_match_id": self.match_match_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RefereeHasMatch:
        return RefereeHasMatch(**dto_dict)
