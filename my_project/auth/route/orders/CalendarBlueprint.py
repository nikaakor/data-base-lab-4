from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import calendar_controller
from my_project.auth.domain.orders.Calendar import Calendar

calender_bp = Blueprint("calendar", __name__, url_prefix="/calendar")


@calender_bp.get("")
def get_all_calendars() -> Response:
    calendars = calendar_controller.find_all()
    calendars_dto = [calendar.put_into_dto() for calendar in calendars]
    return make_response(jsonify(calendars_dto), HTTPStatus.OK)


@calender_bp.post("")
def create_calendar() -> Response:
    content = request.get_json()
    calendar = Calendar.create_from_dto(content)
    calendar_controller.create(calendar)
    return make_response(jsonify(calendar.put_into_dto()), HTTPStatus.CREATED)


@calender_bp.get("/<int:calendar_id>")
def get_calendar(calendar_id: int) -> Response:
    calendar = calendar_controller.find_by_id(calendar_id)
    if calendar:
        return make_response(jsonify(calendar.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Calendar not found"}), HTTPStatus.NOT_FOUND)


@calender_bp.put("/<int:calendar_id>")
def update_calendar(calendar_id: int) -> Response:
    content = request.get_json()
    calendar = Calendar.create_from_dto(content)
    calendar_controller.update(calendar_id, calendar)
    return make_response("Calendar updated", HTTPStatus.OK)


@calender_bp.delete("/<int:calendar_id>")
def delete_calendar(calendar_id: int) -> Response:
    calendar_controller.delete(calendar_id)
    return make_response("Calendar deleted", HTTPStatus.NO_CONTENT)
