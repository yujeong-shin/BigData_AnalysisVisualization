import pandas as pd
import matplotlib.pyplot as plt

# file import
DF = pd.read_csv('C:/Pet.csv')
# print(DF)

# delete rows with NaN
df = DF.dropna()
print(df)

# draw donut chart
# 반려동물 보유 연령 비율
labels = ['20s', '30s', '40s', 'Over 50s'] # 20대, 30대, 40대, 50대 이상
frequency = df['Tens_age'].value_counts()
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(frequency, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.legend(bbox_to_anchor=(0.9, 1.0), loc='upper left')
plt.tight_layout()
plt.show()