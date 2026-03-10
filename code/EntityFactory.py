from abc import ABC

from code.Background import Background
from code.Const import WIN_WIDTH


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
        return None