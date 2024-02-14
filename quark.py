import space as spc
import supplements as sup


class Quark:
    TYPE = 0

    @classmethod
    def use_space(cls, space: spc.Space):
        """Change the current space"""
        cls.space = space

    def __init__(self, x: int, y: int, mass: float, spin: float) -> None:
        self.checksum = sup.generate_checksum(x, y, mass, spin, Quark.TYPE)
