from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import referee_has_match_controller
from my_project.auth.domain.orders.RefereeHasMatch import RefereeHasMatch

referee_has_match_bp = Blueprint(
    "referee_has_match", __name__, url_prefix="/referee_has_match"
)


@referee_has_match_bp.get("")
def get_all_referee_has_matches() -> Response:
    referee_has_matches = referee_has_match_controller.find_all()
    referee_has_matches_dto = [
        referee_has_match.put_into_dto() for referee_has_match in referee_has_matches
    ]
    return make_response(jsonify(referee_has_matches_dto), HTTPStatus.OK)


@referee_has_match_bp.post("")
def create_referee_has_match() -> Response:
    content = request.get_json()
    referee_has_match = RefereeHasMatch.create_from_dto(content)
    referee_has_match_controller.create(referee_has_match)
    return make_response(jsonify(referee_has_match.put_into_dto()), HTTPStatus.CREATED)


@referee_has_match_bp.get("/<int:referee_has_match_id>")
def get_referee_has_match(referee_has_match_id: int) -> Response:
    referee_has_match = referee_has_match_controller.find_by_id(referee_has_match_id)
    if referee_has_match:
        return make_response(jsonify(referee_has_match.put_into_dto()), HTTPStatus.OK)
    return make_response(
        jsonify({"error": "RefereeHasMatch not found"}), HTTPStatus.NOT_FOUND
    )


@referee_has_match_bp.put("/<int:referee_has_match_id>")
def update_referee_has_match(referee_has_match_id: int) -> Response:
    content = request.get_json()
    referee_has_match = RefereeHasMatch.create_from_dto(content)
    referee_has_match_controller.update(referee_has_match_id, referee_has_match)
    return make_response("RefereeHasMatch updated", HTTPStatus.OK)


@referee_has_match_bp.delete("/<int:referee_has_match_id>")
def delete_referee_has_match(referee_has_match_id: int) -> Response:
    referee_has_match_controller.delete(referee_has_match_id)
    return make_response("RefereeHasMatch deleted", HTTPStatus.NO_CONTENT)
