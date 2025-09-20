from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Match(db.Model, IDto):
    __tablename__ = "match"
    match_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    match_date = db.Column(db.Date, nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)
    stadium_id = db.Column(
        db.Integer, db.ForeignKey("stadium.stadium_id"), nullable=False
    )
    match_time = db.Column(db.Time, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "match_id": self.match_id,
            "match_date": self.match_date,
            "home_team_id": self.home_team_id,
            "away_team_id": self.away_team_id,
            "stadium_id": self.stadium_id,
            "match_time": self.match_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Match:
        return Match(**dto_dict)

# from __future__ import annotations
# from typing import Dict, Any
# from my_project import db
# from my_project.auth.domain.i_dto import IDto


# class Match(db.Model):
#     __tablename__ = "match"
#     match_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     stadium_id = db.Column(
#         db.Integer, db.ForeignKey("stadium.stadium_id"), nullable=False
#     )
#     match_date = db.Column(db.Date, nullable=False)
#     match_time = db.Column(db.Time, nullable=False)

#     # Зв'язок "багато-до-одного" з Stadium
#     stadium = db.relationship("Stadium", back_populates="matches", lazy="joined")

#     def put_into_dto(self) -> Dict[str, Any]:
#         return {
#             "match_id": self.match_id,
#             "match_date": self.match_date,
#             "stadium_id": self.stadium_id,
#             "match_time": self.match_time,
#         }

#     @staticmethod
#     def create_from_dto(dto_dict: Dict[str, Any]) -> Match:
#         return Match(**dto_dict)
