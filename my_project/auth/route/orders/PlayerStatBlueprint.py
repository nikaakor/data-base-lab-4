from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import player_stat_controller
from my_project.auth.domain.orders.PlayerStat import PlayerStat

player_stat_bp = Blueprint("player_stat", __name__, url_prefix="/player_stat")


@player_stat_bp.get("")
def get_all_player_stats() -> Response:
    player_stats = player_stat_controller.find_all()
    player_stats_dto = [player_stat.put_into_dto() for player_stat in player_stats]
    return make_response(jsonify(player_stats_dto), HTTPStatus.OK)


@player_stat_bp.post("")
def create_player_stat() -> Response:
    content = request.get_json()
    player_stat = PlayerStat.create_from_dto(content)
    player_stat_controller.create(player_stat)
    return make_response(jsonify(player_stat.put_into_dto()), HTTPStatus.CREATED)


@player_stat_bp.get("/<int:player_stat_id>")
def get_player_stat(player_stat_id: int) -> Response:
    player_stat = player_stat_controller.find_by_id(player_stat_id)
    if player_stat:
        return make_response(jsonify(player_stat.put_into_dto()), HTTPStatus.OK)
    return make_response(
        jsonify({"error": "PlayerStat not found"}), HTTPStatus.NOT_FOUND
    )


@player_stat_bp.put("/<int:player_stat_id>")
def update_player_stat(player_stat_id: int) -> Response:
    content = request.get_json()
    player_stat = PlayerStat.create_from_dto(content)
    player_stat_controller.update(player_stat_id, player_stat)
    return make_response("PlayerStat updated", HTTPStatus.OK)


@player_stat_bp.delete("/<int:player_stat_id>")
def delete_player_stat(player_stat_id: int) -> Response:
    player_stat_controller.delete(player_stat_id)
    return make_response("PlayerStat deleted", HTTPStatus.NO_CONTENT)
