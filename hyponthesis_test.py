import pandas as pd # pyright: ignore[reportMissingModuleSource]
import scipy.stats # pyright: ignore[reportMissingImports]

def run_ttest():
    data = pd.read_csv("data/ab_test_data.csv")

    rate_A = data.loc[data['group'] == 'A', 'conversions'].values[0] / \
             data.loc[data['group'] == 'A', 'visitors'].values[0]

    rate_B = data.loc[data['group'] == 'B', 'conversions'].values[0] / \
             data.loc[data['group'] == 'B', 'visitors'].values[0]

    t_stat, p_value = scipy.stats.ttest_ind([rate_A], [rate_B])

    print("\nHypothesis Testing Results")
    print("Conversion Rate A:", rate_A)
    print("Conversion Rate B:", rate_B)
    print("T-statistic:", t_stat)
    print("P-value:", p_value)

    if p_value < 0.05:
        print("\nResult: Reject Null Hypothesis")
        print("New website significantly improves conversions.")
    else:
        print("\nResult: Fail to Reject Null Hypothesis")
        print("No statistically significant improvement.")

if __name__ == "__main__":
    run_ttest()
