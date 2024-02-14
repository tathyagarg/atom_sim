import numpy as np
import supplements as sup


class Space:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.mass = np.array([[0.]*x]*y)  # 0. is a float rather than 0 which is an integer
        self.energy = np.array([[0.]*x]*y)
        self.objects = np.array([[-1]*x]*y)  # There are no objects

    def display(self, display_mass: bool = True) -> None:
        """
        Prints the contents of the space
        The display_mass parameter dictates whether the function prints the mass array or energy array
        """
        target: np.ndarray = [self.energy, self.mass][display_mass]  # Fetches mass if display_mass, energy otherwise
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
