from typing import List
from my_project.auth.dao.orders.LineupDAO import LineupDAO
from my_project.auth.domain.orders.Lineup import Lineup


class LineupController:
    _dao = LineupDAO()

    def find_all(self) -> List[Lineup]:
        return self._dao.find_all()

    def create(self, lineup: Lineup) -> None:
        self._dao.create(lineup)

    def find_by_id(self, lineup_id: int) -> Lineup:
        return self._dao.find_by_id(lineup_id)

    def update(self, lineup_id: int, lineup: Lineup) -> None:
        self._dao.update(lineup_id, lineup)

    def delete(self, lineup_id: int) -> None:
        self._dao.delete(lineup_id)
