from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Stadium import Stadium


class StadiumDAO(GeneralDAO):
    _domain_type = Stadium

    def create(self, stadium: Stadium) -> None:
        self._session.add(stadium)
        self._session.commit()

    def find_all(self) -> List[Stadium]:
        return self._session.query(Stadium).all()

    def find_by_name(self, stadium_name: str) -> Optional[Stadium]:
        return (
            self._session.query(Stadium)
            .filter(Stadium.stadium_name == stadium_name)
            .first()
        )

# from typing import List, Optional
# from my_project.auth.dao.general_dao import GeneralDAO
# from my_project.auth.domain.orders.Stadium import Stadium, Match


# class StadiumDAO(GeneralDAO):
#     _domain_type = Stadium

#     def create(self, stadium: Stadium) -> None:
#         self._session.add(stadium)
#         self._session.commit()

#     def find_all(self) -> List[Stadium]:
#         return self._session.query(Stadium).all()

#     def find_by_name(self, stadium_name: str) -> Optional[Stadium]:
#         return (
#             self._session.query(Stadium)
#             .filter(Stadium.stadium_name == stadium_name)
#             .first()
#         )

#     def find_matches_by_stadium(self, stadium_id: int) -> List[Match]:
#         return self._session.query(Match).join(Stadium).filter(Stadium.stadium_id == stadium_id).all()

# class StadiumDAO(GeneralDAO):
#     _domain_type = Stadium

#     def create(self, stadium: Stadium) -> None:
#         with self._session.begin():
#             self._session.add(stadium)

#     def find_all(self) -> List[Stadium]:
#         return self._session.query(Stadium).all()

#     def find_matches_by_stadium(self, stadium_id: int) -> List[Match]:
#         return (
#             self._session.query(Match)
#             .join(Stadium)
#             .filter(Stadium.stadium_id == stadium_id)
#             .all()
#         )


# class StadiumDAO(GeneralDAO):
#     _domain_type = Stadium

#     def create(self, stadium: Stadium) -> None:
#         with self._session.begin():
#             self._session.add(stadium)

#     def find_all(self) -> List[Stadium]:
#         return self._session.query(Stadium).all()

#     def find_matches_by_stadium(self, stadium_id: int) -> List[Match]:
#         return (
#             self._session.query(Match)
#             .join(Stadium)
#             .filter(Stadium.stadium_id == stadium_id)
#             .all()
#         )
