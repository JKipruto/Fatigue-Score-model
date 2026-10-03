import os
import pandas as pd
if os.path.exists("bedtime_screentime_sleep_debt.csv"):
  # The target from my model will be next_day_fatigue_score-
    print("File Available")
    bssd_df = pd.read_csv("bedtime_screentime_sleep_debt.csv")
    print(bssd_df.isnull().sum())
    print(bssd_df.dtype)
else:
    print("File unavailable")
