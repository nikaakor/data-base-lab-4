from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Calendar import (
    Calendar,
)  # Ensure this is the correct path


class CalendarDAO(GeneralDAO):
    _domain_type = Calendar

    def create(self, calendar: Calendar) -> None:
        self._session.add(calendar)
        self._session.commit()

    def find_all(self) -> List[Calendar]:
        return self._session.query(Calendar).all()

    def find_by_match_id(self, match_id: int) -> Optional[Calendar]:
        return (
            self._session.query(Calendar).filter(Calendar.match_id == match_id).first()
        )
