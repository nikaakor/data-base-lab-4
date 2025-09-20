from typing import List
from my_project.auth.dao.orders import TeamDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Team


class TeamService(GeneralService):
    _dao = TeamDAO

    def create(self, team: Team) -> None:
        self._dao.create(team)

    def get_all_teams(self) -> List[Team]:  # type: ignore
        return self._dao.find_all()

    def get_team_by_id(self, team_id: int) -> Team:
        return self._dao.find_by_id(team_id)

    def update_team(self, team: Team) -> None:
        self._dao.update(team)

    def delete_team(self, team_id: int) -> None:
        self._dao.delete(team_id)
