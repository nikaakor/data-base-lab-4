from typing import List
from my_project.auth.dao.orders import TeamStatDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import TeamStat


class TeamStatService(GeneralService):
    _dao = TeamStatDAO

    def create(self, team_stat: TeamStat) -> None:
        self._dao.create(team_stat)

    def get_all_team_stats(self) -> List[TeamStat]:  # type: ignore
        return self._dao.find_all()

    def get_team_stat_by_id(self, team_stat_id: int) -> TeamStat:
        return self._dao.find_by_id(team_stat_id)

    def update_team_stat(self, team_stat: TeamStat) -> None:
        self._dao.update(team_stat)

    def delete_team_stat(self, team_stat_id: int) -> None:
        self._dao.delete(team_stat_id)
