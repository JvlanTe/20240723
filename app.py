import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# dataflameを使うときの一番最初のやつ、pandasでread_csvして、どのcsvを使うか指定して、encording=を指定する）
df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

# "Date"列を日付型に変換する？　下の日付が月ごとになった
df["Date"] = pd.to_datetime(df["Date"])

# プロットのサイズの設定・幅8インチ、高さ3インチ
plt.figure(figsize=(8, 3))

# plt.plotでグラフを作成する この場合DateとIwate列を使用している
# dfの次に書かれるDateなどの文字は、大文字小文字寸分違わずcsvに書いてる通りのそれを入力する
plt.plot(df["Date"], df["Iwate"], label="Iwate", color="y")
plt.plot(df["Date"], df["Tokyo"], label="Tokyo", color="b")


plt.title("岩手・東京コロナ感染者数")
# x軸のラベル
plt.xlabel("日付")
# y軸のラベル
plt.ylabel("感染者数")

# グリッド出してくれる
plt.grid(True)

#
plt.xticks(rotation=45)

# これがないときれいにならないらしい
plt.legend()

# これがないと表示できない
plt.show()
