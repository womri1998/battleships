MISS = 0
HIT = 1
DROWNED = 2


class Board:
    """
    board contains the list of submarines of the player

    :param list submarines: game submarines
    """
    def __init__(self, submarines: list):
        self.submarines = submarines

    """
    checks if the enemy hit, and if he did determines whether he drowned a submarine or not
    
    :param (int, int) target: the location which the enemy targeted
    :return: MISS, HIT or DROWNED
    """
    def enemy_attack(self, target: [int, int]) -> int:
        for submarine in self.submarines:
            if submarine.is_hit(target):
                return HIT if submarine.is_alive() else DROWNED
        return MISS

    """
    checks if the player still has a living submarine
    
    :return: True iff contains a living submarine
    """
    def is_alive(self) -> bool:
        return True in [submarine.is_alive() for submarine in self.submarines]
