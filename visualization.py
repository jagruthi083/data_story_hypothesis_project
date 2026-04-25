import pandas as pd # type: ignore
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

def plot_conversion_rates():
    data = pd.read_csv("data/ab_test_data.csv")
    data["conversion_rate"] = data["conversions"] / data["visitors"]

    plt.bar(data["group"], data["conversion_rate"])
    plt.title("Conversion Rate Comparison (A/B Test)")
    plt.xlabel("Group")
    plt.ylabel("Conversion Rate")

    plt.show()

if __name__ == "__main__":
    plot_conversion_rates()
