import pandas as pd

data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")

# #2-1 1)
results_list = []
cols = ['H', 'avg', 'HR', 'OBP']

for year in range(2015, 2019):
    for col in cols:
        selected_year = data[data['year'] == year]
        sorted_rows = selected_year.sort_values(by=col, ascending=False)
        result1 = sorted_rows[['batter_name', 'year', col]].head(10).reset_index(drop=True)
        result1.index += 1
        results_list.append(result1)
        print(result1)

print()

# #2-1 2)
positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']

for position in positions:
    cp_2018 = data[(data['cp'] == position) & (data['year'] == 2018)]
    war_max = cp_2018.loc[cp_2018['war'].idxmax()]
    result2 = war_max[['batter_name', 'war']]
    print(f"{position}의 최대 승리 기여 선수: {result2['batter_name']} (승리 기여도: {result2['war']})")

# #2-1 3)
cols = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']

max_corr = 0
max_corr_col = None

for col in cols:
    corr = data[col].corr(data['salary'])
    if abs(corr) > abs(max_corr):
        max_corr = corr
        max_corr_col = col

print(f"\nhighest correlation with salary is {max_corr_col}")