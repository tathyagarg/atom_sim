import supplements as sup
import time


class Quark:
    TYPE = 0
    space = None  # Initializing the space

    @classmethod
    def use_space(cls, space):
        """Change the current space"""
        cls.space = space

    def __init__(self, x: int, y: int, mass: float, spin: float, charge: float) -> None:
        self.checksum = sup.generate_checksum(x, y, mass, spin, charge, Quark.TYPE, int(time.time()))
        self.x = x
        self.y = y
        self.mass = mass
        self.spin = spin
        self.charge = charge

    def place(self):
        Quark.space.initialize_object(self)
        return self
