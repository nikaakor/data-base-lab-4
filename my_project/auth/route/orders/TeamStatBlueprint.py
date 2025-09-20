from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import team_stat_controller
from my_project.auth.domain.orders.TeamStat import TeamStat

team_stat_bp = Blueprint("team_stat", __name__, url_prefix="/team_stat")


@team_stat_bp.get("")
def get_all_team_stats() -> Response:
    team_stats = team_stat_controller.find_all()
    team_stats_dto = [team_stat.put_into_dto() for team_stat in team_stats]
    return make_response(jsonify(team_stats_dto), HTTPStatus.OK)


@team_stat_bp.post("")
def create_team_stat() -> Response:
    content = request.get_json()
    team_stat = TeamStat.create_from_dto(content)
    team_stat_controller.create(team_stat)
    return make_response(jsonify(team_stat.put_into_dto()), HTTPStatus.CREATED)


@team_stat_bp.get("/<int:team_stat_id>")
def get_team_stat(team_stat_id: int) -> Response:
    team_stat = team_stat_controller.find_by_id(team_stat_id)
    if team_stat:
        return make_response(jsonify(team_stat.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "TeamStat not found"}), HTTPStatus.NOT_FOUND)


@team_stat_bp.put("/<int:team_stat_id>")
def update_team_stat(team_stat_id: int) -> Response:
    content = request.get_json()
    team_stat = TeamStat.create_from_dto(content)
    team_stat_controller.update(team_stat_id, team_stat)
    return make_response("TeamStat updated", HTTPStatus.OK)


@team_stat_bp.delete("/<int:team_stat_id>")
def delete_team_stat(team_stat_id: int) -> Response:
    team_stat_controller.delete(team_stat_id)
    return make_response("TeamStat deleted", HTTPStatus.NO_CONTENT)
