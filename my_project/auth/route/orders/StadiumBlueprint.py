from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import stadium_controller
from my_project.auth.domain.orders.Stadium import Stadium

stadium_bp = Blueprint("stadium", __name__, url_prefix="/stadium")


@stadium_bp.get("")
def get_all_stadiums() -> Response:
    stadiums = stadium_controller.find_all()
    stadiums_dto = [stadium.put_into_dto() for stadium in stadiums]
    return make_response(jsonify(stadiums_dto), HTTPStatus.OK)


@stadium_bp.post("")
def create_stadium() -> Response:
    content = request.get_json()
    stadium = Stadium.create_from_dto(content)
    stadium_controller.create(stadium)
    return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.CREATED)


@stadium_bp.get("/<int:stadium_id>")
def get_stadium(stadium_id: int) -> Response:
    stadium = stadium_controller.find_by_id(stadium_id)
    if stadium:
        return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Stadium not found"}), HTTPStatus.NOT_FOUND)


@stadium_bp.put("/<int:stadium_id>")
def update_stadium(stadium_id: int) -> Response:
    content = request.get_json()
    stadium = Stadium.create_from_dto(content)
    stadium_controller.update(stadium_id, stadium)
    return make_response("Stadium updated", HTTPStatus.OK)


@stadium_bp.delete("/<int:stadium_id>")
def delete_stadium(stadium_id: int) -> Response:
    stadium_controller.delete(stadium_id)
    return make_response("Stadium deleted", HTTPStatus.NO_CONTENT)


# from http import HTTPStatus
# from flask import Blueprint, jsonify, Response, request, make_response
# from my_project.auth.controller import stadium_controller
# from my_project.auth.domain.orders.Stadium import Stadium

# stadium_bp = Blueprint("stadium", __name__, url_prefix="/stadium")


# @stadium_bp.get("")
# def get_all_stadiums() -> Response:
#     stadiums = stadium_controller.find_all()
#     stadiums_dto = [stadium.put_into_dto() for stadium in stadiums]
#     return make_response(jsonify(stadiums_dto), HTTPStatus.OK)


# @stadium_bp.post("")
# def create_stadium() -> Response:
#     content = request.get_json()
#     stadium = Stadium.create_from_dto(content)
#     stadium_controller.create(stadium)
#     return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.CREATED)


# @stadium_bp.get("/<int:stadium_id>")
# def get_stadium(stadium_id: int) -> Response:
#     stadium = stadium_controller.find_by_id(stadium_id)
#     if stadium:
#         return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.OK)
#     return make_response(jsonify({"error": "Stadium not found"}), HTTPStatus.NOT_FOUND)


# @stadium_bp.get("/<int:stadium_id>/matches")
# def get_matches_by_stadium(stadium_id: int) -> Response:
#     matches = stadium_controller.find_matches_by_stadium(stadium_id)
#     matches_dto = [match.put_into_dto() for match in matches]
#     return make_response(jsonify(matches_dto), HTTPStatus.OK)


# @stadium_bp.put("/<int:stadium_id>")
# def update_stadium(stadium_id: int) -> Response:
#     content = request.get_json()
#     stadium = Stadium.create_from_dto(content)
#     stadium_controller.update(stadium_id, stadium)
#     return make_response("Stadium updated", HTTPStatus.OK)


# @stadium_bp.delete("/<int:stadium_id>")
# def delete_stadium(stadium_id: int) -> Response:
#     stadium_controller.delete(stadium_id)
#     return make_response("Stadium deleted", HTTPStatus.NO_CONTENT)
