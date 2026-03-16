from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0

        if isinstance(entity, PlayerShot):
            if entity.rect.left >= WIN_WIDTH:
                entity.health = 0

        if isinstance(entity, EnemyShot):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for item in range(len(entity_list)):
            entity = entity_list[item]

            EntityMediator.__verify_collision_window(entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)

