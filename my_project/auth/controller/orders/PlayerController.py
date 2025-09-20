from typing import List
from my_project.auth.dao.orders.PlayerDAO import PlayerDAO
from my_project.auth.domain.orders.Player import Player


class PlayerController:
    _dao = PlayerDAO()

    def find_all(self) -> List[Player]:
        return self._dao.find_all()

    def create(self, player: Player) -> None:
        self._dao.create(player)

    def find_by_id(self, player_id: int) -> Player:
        return self._dao.find_by_id(player_id)

    def update(self, player_id: int, player: Player) -> None:
        self._dao.update(player_id, player)

    def delete(self, player_id: int) -> None:
        self._dao.delete(player_id)
