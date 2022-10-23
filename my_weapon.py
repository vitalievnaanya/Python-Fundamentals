class Weapon:
    shoot_bullets = 0

    def __init__(self, bullets):
        self.bullets = bullets


    def shoot(self):
        if self.bullets > 0:
            self.shoot_bullets += 1
            self.bullets -= 1
            return f'shooting...'
        else:
            return f'no bullets left'

    def __repr__(self):
        if self.shoot_bullets < self.bullets:
            self.amount_of_bullets = abs(self.shoot_bullets - self.bullets)
        else:
            self.amount_of_bullets = 0
        return f'Remaining bullets: {self.amount_of_bullets}'

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
