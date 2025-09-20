from typing import List
from my_project.auth.dao.orders.GoalDAO import GoalDAO
from my_project.auth.domain.orders.Goal import Goal


class GoalController:
    _dao = GoalDAO()

    def find_all(self) -> List[Goal]:
        return self._dao.find_all()

    def create(self, goal: Goal) -> None:
        self._dao.create(goal)

    def find_by_id(self, goal_id: int) -> Goal:
        return self._dao.find_by_id(goal_id)

    def update(self, goal_id: int, goal: Goal) -> None:
        self._dao.update(goal_id, goal)

    def delete(self, goal_id: int) -> None:
        self._dao.delete(goal_id)
