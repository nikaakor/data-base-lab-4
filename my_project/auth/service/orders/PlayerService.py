from typing import List
from my_project.auth.dao.orders import PlayerDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Player


class PlayerService(GeneralService):
    _dao = PlayerDAO

    def create(self, player: Player) -> None:
        self._dao.create(player)

    def get_all_players(self) -> List[Player]:  # type: ignore
        return self._dao.find_all()

    def get_player_by_id(self, player_id: int) -> Player:
        return self._dao.find_by_id(player_id)

    def update_player(self, player: Player) -> None:
        self._dao.update(player)

    def delete_player(self, player_id: int) -> None:
        self._dao.delete(player_id)
