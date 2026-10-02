import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
if os.path.exists("bedtime_screentime_sleep_debt.csv"):
    # The target from my model will be next_day_fatigue_score
    print("File Available")
    bssd_df = pd.read_csv("bedtime_screentime_sleep_debt.csv")
    print(bssd_df.isnull().sum())
    print(bssd_df.describe())
    scatter_data = bssd_df.drop(
        columns=["next_day_fatigue_score", "gender", "occupation_type", "chronotype", "primary_bedtime_app", "sleep_debt_category", "user_id"])
    scatter_data = np.array(scatter_data.columns, dtype=float)
    for column in scatter_data:
        print(type(column))
        plt.title("Scatterplot for next_day_fatigue_score against other features")
        plt.figure(figsize=(12, 12))
        sns.scatterplot(x=column, y=float(bssd_df["next_day_fatigue_score"]))
    plt.xlabel("Other Features")
    plt.ylabel("next_day_fatigue_score")
    plt.legend()
    plt.show()

else:
    print("File unavailable")
