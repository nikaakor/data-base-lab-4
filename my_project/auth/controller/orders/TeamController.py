from typing import List
from my_project.auth.dao.orders.TeamDAO import TeamDAO
from my_project.auth.domain.orders.Team import Team


class TeamController:
    _dao = TeamDAO()

    def find_all(self) -> List[Team]:
        return self._dao.find_all()

    def create(self, team: Team) -> None:
        self._dao.create(team)

    def find_by_id(self, team_id: int) -> Team:
        return self._dao.find_by_id(team_id)

    def update(self, team_id: int, team: Team) -> None:
        self._dao.update(team_id, team)

    def delete(self, team_id: int) -> None:
        self._dao.delete(team_id)
