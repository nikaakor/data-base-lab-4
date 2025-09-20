from typing import List
from my_project.auth.dao.orders import LineupDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Lineup


class LineupService(GeneralService):
    _dao = LineupDAO

    def create(self, lineup: Lineup) -> None:
        self._dao.create(lineup)

    def get_all_lineups(self) -> List[Lineup]:  # type: ignore
        return self._dao.find_all()

    def get_lineup_by_id(self, lineup_id: int) -> Lineup:
        return self._dao.find_by_id(lineup_id)

    def update_lineup(self, lineup: Lineup) -> None:
        self._dao.update(lineup)

    def delete_lineup(self, lineup_id: int) -> None:
        self._dao.delete(lineup_id)
