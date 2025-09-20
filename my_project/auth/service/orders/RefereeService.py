from typing import List
from my_project.auth.dao.orders import RefereeDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Referee


class RefereeService(GeneralService):
    _dao = RefereeDAO

    def create(self, referee: Referee) -> None:
        self._dao.create(referee)

    def get_all_referees(self) -> List[Referee]:  # type: ignore
        return self._dao.find_all()

    def get_referee_by_id(self, referee_id: int) -> Referee:
        return self._dao.find_by_id(referee_id)

    def update_referee(self, referee: Referee) -> None:
        self._dao.update(referee)

    def delete_referee(self, referee_id: int) -> None:
        self._dao.delete(referee_id)
