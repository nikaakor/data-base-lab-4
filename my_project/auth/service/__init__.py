"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import services using HelloWorld naming convention
from .orders.RefereeHasMatchService import RefereeHasMatchService
from .orders.CardService import CardService
from .orders.MatchStatService import MatchStatService
from .orders.LineupService import LineupService
from .orders.StadiumService import StadiumService
from .orders.CalendarService import CalendarService
from .orders.PlayerStatService import PlayerStatService
from .orders.TeamService import TeamService
from .orders.PlayerService import PlayerService
from .orders.MatchService import MatchService
from .orders.GoalService import GoalService
from .orders.RefereeService import RefereeService

# Initialize service instances with HelloWorld naming style
refereeHasMatchService = RefereeHasMatchService()
cardService = CardService()
matchStatService = MatchStatService()
lineupService = LineupService()
stadiumService = StadiumService()
calendarService = CalendarService()
playerStatService = PlayerStatService()
teamService = TeamService()
playerService = PlayerService()
matchService = MatchService()
goalService = GoalService()
refereeService = RefereeService()
