from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PlayerStat import (
    PlayerStat,
)  # Ensure this is the correct path


class PlayerStatDAO(GeneralDAO):
    _domain_type = PlayerStat

    def create(self, player_stat: PlayerStat) -> None:
        self._session.add(player_stat)
        self._session.commit()

    def find_all(self) -> List[PlayerStat]:
        return self._session.query(PlayerStat).all()

    def find_by_player_id(self, player_id: int) -> List[PlayerStat]:
        return (
            self._session.query(PlayerStat)
            .filter(PlayerStat.player_id == player_id)
            .all()
        )
