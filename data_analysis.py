import pandas as pd # type: ignore

def load_data():
    data = pd.read_csv("data/ab_test_data.csv")
    return data

def calculate_conversion_rates(data):
    data["conversion_rate"] = data["conversions"] / data["visitors"]
    return data

def display_summary(data):
    print("\nA/B Test Summary")
    print(data)

if __name__ == "__main__":
    data = load_data()
    data = calculate_conversion_rates(data)
    display_summary(data)
