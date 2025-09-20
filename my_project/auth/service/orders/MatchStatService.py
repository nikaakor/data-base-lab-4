from typing import List
from my_project.auth.dao.orders import MatchStatDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import MatchStat


class MatchStatService(GeneralService):
    _dao = MatchStatDAO

    def create(self, match_stat: MatchStat) -> None:
        self._dao.create(match_stat)

    def get_all_match_stats(self) -> List[MatchStat]:  # type: ignore
        return self._dao.find_all()

    def get_match_stat_by_id(self, match_stat_id: int) -> MatchStat:
        return self._dao.find_by_id(match_stat_id)

    def update_match_stat(self, match_stat: MatchStat) -> None:
        self._dao.update(match_stat)

    def delete_match_stat(self, match_stat_id: int) -> None:
        self._dao.delete(match_stat_id)
