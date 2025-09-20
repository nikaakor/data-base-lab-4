from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import goal_controller
from my_project.auth.domain.orders.Goal import Goal

goal_bp = Blueprint("goal", __name__, url_prefix="/goal")


@goal_bp.get("")
def get_all_goals() -> Response:
    goals = goal_controller.find_all()
    goals_dto = [goal.put_into_dto() for goal in goals]
    return make_response(jsonify(goals_dto), HTTPStatus.OK)


@goal_bp.post("")
def create_goal() -> Response:
    content = request.get_json()
    goal = Goal.create_from_dto(content)
    goal_controller.create(goal)
    return make_response(jsonify(goal.put_into_dto()), HTTPStatus.CREATED)


@goal_bp.get("/<int:goal_id>")
def get_goal(goal_id: int) -> Response:
    goal = goal_controller.find_by_id(goal_id)
    if goal:
        return make_response(jsonify(goal.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Goal not found"}), HTTPStatus.NOT_FOUND)


@goal_bp.put("/<int:goal_id>")
def update_goal(goal_id: int) -> Response:
    content = request.get_json()
    goal = Goal.create_from_dto(content)
    goal_controller.update(goal_id, goal)
    return make_response("Goal updated", HTTPStatus.OK)


@goal_bp.delete("/<int:goal_id>")
def delete_goal(goal_id: int) -> Response:
    goal_controller.delete(goal_id)
    return make_response("Goal deleted", HTTPStatus.NO_CONTENT)
