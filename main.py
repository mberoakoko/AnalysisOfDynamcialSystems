from src.utils.plotting import Plotter
from src.utils.utils import ViolinString, PolarDiff, Example3_4

if __name__ == "__main__":
    # Plotter.plot_tragectories(
    #     system=ViolinString(epsilon=2),
    #     x_range=(-1, 1),
    #     y_range=(-1, 1),
    #     num=20
    # )
    Plotter.plot_phase_plot(
        system=Example3_4(),
        x_range=(-1, 1),
        y_range=(-1, 1),
        num=10
    )