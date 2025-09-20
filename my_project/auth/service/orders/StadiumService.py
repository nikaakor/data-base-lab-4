from typing import List
from my_project.auth.dao.orders import StadiumDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Stadium


class StadiumService(GeneralService):
    _dao = StadiumDAO

    def create(self, stadium: Stadium) -> None:
        self._dao.create(stadium)

    def get_all_stadiums(self) -> List[Stadium]:  # type: ignore
        return self._dao.find_all()

    def get_stadium_by_id(self, stadium_id: int) -> Stadium:
        return self._dao.find_by_id(stadium_id)

    def update_stadium(self, stadium: Stadium) -> None:
        self._dao.update(stadium)

    def delete_stadium(self, stadium_id: int) -> None:
        self._dao.delete(stadium_id)

# from typing import List
# from my_project.auth.dao.orders import StadiumDAO
# from my_project.auth.service.general_service import GeneralService
# from my_project.auth.domain.orders import Stadium, Match


# class StadiumService(GeneralService):
#     _dao = StadiumDAO

#     def create(self, stadium: Stadium) -> None:
#         self._dao.create(stadium)

#     def get_all_stadiums(self) -> List[Stadium]:  # type: ignore
#         return self._dao.find_all()

#     def get_stadium_by_id(self, stadium_id: int) -> Stadium:
#         return self._dao.find_by_id(stadium_id)

#     def get_matches_by_stadium(self, stadium_id: int) -> List[Match]:
#         return self._dao.find_matches_by_stadium(stadium_id)

#     def update_stadium(self, stadium: Stadium) -> None:
#         self._dao.update(stadium)

#     def delete_stadium(self, stadium_id: int) -> None:
#         self._dao.delete(stadium_id)
