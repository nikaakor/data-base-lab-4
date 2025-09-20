from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import lineup_controller
from my_project.auth.domain.orders.Lineup import Lineup

lineup_bp = Blueprint("lineup", __name__, url_prefix="/lineup")


@lineup_bp.get("")
def get_all_lineups() -> Response:
    lineups = lineup_controller.find_all()
    lineups_dto = [lineup.put_into_dto() for lineup in lineups]
    return make_response(jsonify(lineups_dto), HTTPStatus.OK)


@lineup_bp.post("")
def create_lineup() -> Response:
    content = request.get_json()
    lineup = Lineup.create_from_dto(content)
    lineup_controller.create(lineup)
    return make_response(jsonify(lineup.put_into_dto()), HTTPStatus.CREATED)


@lineup_bp.get("/<int:lineup_id>")
def get_lineup(lineup_id: int) -> Response:
    lineup = lineup_controller.find_by_id(lineup_id)
    if lineup:
        return make_response(jsonify(lineup.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Lineup not found"}), HTTPStatus.NOT_FOUND)


@lineup_bp.put("/<int:lineup_id>")
def update_lineup(lineup_id: int) -> Response:
    content = request.get_json()
    lineup = Lineup.create_from_dto(content)
    lineup_controller.update(lineup_id, lineup)
    return make_response("Lineup updated", HTTPStatus.OK)


@lineup_bp.delete("/<int:lineup_id>")
def delete_lineup(lineup_id: int) -> Response:
    lineup_controller.delete(lineup_id)
    return make_response("Lineup deleted", HTTPStatus.NO_CONTENT)
