import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic' # 윈도우 기준
plt.rcParams['axes.unicode_minus'] = False

# 1. 불러오고 싶은 요일 입력
target_day = "일요웹툰" # [월요웹툰, 화요웹툰, 수요웹툰, 목요웹툰, 금요웹툰, 토요웹툰, 일요웹툰] 원하는 거 골라 넣기
file_name = f'분석_{target_day}.csv'

day_data = pd.read_csv(file_name)
# 불용어 제어
stopwords = ['지금핫한추천작', '요즘핫한추천작', '지금추천작','독자PICK', '2025 지상최대공모전', '2024 지상최대공모전', '2024 연재직행열차',
             '2025 연재직행열차','2023 지상최대공모전', '2024 최강자전', '2018 최강자전', '2020 지상최대공모전', '2022 지상최대공모전',
             '2021 지상최대공모전', '2022 최강자전', '2021 지상최대공모전', '2017 최강자전','레드아이스 스튜디오']
df_filtered = day_data[~day_data['Tag'].isin(stopwords)]


# 2. 시각화 (인기지수, 빈도 같이)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# [좌측: 인기 지수 시각화]
sns.barplot(x='popular_index', y='Tag', data=df_filtered.head(40), ax=ax1, hue='Tag', legend=False, palette='coolwarm')
ax1.set_title(f'[{target_day}] 인기 지수 TOP 40', fontsize=15)
ax1.set_xlabel('인기 지수')
ax1.set_ylabel('태그', fontsize=12)
ax1.set_xlim(0, 2700)

# [우측: 순수 빈도 시각화]
# 빈도(count) 기준으로 다시 정렬해서 보여주면 더 정확합니다.
sns.barplot(x='count', y='Tag', data=df_filtered.iloc[30:71].sort_values('count', ascending=False), ax=ax2, hue='Tag', legend=False, palette='viridis')
ax2.set_title(f'[{target_day}] 순수 빈도 TOP 40', fontsize=15)
ax2.set_xlabel('사용 횟수 (개)')
ax2.set_ylabel('')
ax2.set_xlim(0, 50)

plt.tight_layout()

# 3. 이미지 저장
plt.savefig(f'시각화_{target_day}.png', dpi=300)
plt.show()