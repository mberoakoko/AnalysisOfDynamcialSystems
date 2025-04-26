import numpy as np
import itertools
from scipy import integrate
from src.utils.utils import DynamicalSystem
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib
matplotlib.use("TkAgg")
plt.rcParams.update({"font.size": 8})
plt.style.use("dark_background")

class Plotter:
    @staticmethod
    def plot_phase_plot(system: DynamicalSystem,
                        x_range: tuple[float, float], y_range: tuple[float, float],
                        num=10) -> None:
        x = np.linspace(x_range[0], x_range[1], num)
        y = np.linspace(y_range[0], y_range[1], num)
        x_, y_ = np.meshgrid(x, y)
        gradients = (
            system.dx(0, np.array([x_[section], y_[section]]))
            for section in itertools.product(range(len(x)), range(len(y)))
        )
        gradients = np.array(list(gradients))
        u, v = np.meshgrid(gradients[:, 0], gradients[:, 1])
        plt.quiver(x_, y_, u, v, color="C1", scale_units="xy", units="xy")
        plt.show()

    @staticmethod
    def plot_tragectories(system: DynamicalSystem,
                          x_range: tuple[float, float], y_range: tuple[float, float], num: int, dt: float = 0.01,
                          t_final: float = 10):
        x = np.linspace(x_range[0], x_range[1], num)
        y = np.linspace(y_range[0], y_range[1], num)
        x_, y_ = np.meshgrid(x, y)
        t_span = np.linspace(0, t_final, round(t_final/dt))
        trajectorie_raw = (
            integrate.solve_ivp(system.dx, t_span=(0, t_final),t_eval=t_span, y0=np.array([x_[section], y_[section]]))
            for section in itertools.product(range(len(x)), range(len(y)))
        )

        fig: Figure = plt.figure(figsize=(16//2, 9//2))
        ax: Axes = fig.add_subplot()
        for trajectory in map(lambda item: item.y, trajectorie_raw):
            ax.plot(trajectory[0, :], trajectory[1, :], color="C4", linewidth=0.7)

        ax.set_title(f"Phase plot of {system.__class__.__name__}")
        plt.tight_layout()
        plt.show()

