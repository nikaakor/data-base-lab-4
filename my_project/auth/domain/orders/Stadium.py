from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Stadium(db.Model, IDto):
    __tablename__ = "stadium"
    stadium_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(90), nullable=False)
    stadium_name = db.Column(db.String(45), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "stadium_id": self.stadium_id,
            "location": self.location,
            "stadium_name": self.stadium_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Stadium:
        return Stadium(**dto_dict)

# from __future__ import annotations
# from typing import Dict, Any
# from my_project import db
# from my_project.auth.domain.i_dto import IDto

# from my_project.auth.domain.orders.Match import Match  # Correct the import path


# class Stadium(db.Model, IDto):
#     __tablename__ = "stadium"
#     stadium_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     location = db.Column(db.String(90), nullable=False)
#     stadium_name = db.Column(db.String(45), nullable=False)

#     # Relationship to the Match model
#     matches = db.relationship("Match", back_populates="stadium", lazy="select")

#     def put_into_dto(self) -> Dict[str, Any]:
#         return {
#             "stadium_id": self.stadium_id,
#             "location": self.location,
#             "stadium_name": self.stadium_name,
#             "matches": [match.put_into_dto() for match in self.matches],
#         }

#     @staticmethod
#     def create_from_dto(dto_dict: Dict[str, Any]) -> Stadium:
#         return Stadium(**dto_dict)
