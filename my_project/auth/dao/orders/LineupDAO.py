from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Lineup import (
    Lineup,
)  # Ensure this is the correct path


class LineupDAO(GeneralDAO):
    _domain_type = Lineup

    def create(self, lineup: Lineup) -> None:
        self._session.add(lineup)
        self._session.commit()

    def find_all(self) -> List[Lineup]:
        return self._session.query(Lineup).all()

    def find_by_match_id(self, match_id: int) -> List[Lineup]:
        return self._session.query(Lineup).filter(Lineup.match_id == match_id).all()
