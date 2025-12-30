import pandas as pd

regular_file = './data/Batting.csv'
postseason_file = './data/BattingPost.csv'

regular_df = pd.read_csv(regular_file) # 101,332 entries
postseason_df = pd.read_csv(postseason_file)

print(regular_df.head())

non_stat_cols = {"playerID", "yearID", "round", "teamID", "lgID"}
for col_name, col_data in regular_df.items():
    if col_name in non_stat_cols:
        continue

    sum, cnt = 0, 0
    for x in col_data:
        try:
            sum += x
            cnt += 1
        except Exception:
            print(f"{x} is not a number")

    # print(col_name, sum([0 if x == "NaN" else x for x in col_data]))