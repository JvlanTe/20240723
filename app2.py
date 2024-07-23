import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(9, 4))

plt.plot(df["Date"], df["Hokkaido"], label="Hokkaido", color="y")
plt.plot(df["Date"], df["Gifu"], label="Gifu", color="b")
plt.plot(df["Date"], df["Okinawa"], label="Okinawa", color="g")
plt.plot(df["Date"], df["ALL"], label="ALL", color="r")

plt.title("全国・岐阜・沖縄・北海道コロナ感染者数")
plt.xlabel("日付")
plt.ylabel("感染者数")

plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.show()
