from typing import List
from my_project.auth.dao.orders.CalendarDAO import CalendarDAO
from my_project.auth.domain.orders.Calendar import Calendar


class CalendarController:
    _dao = CalendarDAO()

    def find_all(self) -> List[Calendar]:
        return self._dao.find_all()

    def create(self, calendar: Calendar) -> None:
        self._dao.create(calendar)

    def find_by_id(self, calendar_id: int) -> Calendar:
        return self._dao.find_by_id(calendar_id)

    def update(self, calendar_id: int, calendar: Calendar) -> None:
        self._dao.update(calendar_id, calendar)

    def delete(self, calendar_id: int) -> None:
        self._dao.delete(calendar_id)
