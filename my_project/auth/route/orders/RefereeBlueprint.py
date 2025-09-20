from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import referee_controller
from my_project.auth.domain.orders.Referee import Referee

referee_bp = Blueprint("referee", __name__, url_prefix="/referee")


@referee_bp.get("")
def get_all_referees() -> Response:
    referees = referee_controller.find_all()
    referees_dto = [referee.put_into_dto() for referee in referees]
    return make_response(jsonify(referees_dto), HTTPStatus.OK)


@referee_bp.post("")
def create_referee() -> Response:
    content = request.get_json()
    referee = Referee.create_from_dto(content)
    referee_controller.create(referee)
    return make_response(jsonify(referee.put_into_dto()), HTTPStatus.CREATED)


@referee_bp.get("/<int:referee_id>")
def get_referee(referee_id: int) -> Response:
    referee = referee_controller.find_by_id(referee_id)
    if referee:
        return make_response(jsonify(referee.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Referee not found"}), HTTPStatus.NOT_FOUND)


@referee_bp.put("/<int:referee_id>")
def update_referee(referee_id: int) -> Response:
    content = request.get_json()
    referee = Referee.create_from_dto(content)
    referee_controller.update(referee_id, referee)
    return make_response("Referee updated", HTTPStatus.OK)


@referee_bp.delete("/<int:referee_id>")
def delete_referee(referee_id: int) -> Response:
    referee_controller.delete(referee_id)
    return make_response("Referee deleted", HTTPStatus.NO_CONTENT)
