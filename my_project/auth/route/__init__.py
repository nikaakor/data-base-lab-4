"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities
    from .orders.TeamBlueprint import team_bp
    from .orders.PlayerStatBlueprint import player_stat_bp
    from .orders.TeamStatBlueprint import team_stat_bp
    from .orders.StadiumBlueprint import stadium_bp
    from .orders.CalendarBlueprint import calender_bp
    from .orders.CardBlueprint import card_bp
    from .orders.PlayerBlueprint import player_bp
    from .orders.LineupBlueprint import lineup_bp
    from .orders.MatchBlueprint import match_bp
    from .orders.MatchStatBlueprint import match_stat_bp
    from .orders.RefereeBlueprint import referee_bp
    from .orders.RefereeHasMatchBlueprint import referee_has_match_bp

    # Register each blueprint with the app
    app.register_blueprint(team_bp)
    app.register_blueprint(player_stat_bp)
    app.register_blueprint(team_stat_bp)
    app.register_blueprint(stadium_bp)
    app.register_blueprint(calender_bp)
    app.register_blueprint(card_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(lineup_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(match_stat_bp)
    app.register_blueprint(referee_bp)
    app.register_blueprint(referee_has_match_bp)
