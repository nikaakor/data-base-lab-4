from typing import List
from my_project.auth.dao.orders.RefereeHasMatchDAO import RefereeHasMatchDAO
from my_project.auth.domain.orders.RefereeHasMatch import RefereeHasMatch


class RefereeHasMatchController:
    _dao = RefereeHasMatchDAO()

    def find_all(self) -> List[RefereeHasMatch]:
        return self._dao.find_all()

    def create(self, referee_has_match: RefereeHasMatch) -> None:
        self._dao.create(referee_has_match)

    def find_by_id(self, referee_has_match_id: int) -> RefereeHasMatch:
        return self._dao.find_by_id(referee_has_match_id)

    def update(
        self, referee_has_match_id: int, referee_has_match: RefereeHasMatch
    ) -> None:
        self._dao.update(referee_has_match_id, referee_has_match)

    def delete(self, referee_has_match_id: int) -> None:
        self._dao.delete(referee_has_match_id)
