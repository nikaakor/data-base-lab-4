from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import match_controller
from my_project.auth.domain.orders.Match import Match

match_bp = Blueprint("match", __name__, url_prefix="/match")


@match_bp.get("")
def get_all_matches() -> Response:
    matches = match_controller.find_all()
    matches_dto = [match.put_into_dto() for match in matches]
    return make_response(jsonify(matches_dto), HTTPStatus.OK)


@match_bp.post("")
def create_match() -> Response:
    content = request.get_json()
    match = Match.create_from_dto(content)
    match_controller.create(match)
    return make_response(jsonify(match.put_into_dto()), HTTPStatus.CREATED)


@match_bp.get("/<int:match_id>")
def get_match(match_id: int) -> Response:
    match = match_controller.find_by_id(match_id)
    if match:
        return make_response(jsonify(match.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Match not found"}), HTTPStatus.NOT_FOUND)


@match_bp.put("/<int:match_id>")
def update_match(match_id: int) -> Response:
    content = request.get_json()
    match = Match.create_from_dto(content)
    match_controller.update(match_id, match)
    return make_response("Match updated", HTTPStatus.OK)


@match_bp.delete("/<int:match_id>")
def delete_match(match_id: int) -> Response:
    match_controller.delete(match_id)
    return make_response("Match deleted", HTTPStatus.NO_CONTENT)
