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


if __name__ == "__main__":
    violin_string_sys = ViolinString(epsilon=10)
    print(violin_string_sys.dx(0, np.array([1, 1])))