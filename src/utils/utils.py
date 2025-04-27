from typing import Protocol
import dataclasses
import numpy as np


class DynamicalSystem(Protocol):
    def dx(self, t: float, x: np.ndarray) -> np.ndarray:
        ...


@dataclasses.dataclass
class ViolinString(DynamicalSystem):
    epsilon: float

    def dx(self, t: float, x: np.ndarray) -> np.ndarray:
        x_1, x_2 = x
        return np.array([
            x_2,
            -x_1 - self.epsilon * (1 / 3 * x_2 ** 2 - 1)
        ])


@dataclasses.dataclass
class PolarDiff(DynamicalSystem):
    alpha: float = 1
    beta: float = 2
    omega: float = 3

    def dx(self, t: float, x: np.ndarray) -> np.ndarray:
        x_1, x_2 = x
        return np.array([
            x_1 * (self.alpha - x_1) * (self.beta - x_1) * (self.omega - x_1),
            -1
        ])


@dataclasses.dataclass
class Example3_4(DynamicalSystem):
    def dx(self, t: float, x: np.ndarray) -> np.ndarray:
        x_, y_ = x
        return np.array([
            y_ - 8 * x_ ** 3,
            2*y_ - 4*x_ - 2*y_**3
        ])


if __name__ == "__main__":
    violin_string_sys = PolarDiff()
    print(violin_string_sys.dx(0, np.array([1, 3])))
