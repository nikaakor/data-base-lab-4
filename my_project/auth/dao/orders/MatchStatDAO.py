from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.MatchStat import (
    MatchStat,
)  # Ensure this is the correct path


class MatchStatDAO(GeneralDAO):
    _domain_type = MatchStat

    def create(self, match_stat: MatchStat) -> None:
        self._session.add(match_stat)
        self._session.commit()

    def find_all(self) -> List[MatchStat]:
        return self._session.query(MatchStat).all()

    def find_by_match_id(self, match_id: int) -> Optional[MatchStat]:
        return (
            self._session.query(MatchStat)
            .filter(MatchStat.match_id == match_id)
            .first()
        )
