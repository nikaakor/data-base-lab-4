from typing import List
from my_project.auth.dao.orders import GoalDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Goal


class GoalService(GeneralService):
    _dao = GoalDAO

    def create(self, goal: Goal) -> None:
        self._dao.create(goal)

    def get_all_goals(self) -> List[Goal]:  # type: ignore
        return self._dao.find_all()

    def get_goal_by_id(self, goal_id: int) -> Goal:
        return self._dao.find_by_id(goal_id)

    def update_goal(self, goal: Goal) -> None:
        self._dao.update(goal)

    def delete_goal(self, goal_id: int) -> None:
        self._dao.delete(goal_id)
