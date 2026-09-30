import os
import pandas as pd
if os.path.exists("bedtime_screentime_sleep_debt.csv"):
    print("File Available")
    df = pd.read_csv("bedtime_screentime_sleep_debt.csv")
    print(df.isnull().sum())
else:
    print("File unavailable")
