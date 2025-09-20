from typing import List
from my_project.auth.dao.orders import MatchDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Match


class MatchService(GeneralService):
    _dao = MatchDAO

    def create(self, match: Match) -> None:
        self._dao.create(match)

    def get_all_matches(self) -> List[Match]:  # type: ignore
        return self._dao.find_all()

    def get_match_by_id(self, match_id: int) -> Match:
        return self._dao.find_by_id(match_id)

    def update_match(self, match: Match) -> None:
        self._dao.update(match)

    def delete_match(self, match_id: int) -> None:
        self._dao.delete(match_id)
