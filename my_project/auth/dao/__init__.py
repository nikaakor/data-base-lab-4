"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Orders DB imports for DAOs corresponding to each entity, using HelloWorld naming
from .orders.MatchStatDAO import MatchStatDAO
from .orders.RefereeDAO import RefereeDAO
from .orders.PlayerStatDAO import PlayerStatDAO
from .orders.RefereeHasMatchDAO import RefereeHasMatchDAO
from .orders.StadiumDAO import StadiumDAO
from .orders.TeamDAO import TeamDAO
from .orders.CardDAO import CardDAO
from .orders.MatchDAO import MatchDAO
from .orders.CalendarDAO import CalendarDAO
from .orders.PlayerDAO import PlayerDAO
from .orders.GoalDAO import GoalDAO
from .orders.LineupDAO import LineupDAO

# Initialize DAOs for each entity with HelloWorld naming style
matchStatDao = MatchStatDAO()
refereeDao = RefereeDAO()
playerStatDao = PlayerStatDAO()
refereeHasMatchDao = RefereeHasMatchDAO()
stadiumDao = StadiumDAO()
teamDao = TeamDAO()
cardDao = CardDAO()
matchDao = MatchDAO()
calendarDao = CalendarDAO()
playerDao = PlayerDAO()
goalDao = GoalDAO()
lineupDao = LineupDAO()
