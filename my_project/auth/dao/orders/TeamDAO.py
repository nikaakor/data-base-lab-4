from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Team import Team  # Ensure this is the correct path


class TeamDAO(GeneralDAO):
    _domain_type = Team

    def create(self, team: Team) -> None:
        self._session.add(team)
        self._session.commit()

    def find_all(self) -> List[Team]:
        return self._session.query(Team).all()

    def find_by_name(self, team_name: str) -> Optional[Team]:
        return self._session.query(Team).filter(Team.team_name == team_name).first()
