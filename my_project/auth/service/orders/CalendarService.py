from typing import List

from my_project.auth.dao import calendarDao
from my_project.auth.dao.orders import (
    CalendarDAO,
    CardDAO,
    GoalDAO,
    LineupDAO,
    MatchDAO,
    MatchStatDAO,
    PlayerDAO,
    PlayerStatDAO,
    RefereeDAO,
    RefereeHasMatchDAO,
    StadiumDAO,
    TeamDAO,
)
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import (
    Calendar,
    Card,
    Goal,
    Lineup,
    Match,
    MatchStat,
    Player,
    PlayerStat,
    Referee,
    RefereeHasMatch,
    Stadium,
    Team,
)


class CalendarService(GeneralService):
    _dao = calendarDao

    def create(self, calendar: Calendar) -> None:
        self._dao.create(calendar)

    def get_all_calendars(self) -> List[Calendar]: # type: ignore
        return self._dao.find_all()

    def get_calendars_by_last_name(self, last_name: str) -> List[Calendar]: # type: ignore
        return self._dao.find_by_last_name(last_name)
