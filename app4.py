import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

# 特定の日付に対応するデータのフィルタリングをする。
date = "2021/5/10"

# df_with_Dateは、dfの中のdfの中のDateと変数dateと一致するよ的な？
df_with_Date = df[df["Date"] == date]

# if、df_with_dateの中身が空なら、下記の文章を表示するよ
if df_with_Date.empty:
    print(f"No data available for the date: {date}")
# そうでないなら、DateとALL列を削除するよ
# ilocは最初の行を取得するためのもの
else:
    date_data = df_with_Date.drop(columns=["Date", "ALL"]).iloc[0]

    # 各都道府県の数値順に並び変える
    date_data_sorted = date_data.sort_values(ascending=True)
    print(date_data_sorted)

    # 特定の部分だけ色を変えるコード 岩手じゃないなら水色にするよ
colors = ["red" if prefecture == "Iwate" else "skyblue" for prefecture in date_data_sorted.index]

plt.figure(figsize=(12, 8))
# これでバーグラフを作成する(barhとbarがあるみたい)
# 最後にグラフ作成段階で先ほど作成したcolorsをcolorにあてはめないといけない ※注意
plt.bar(date_data_sorted.index, date_data_sorted.values, color=colors)
plt.xlabel("感染者数")
# fを使って変数と一緒に使うことができる
plt.title(f"都道府県ごとの感染者数 {date}")
plt.xticks(rotation=90)
plt.show()
