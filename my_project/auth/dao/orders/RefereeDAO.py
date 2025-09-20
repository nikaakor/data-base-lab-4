from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Referee import Referee


class RefereeDAO(GeneralDAO):
    _domain_type = Referee

    def create(self, referee: Referee) -> None:
        self._session.add(referee)
        self._session.commit()

    def find_all(self) -> List[Referee]:
        return self._session.query(Referee).all()

    def find_by_name(self, referee_name: str) -> List[Referee]:
        return (
            self._session.query(Referee)
            .filter(Referee.referee_name == referee_name)
            .all()
        )
