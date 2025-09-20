from typing import List
from my_project.auth.dao.orders.CardDAO import CardDAO
from my_project.auth.domain.orders.Card import Card


class CardController:
    _dao = CardDAO()

    def find_all(self) -> List[Card]:
        return self._dao.find_all()

    def create(self, card: Card) -> None:
        self._dao.create(card)

    def find_by_id(self, card_id: int) -> Card:
        return self._dao.find_by_id(card_id)

    def update(self, card_id: int, card: Card) -> None:
        self._dao.update(card_id, card)

    def delete(self, card_id: int) -> None:
        self._dao.delete(card_id)
