import pandas as pd
import os

from data_funcs import min_lst, max_lst, mean_lst, stddev_lst, median_lst

regular_file = './data/Batting.csv'
postseason_file = './data/BattingPost.csv'

regular_df = pd.read_csv(regular_file) # 101,332 entries
postseason_df = pd.read_csv(postseason_file)

print(regular_df.head())

output_df = {
    'stat': [col_name for col_name, col_data in regular_df.items()]
}

func_lst = [min_lst, max_lst, mean_lst, stddev_lst, median_lst]

def cleanse_lst(lst):
    return [x for x in lst if x != "NaN"]

non_stat_cols = {"playerID", "yearID", "round", "teamID", "lgID"}

for f in func_lst:
    stat_calcs = ["N/A" if col_name in non_stat_cols else f(cleanse_lst(col_data))
                  for col_name, col_data in regular_df.items()]
    output_df[f.__name__[0:-4]] = stat_calcs

# after this point output_df : dict -> df
output_path = './output/BattingAggregate.csv'
dir_name = os.path.dirname(output_path)

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

output_df = pd.DataFrame(output_df)
output_df.to_csv(output_path, index=False)
    

    