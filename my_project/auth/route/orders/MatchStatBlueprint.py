from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import match_stat_controller
from my_project.auth.domain.orders.MatchStat import MatchStat

match_stat_bp = Blueprint("match_stat", __name__, url_prefix="/match_stat")


@match_stat_bp.get("")
def get_all_match_stats() -> Response:
    match_stats = match_stat_controller.find_all()
    match_stats_dto = [match_stat.put_into_dto() for match_stat in match_stats]
    return make_response(jsonify(match_stats_dto), HTTPStatus.OK)


@match_stat_bp.post("")
def create_match_stat() -> Response:
    content = request.get_json()
    match_stat = MatchStat.create_from_dto(content)
    match_stat_controller.create(match_stat)
    return make_response(jsonify(match_stat.put_into_dto()), HTTPStatus.CREATED)


@match_stat_bp.get("/<int:match_stat_id>")
def get_match_stat(match_stat_id: int) -> Response:
    match_stat = match_stat_controller.find_by_id(match_stat_id)
    if match_stat:
        return make_response(jsonify(match_stat.put_into_dto()), HTTPStatus.OK)
    return make_response(
        jsonify({"error": "MatchStat not found"}), HTTPStatus.NOT_FOUND
    )


@match_stat_bp.put("/<int:match_stat_id>")
def update_match_stat(match_stat_id: int) -> Response:
    content = request.get_json()
    match_stat = MatchStat.create_from_dto(content)
    match_stat_controller.update(match_stat_id, match_stat)
    return make_response("MatchStat updated", HTTPStatus.OK)


@match_stat_bp.delete("/<int:match_stat_id>")
def delete_match_stat(match_stat_id: int) -> Response:
    match_stat_controller.delete(match_stat_id)
    return make_response("MatchStat deleted", HTTPStatus.NO_CONTENT)
