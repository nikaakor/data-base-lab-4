from typing import List
from my_project.auth.dao.orders.MatchStatDAO import MatchStatDAO
from my_project.auth.domain.orders.MatchStat import MatchStat


class MatchStatController:
    _dao = MatchStatDAO()

    def find_all(self) -> List[MatchStat]:
        return self._dao.find_all()

    def create(self, match_stat: MatchStat) -> None:
        self._dao.create(match_stat)

    def find_by_id(self, match_stat_id: int) -> MatchStat:
        return self._dao.find_by_id(match_stat_id)

    def update(self, match_stat_id: int, match_stat: MatchStat) -> None:
        self._dao.update(match_stat_id, match_stat)

    def delete(self, match_stat_id: int) -> None:
        self._dao.delete(match_stat_id)
