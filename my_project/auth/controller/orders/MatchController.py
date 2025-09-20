from typing import List
from my_project.auth.dao.orders.MatchDAO import MatchDAO
from my_project.auth.domain.orders.Match import Match


class MatchController:
    _dao = MatchDAO()

    def find_all(self) -> List[Match]:
        return self._dao.find_all()

    def create(self, match: Match) -> None:
        self._dao.create(match)

    def find_by_id(self, match_id: int) -> Match:
        return self._dao.find_by_id(match_id)

    def update(self, match_id: int, match: Match) -> None:
        self._dao.update(match_id, match)

    def delete(self, match_id: int) -> None:
        self._dao.delete(match_id)
