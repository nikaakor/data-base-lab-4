from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Match import Match  # Ensure this is the correct path


class MatchDAO(GeneralDAO):
    _domain_type = Match

    def create(self, match: Match) -> None:
        self._session.add(match)
        self._session.commit()

    def find_all(self) -> List[Match]:
        return self._session.query(Match).all()

    def find_by_date(self, match_date: str) -> List[Match]:
        return self._session.query(Match).filter(Match.match_date == match_date).all()
