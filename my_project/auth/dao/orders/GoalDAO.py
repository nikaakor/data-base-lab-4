from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Goal import Goal  # Ensure this is the correct path


class GoalDAO(GeneralDAO):
    _domain_type = Goal

    def create(self, goal: Goal) -> None:
        self._session.add(goal)
        self._session.commit()

    def find_all(self) -> List[Goal]:
        return self._session.query(Goal).all()

    def find_by_player_id(self, player_id: int) -> List[Goal]:
        return self._session.query(Goal).filter(Goal.player_id == player_id).all()
