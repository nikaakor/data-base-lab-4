from typing import List
from my_project.auth.dao.orders.RefereeDAO import RefereeDAO
from my_project.auth.domain.orders.Referee import Referee


class RefereeController:
    _dao = RefereeDAO()

    def find_all(self) -> List[Referee]:
        return self._dao.find_all()

    def create(self, referee: Referee) -> None:
        self._dao.create(referee)

    def find_by_id(self, referee_id: int) -> Referee:
        return self._dao.find_by_id(referee_id)

    def update(self, referee_id: int, referee: Referee) -> None:
        self._dao.update(referee_id, referee)

    def delete(self, referee_id: int) -> None:
        self._dao.delete(referee_id)
