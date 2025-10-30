from matplotlib import pyplot as plt
import numpy as np
class Plotter:
    def __init__(self, dictionary: dict[tuple[np.float64, str], list[np.array]]):
        self.dictionary = dictionary

    def get_stats(self, time_series):
        stats = {"mean": np.mean, "std": np.std, "max": np.max, "min": np.min}
        transposed = np.array(time_series).T
        return {stat: np.array([func(ts) for ts in transposed]) for stat, func in stats.items()}

    def plot_histogram(self):
        new_dict = {key[0]: len(value) for key, value in self.dictionary.items()}
        plt.bar(list(new_dict.keys()), list(new_dict.values()))
        plt.xlabel("Class")
        plt.ylabel("Number of time series")
        plt.title("Number of time series per class")
        plt.show()

    def plot_time_series(self, time_series, label="unknown", dimension="unknown", ax=None):
        if ax is None:
            ax = plt.gca()

        for ts in time_series:
            ax.plot(ts)
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.set_title(f"All time series for class {label}\nand dimension {dimension}")

    def plot_stats(self, time_series, label="unknown", dimension="unknown", ax=None):
        stats = self.get_stats(time_series)
        upper_bound = stats["mean"] + 3 * stats["std"]
        lower_bound = stats["mean"] - 3 * stats["std"]

        if ax is None:
            ax = plt.gca()

        ax.plot(stats["mean"], label="mean")
        ax.plot(stats["max"], label="max")
        ax.plot(stats["min"], label="min")
        ax.plot(upper_bound, label="+3 std")
        ax.plot(lower_bound, label="-3 std")

        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.set_title(f"Time series statistics for dimension {dimension}\n and class {label}")
        ax.fill_between(range(len(stats["mean"])), upper_bound, lower_bound, color='blue', alpha=0.2, label="±3 std")
        ax.legend()

    def plot_all_stats_from_dict(self):
        for dimension_idx in "xyz":
            fig, axs = plt.subplots(3, 3, figsize=(15, 15))
            axs = axs.flatten()

            idx = 0
            for class_idx in range(1,9):
                key = (np.float64(class_idx), dimension_idx)
                if key in self.dictionary:
                    self.plot_stats(self.dictionary[key], label=np.float64(class_idx), dimension=dimension_idx, ax=axs[idx])
                    idx += 1

            for i in range(idx, 9):
                axs[i].axis('off')

            plt.subplots_adjust(wspace=0.3, hspace=0.3)
            plt.tight_layout()
            plt.show()

    def plot_all_series_from_dict(self):
        for dimension_idx in "xyz":
            fig, axs = plt.subplots(3, 3, figsize=(15, 15))
            axs = axs.flatten()

            idx = 0
            for class_idx in range(1,9):
                key = (np.float64(class_idx), dimension_idx)
                if key in self.dictionary:
                    self.plot_time_series(self.dictionary[key], label=np.float64(class_idx), dimension=dimension_idx, ax=axs[idx])
                    idx += 1

            for i in range(idx, 9):
                axs[i].axis('off')

            plt.subplots_adjust(wspace=0.3, hspace=0.3)
            plt.tight_layout()
            plt.show()

    def plot_mean_comparison(self):
        fig, axs = plt.subplots(1, 3, figsize=(18, 6))

        for i, dimension_idx in enumerate("xyz"):
            for class_idx in range(1, 9):
                key = (np.float64(class_idx), dimension_idx)
                if key in self.dictionary:
                    time_series = self.dictionary[key]
                    mean_values = np.mean(np.array(time_series), axis=0)
                    axs[i].plot(mean_values, label=f"Klasa {class_idx}")

            axs[i].set_title(f"Porównanie średnich dla współrzędnej {dimension_idx}")
            axs[i].set_xlabel("Czas")
            axs[i].set_ylabel("Średnia wartość")
            axs[i].legend()

        plt.tight_layout()
        plt.show()

        plt.tight_layout()
        plt.show()

    def run(self):
        self.plot_histogram()
        self.plot_all_stats_from_dict()
        self.plot_all_series_from_dict()
        self.plot_mean_comparison()

def generate_multiple_time_series(number_of_series, length, mean, std):
    return [np.random.normal(mean, std, length) for _ in range(number_of_series)]


time_series = {}
for i in range(8):
    for j in range(3):
        if (f"class_{i}", f"dimension_{j}") not in time_series:
            time_series[(f"class_{i}", f"dimension_{j}")] = []
        time_series[(f"class_{i}", f"dimension_{j}")].append(generate_multiple_time_series(40, 315, i, (j + 1) * 0.1))


plotter = Plotter(time_series)
plotter.run()

