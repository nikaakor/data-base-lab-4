from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Referee(db.Model, IDto):
    __tablename__ = "referee"
    referee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    referee_name = db.Column(db.String(45), nullable=False)
    referee_surname = db.Column(db.String(45), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "referee_id": self.referee_id,
            "referee_name": self.referee_name,
            "referee_surname": self.referee_surname,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Referee:
        return Referee(**dto_dict)
