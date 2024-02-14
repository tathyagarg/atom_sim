import numpy as np
import supplements as sup
import quark as qrk


class Space:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.mass = np.array([[0.]*x]*y)  # 0. is a float rather than 0 which is an integer
        self.energy = np.array([[0.]*x]*y)
        self.objects = np.array([[-1]*x]*y)  # There are no objects

    def use_in_quarks(self):
        qrk.Quark.use_space(self)
        return self

    def display(self, target: int = 0) -> None:
        """
        Prints the contents of the space
        The target parameter dictates which space to print
        """
        target: np.ndarray = [self.energy, self.mass, self.objects][target]
        # ^ Fetches mass if display_mass, energy otherwise
        max_len = sup.fetch_float_length(max(target.flatten()))
        for row in target:
            for item in row:
                print(f"{item: >{max_len+1}}", end='')
            print()  # Goes to the next line

    def apply_mass(self, x: int, y: int, mass: float) -> None:
        """Applies the given mass at the given location"""
        self.mass[x, y] = mass

    def apply_mass_at(self, location: tuple[int, int], mass: float) -> None:
        """Applies the given mass at the given location"""
        self.mass[location] = mass

    def apply_energy(self, x: int, y: int, energy: float) -> None:
        """Applies the given mass at the given location"""
        self.energy[x, y] = energy

    def apply_energy_at(self, location: tuple[int, int], energy: float) -> None:
        """Applies the given mass at the given location"""
        self.energy[location] = energy

    def place_object(self, x: int, y: int, obj) -> None:
        """Places an object at a given location"""
        self.objects[x, y] = obj.checksum

    def place_object_at(self, location: tuple[int, int], obj) -> None:
        """Places an object at a given location"""
        self.objects[location] = obj.checksum

    def initialize_object(self, obj) -> None:
        """Initialize an object with mass, energy, and its checksum"""
        x, y = obj.x, obj.y
        self.apply_mass(x, y, obj.mass)
        self.apply_energy(x, y, obj.charge)
        self.place_object(x, y, obj)
