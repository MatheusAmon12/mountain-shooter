from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
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
    def __verify_collision_entity(entity_ref, entity_to_compare):
        valid_interaction = False

        if isinstance(entity_ref, Enemy) and isinstance(entity_to_compare, PlayerShot):
            valid_interaction = True

        elif isinstance(entity_ref, PlayerShot) and isinstance(entity_to_compare, Enemy):
            valid_interaction = True

        elif isinstance(entity_ref, Player) and isinstance(entity_to_compare, EnemyShot):
            valid_interaction = True

        elif isinstance(entity_ref, EnemyShot) and isinstance(entity_to_compare, Player):
            valid_interaction = True

        if valid_interaction:
            if (
                    entity_ref.rect.right >= entity_to_compare.rect.left and
                    entity_ref.rect.left <= entity_to_compare.rect.right and
                    entity_ref.rect.bottom >= entity_to_compare.rect.top and
                    entity_ref.rect.top <= entity_to_compare.rect.bottom
            ):
                entity_ref.health -= entity_to_compare.damage
                entity_to_compare.health -= entity_ref.damage
                entity_ref.last_damage = entity_to_compare.name
                entity_to_compare.last_damage = entity_ref.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_ref = entity_list[i]

            EntityMediator.__verify_collision_window(entity_ref)

            # dedup all comparisons
            for j in range(i + 1, len(entity_list)):
                entity_to_compare = entity_list[j]

                EntityMediator.__verify_collision_entity(entity_ref, entity_to_compare)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
