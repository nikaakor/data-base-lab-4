from typing import List
from my_project.auth.dao.orders import RefereeHasMatchDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import RefereeHasMatch


class RefereeHasMatchService(GeneralService):
    _dao = RefereeHasMatchDAO

    def create(self, referee_has_match: RefereeHasMatch) -> None:
        self._dao.create(referee_has_match)

    def get_all_referee_has_matches(self) -> List[RefereeHasMatch]:  # type: ignore
        return self._dao.find_all()

    def get_referee_has_match_by_id(
        self, match_id: int, referee_id: int
    ) -> RefereeHasMatch:
        return self._dao.find_by_ids(match_id, referee_id)

    def update_referee_has_match(self, referee_has_match: RefereeHasMatch) -> None:
        self._dao.update(referee_has_match)

    def delete_referee_has_match(self, match_id: int, referee_id: int) -> None:
        self._dao.delete(match_id, referee_id)
