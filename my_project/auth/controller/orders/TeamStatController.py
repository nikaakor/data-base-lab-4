from typing import List
from my_project.auth.dao.orders.TeamStatDAO import TeamStatDAO
from my_project.auth.domain.orders.TeamStat import TeamStat


class TeamStatController:
    _dao = TeamStatDAO()

    def find_all(self) -> List[TeamStat]:
        return self._dao.find_all()

    def create(self, team_stat: TeamStat) -> None:
        self._dao.create(team_stat)

    def find_by_id(self, team_stat_id: int) -> TeamStat:
        return self._dao.find_by_id(team_stat_id)

    def update(self, team_stat_id: int, team_stat: TeamStat) -> None:
        self._dao.update(team_stat_id, team_stat)

    def delete(self, team_stat_id: int) -> None:
        self._dao.delete(team_stat_id)
