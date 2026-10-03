import os
import pandas as pd
import duckdb as db
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns

ohecoder = OneHotEncoder()
conn = db.connect("My_database.duckdb")
if os.path.exists("bedtime_screentime_sleep_debt.csv"):
  # The target from my model will be next_day_fatigue_score-
    print("File Available")
    bssd_df = conn.sql("""select age,gender,occupation_type,chronotype,bedtime_phone_minutes,primary_bedtime_app,
    screen_brightness_pct,blue_light_filter_active,caffeine_post_5pm_mg,physical_activity_min,sleep_latency_min,total_sleep_hours,deep_sleep_pct,rem_sleep_pct,
    morning_alarm_snoozes,next_day_fatigue_score,sleep_debt_category from 'bedtime_screentime_sleep_debt.csv'""").df()
    non_binary_sex = conn.sql(
        """select * from'bedtime_screentime_sleep_debt.csv' where gender not in ('Male','Female')""").df()

    print(bssd_df.isnull().sum())
    print(non_binary_sex.count())
    print(bssd_df.isna().sum())
    print(bssd_df.dtypes)

    numeric_columns = ["age", "bedtime_phone_minutes", "screen_brightness_pct", "blue_light_filter_active",
                       "caffeine_post_5pm_mg", "physical_activity_min", "sleep_latency_min", "total_sleep_hours", "deep_sleep_pct", "rem_sleep_pct", "morning_alarm_snoozes"]

    plt.figure(figsize=(12, 12))
    col1 = numeric_columns[0]
    for col in numeric_columns:
        plt.title(f"Scatterplot of next day fatigue score against  {col}")
        sns.scatterplot(x=col, y="next_day_fatigue_score", data=bssd_df)
        plt.show()


else:
    print("File unavailable")
