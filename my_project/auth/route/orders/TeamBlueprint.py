from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import team_controller
from my_project.auth.domain.orders.Team import Team

team_bp = Blueprint("team", __name__, url_prefix="/team")


@team_bp.get("")
def get_all_teams() -> Response:
    teams = team_controller.find_all()
    teams_dto = [team.put_into_dto() for team in teams]
    return make_response(jsonify(teams_dto), HTTPStatus.OK)


@team_bp.post("")
def create_team() -> Response:
    content = request.get_json()
    team = Team.create_from_dto(content)
    team_controller.create(team)
    return make_response(jsonify(team.put_into_dto()), HTTPStatus.CREATED)


@team_bp.get("/<int:team_id>")
def get_team(team_id: int) -> Response:
    team = team_controller.find_by_id(team_id)
    if team:
        return make_response(jsonify(team.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Team not found"}), HTTPStatus.NOT_FOUND)


@team_bp.put("/<int:team_id>")
def update_team(team_id: int) -> Response:
    content = request.get_json()
    team = Team.create_from_dto(content)
    team_controller.update(team_id, team)
    return make_response("Team updated", HTTPStatus.OK)


@team_bp.delete("/<int:team_id>")
def delete_team(team_id: int) -> Response:
    team_controller.delete(team_id)
    return make_response("Team deleted", HTTPStatus.NO_CONTENT)
