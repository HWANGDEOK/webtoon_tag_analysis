import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('naver_webtoon_tags_weighted.csv')

# 불용어 처리
stopwords = ['지금핫한추천작', '요즘핫한추천작', '지금추천작','독자PICK', '2025 지상최대공모전', '2024 지상최대공모전', '2024 연재직행열차',
             '2025 연재직행열차','2023 지상최대공모전', '2024 최강자전', '2018 최강자전', '2020 지상최대공모전', '2022 지상최대공모전',
             '2021 지상최대공모전', '2022 최강자전', '2021 지상최대공모전', '2017 최강자전','레드아이스 스튜디오','명작','영화원작웹툰',
             '드라마&영화 원작웹툰', '블루스트링','슈퍼스트링','레드스트링']
df_filtered = df[~df['Tag'].isin(stopwords)]

# 1. 태그 빈도수 계산
tag_counts = df_filtered['Tag'].value_counts().reset_index()
tag_counts.columns = ['Tag', 'Count']

tag_counts.to_csv('tag_counts_results.csv', index=False, encoding='utf-8-sig')

# 2. 그래프 설정
plt.figure(figsize=(15, 8))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 3. 상위 40개 태그 시각화
sns.barplot(
    x='Count',
    y='Tag',
    data=tag_counts.head(40),
    palette='flare', # 가중치 그래프와 색 구분
    hue='Tag',
    legend=False
)

plt.title('네이버 웹툰 태그 빈도수')
plt.xlabel('사용된 횟수 (개)')
plt.ylabel('태그')

plt.savefig('태그_빈도수_막대그래프.png', dpi=300, bbox_inches='tight')
plt.show()


