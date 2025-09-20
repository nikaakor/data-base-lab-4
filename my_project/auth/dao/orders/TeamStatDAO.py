from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.TeamStat import (
    TeamStat,
)  # Ensure this is the correct path


class TeamStatDAO(GeneralDAO):
    _domain_type = TeamStat

    def create(self, team_stat: TeamStat) -> None:
        self._session.add(team_stat)
        self._session.commit()

    def find_all(self) -> List[TeamStat]:
        return self._session.query(TeamStat).all()

    def find_by_team_id(self, team_id: int) -> List[TeamStat]:
        return self._session.query(TeamStat).filter(TeamStat.team_id == team_id).all()
