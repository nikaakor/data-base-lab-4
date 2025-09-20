from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Player import (
    Player,
)  # Ensure this is the correct path


class PlayerDAO(GeneralDAO):
    _domain_type = Player

    def create(self, player: Player) -> None:
        self._session.add(player)
        self._session.commit()

    def find_all(self) -> List[Player]:
        return self._session.query(Player).all()

    def find_by_name(self, player_name: str) -> List[Player]:
        return (
            self._session.query(Player).filter(Player.player_name == player_name).all()
        )
