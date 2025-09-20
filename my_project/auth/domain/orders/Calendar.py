from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Calendar(db.Model, IDto):
    __tablename__ = "calendar"
    calendar_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_calendar = db.Column(db.Date, nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.match_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "calendar_id": self.calendar_id,
            "date_calendar": self.date_calendar,
            "match_id": self.match_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Calendar:
        return Calendar(**dto_dict)
