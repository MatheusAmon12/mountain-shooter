from abc import ABC
from unittest import case

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory(ABC):
    @staticmethod
    def get_entity(entity_name: str, position: tuple[int, int] = (0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []

                for item in range(7):
                    list_bg.append(Background(f"Level1Bg{item}", position))
                    list_bg.append(Background(f"Level1Bg{item}", position=(WIN_WIDTH, 0)))

                return list_bg
            case "Player1":
                return Player("Player1", (10, WIN_HEIGHT / 2))
        return None