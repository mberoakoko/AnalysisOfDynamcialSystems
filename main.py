from src.utils.plotting import Plotter
from src.utils.utils import ViolinString

if __name__ == "__main__":
    Plotter.plot_tragectories(
        system=ViolinString(epsilon=1),
        x_range=(-1, 1),
        y_range=(-1, 1),
        num=10
    )
