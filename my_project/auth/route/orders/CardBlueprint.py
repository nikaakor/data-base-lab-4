from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import card_controller
from my_project.auth.domain.orders.Card import Card

card_bp = Blueprint("card", __name__, url_prefix="/card")


@card_bp.get("")
def get_all_cards() -> Response:
    cards = card_controller.find_all()
    cards_dto = [card.put_into_dto() for card in cards]
    return make_response(jsonify(cards_dto), HTTPStatus.OK)


@card_bp.post("")
def create_card() -> Response:
    content = request.get_json()
    card = Card.create_from_dto(content)
    card_controller.create(card)
    return make_response(jsonify(card.put_into_dto()), HTTPStatus.CREATED)


@card_bp.get("/<int:card_id>")
def get_card(card_id: int) -> Response:
    card = card_controller.find_by_id(card_id)
    if card:
        return make_response(jsonify(card.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Card not found"}), HTTPStatus.NOT_FOUND)


@card_bp.put("/<int:card_id>")
def update_card(card_id: int) -> Response:
    content = request.get_json()
    card = Card.create_from_dto(content)
    card_controller.update(card_id, card)
    return make_response("Card updated", HTTPStatus.OK)


@card_bp.delete("/<int:card_id>")
def delete_card(card_id: int) -> Response:
    card_controller.delete(card_id)
    return make_response("Card deleted", HTTPStatus.NO_CONTENT)
