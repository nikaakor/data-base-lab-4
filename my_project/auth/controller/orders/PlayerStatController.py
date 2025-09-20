from typing import List
from my_project.auth.dao.orders.PlayerStatDAO import PlayerStatDAO
from my_project.auth.domain.orders.PlayerStat import PlayerStat


class PlayerStatController:
    _dao = PlayerStatDAO()

    def find_all(self) -> List[PlayerStat]:
        return self._dao.find_all()

    def create(self, player_stat: PlayerStat) -> None:
        self._dao.create(player_stat)

    def find_by_id(self, player_stat_id: int) -> PlayerStat:
        return self._dao.find_by_id(player_stat_id)

    def update(self, player_stat_id: int, player_stat: PlayerStat) -> None:
        self._dao.update(player_stat_id, player_stat)

    def delete(self, player_stat_id: int) -> None:
        self._dao.delete(player_stat_id)
