from typing import List
from my_project.auth.dao.orders.StadiumDAO import StadiumDAO
from my_project.auth.domain.orders.Stadium import Stadium


class StadiumController:
    _dao = StadiumDAO()

    def find_all(self) -> List[Stadium]:
        return self._dao.find_all()

    def create(self, stadium: Stadium) -> None:
        self._dao.create(stadium)

    def find_by_id(self, stadium_id: int) -> Stadium:
        return self._dao.find_by_id(stadium_id)

    def update(self, stadium_id: int, stadium: Stadium) -> None:
        self._dao.update(stadium_id, stadium)

    def delete(self, stadium_id: int) -> None:
        self._dao.delete(stadium_id)

# from typing import List
# from my_project.auth.dao.orders.StadiumDAO import StadiumDAO
# from my_project.auth.domain.orders.Stadium import Stadium, Match


# class StadiumController:
#     _dao = StadiumDAO()

#     def find_all(self) -> List[Stadium]:
#         return self._dao.find_all()

#     def create(self, stadium: Stadium) -> None:
#         self._dao.create(stadium)

#     def find_by_id(self, stadium_id: int) -> Stadium:
#         return self._dao.find_by_id(stadium_id)

#     def find_matches_by_stadium(self, stadium_id: int) -> List[Match]:
#         return self._session.query(Match).join(Stadium).filter(Stadium.stadium_id == stadium_id).all()


#     def update(self, stadium_id: int, stadium: Stadium) -> None:
#         self._dao.update(stadium_id, stadium)

#     def delete(self, stadium_id: int) -> None:
#         self._dao.delete(stadium_id)
