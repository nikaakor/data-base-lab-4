from typing import List
from my_project.auth.dao.orders import CardDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Card


class CardService(GeneralService):
    _dao = CardDAO

    def create(self, card: Card) -> None:
        self._dao.create(card)

    def get_all_cards(self) -> List[Card]: # type: ignore
        return self._dao.find_all()

    def get_card_by_id(self, card_id: int) -> Card:
        return self._dao.find_by_id(card_id)

    def update_card(self, card: Card) -> None:
        self._dao.update(card)

    def delete_card(self, card_id: int) -> None:
        self._dao.delete(card_id)
