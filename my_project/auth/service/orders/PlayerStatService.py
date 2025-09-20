from typing import List
from my_project.auth.dao.orders import PlayerStatDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import PlayerStat


class PlayerStatService(GeneralService):
    _dao = PlayerStatDAO

    def create(self, player_stat: PlayerStat) -> None:
        self._dao.create(player_stat)

    def get_all_player_stats(self) -> List[PlayerStat]:  # type: ignore
        return self._dao.find_all()

    def get_player_stat_by_id(self, player_stat_id: int) -> PlayerStat:
        return self._dao.find_by_id(player_stat_id)

    def update_player_stat(self, player_stat: PlayerStat) -> None:
        self._dao.update(player_stat)

    def delete_player_stat(self, player_stat_id: int) -> None:
        self._dao.delete(player_stat_id)
