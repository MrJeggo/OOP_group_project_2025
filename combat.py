from player import Player
from teachers import Teacher
from Item import Weapon


class Combat:
    def __init__(self, player: Player, teacher: Teacher, weapon: Weapon | None = None, verbose: bool = True):
        self.player = player
        self.teacher = teacher
        self.weapon = weapon or self._find_weapon_in_inventory()
        self.verbose = verbose
        if self.weapon is None:
            raise ValueError("Player has no weapon equipped or in inventory.")

    # ---- helpers -------------------------------------------------------------

    def _find_weapon_in_inventory(self) -> Weapon | None:
        """Find the first Weapon object in player's inventory [(item_obj, qty), ...]."""
        for entry in getattr(self.player, "inventory", []):
            item_obj = entry[0]
            if isinstance(item_obj, Weapon):
                return item_obj
        return None

    def _weapon_multiplier(self) -> float:
        """Bonus/penalty based on weapon effectiveness vs teacher.subject."""
        subject = getattr(self.teacher, "subject", None)
        if subject and isinstance(self.weapon.effective_against, list) and subject in self.weapon.effective_against:
            return 1.5  # super effective
        if subject and isinstance(self.weapon.ineffective_against, list) and subject in self.weapon.ineffective_against:
            return 0.5  # not very effective
        return 1.0

    def _confidence_reduction(self) -> float:
        """Same idea as your print: confidence / (confidence + 100)."""
        c = max(0, getattr(self.player, "confidence", 0))
        return c / (c + 100)

    # ---- actions ------------------------------------------------------------

    def player_attack(self) -> int:
        """Player hits teacher. Returns damage dealt."""
        mult = self._weapon_multiplier()
        dmg = int(round(self.weapon.attack_power * mult))
        self.teacher.health = max(0, self.teacher.health - dmg)

        if self.verbose:
            print(f"You hit {self.teacher.getName()} with {self.weapon.name} for {dmg} damage "
                  f"(multiplier x{mult}). Teacher HP: {self.teacher.health}")
        return dmg

    def teacher_attack(self) -> int:
        """Teacher hits player. Returns damage dealt after reduction."""
        raw = int(getattr(self.teacher, "attackdamage", 0))
        reduction = self._confidence_reduction()
        actual = max(0, int(round(raw * (1 - reduction))))

        # apply to sanity as HP
        self.player.adjust_sanity(-actual)

        if self.verbose:
            print(f"{self.teacher.getName()} hits you for {actual} (from {raw}, "
                  f"{round(reduction*100,1)}% reduced). "
                  f"Your sanity: {self.player.sanity}/{self.player.max_sanity}")
        return actual

    # ---- flow control -------------------------------------------------------

    def is_over(self) -> bool:
        return self.teacher.health <= 0 or self.player.is_dead()

    def winner(self) -> str | None:
        if self.teacher.health <= 0 and not self.player.is_dead():
            return "player"
        if self.player.is_dead() and self.teacher.health > 0:
            return "teacher"
        return None  # still fighting or double-KO (rare with current logic)

    def run_turn(self, action: str = "attack") -> str | None:
        """
        One full turn: player action then teacher counter if still alive.
        Returns 'player', 'teacher', or None if fight continues.
        """
        if self.is_over():
            return self.winner()

        if action == "attack":
            self.player_attack()
        # future: elif action == "block": ...
        # future: elif action == "use_item": ...

        if not self.is_over():
            self.teacher_attack()

        return self.winner()