from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Card import Card  # Ensure this is the correct path


class CardDAO(GeneralDAO):
    _domain_type = Card

    def create(self, card: Card) -> None:
        self._session.add(card)
        self._session.commit()

    def find_all(self) -> List[Card]:
        return self._session.query(Card).all()

    def find_by_type(self, card_type: str) -> List[Card]:
        return self._session.query(Card).filter(Card.card_type == card_type).all()
