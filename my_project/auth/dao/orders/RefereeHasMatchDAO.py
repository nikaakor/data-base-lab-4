from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.RefereeHasMatch import (
    RefereeHasMatch,
)  # Ensure this is the correct path


class RefereeHasMatchDAO(GeneralDAO):
    _domain_type = RefereeHasMatch

    def create(self, referee_has_match: RefereeHasMatch) -> None:
        self._session.add(referee_has_match)
        self._session.commit()

    def find_all(self) -> List[RefereeHasMatch]:
        return self._session.query(RefereeHasMatch).all()

    def find_by_match_id(self, match_id: int) -> List[RefereeHasMatch]:
        return (
            self._session.query(RefereeHasMatch)
            .filter(RefereeHasMatch.match_match_id == match_id)
            .all()
        )
