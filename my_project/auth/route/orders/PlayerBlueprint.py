from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import player_controller
from my_project.auth.domain.orders.Player import Player

player_bp = Blueprint("player", __name__, url_prefix="/player")


@player_bp.get("")
def get_all_players() -> Response:
    players = player_controller.find_all()
    players_dto = [player.put_into_dto() for player in players]
    return make_response(jsonify(players_dto), HTTPStatus.OK)


@player_bp.post("")
def create_player() -> Response:
    content = request.get_json()
    player = Player.create_from_dto(content)
    player_controller.create(player)
    return make_response(jsonify(player.put_into_dto()), HTTPStatus.CREATED)


@player_bp.get("/<int:player_id>")
def get_player(player_id: int) -> Response:
    player = player_controller.find_by_id(player_id)
    if player:
        return make_response(jsonify(player.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Player not found"}), HTTPStatus.NOT_FOUND)


@player_bp.put("/<int:player_id>")
def update_player(player_id: int) -> Response:
    content = request.get_json()
    player = Player.create_from_dto(content)
    player_controller.update(player_id, player)
    return make_response("Player updated", HTTPStatus.OK)


@player_bp.delete("/<int:player_id>")
def delete_player(player_id: int) -> Response:
    player_controller.delete(player_id)
    return make_response("Player deleted", HTTPStatus.NO_CONTENT)
