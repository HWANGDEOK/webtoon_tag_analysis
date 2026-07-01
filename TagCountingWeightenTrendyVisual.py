import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

# 1. 수집한 데이터 불러오기
df = pd.read_csv('naver_webtoon_tags_weighted.csv')

# 불용어 제어
stopwords = ['지금핫한추천작', '요즘핫한추천작', '지금추천작','독자PICK', '2025 지상최대공모전', '2024 지상최대공모전', '2024 연재직행열차',
             '2025 연재직행열차','2023 지상최대공모전', '2024 최강자전', '2018 최강자전', '2020 지상최대공모전', '2022 지상최대공모전',
             '2021 지상최대공모전', '2022 최강자전', '2021 지상최대공모전', '2017 최강자전','레드아이스 스튜디오','명작','영화원작웹툰',
             '드라마&영화 원작웹툰', '블루스트링','슈퍼스트링','레드스트링']
df_filtered = df[~df['Tag'].isin(stopwords)]

# 2. 태그별 가중치 합산 후 내림차순
tag_trends = df_filtered.groupby('Tag')['Weight'].sum().sort_values(ascending=False).reset_index()
tag_trends = tag_trends.rename(columns={'Weight': 'popular index'})
tag_trends.to_csv('tag_trends_results.csv', index=False, encoding='utf-8-sig')

# 3. 결과 확인
# print("--- 가중치 반영 태그 트렌드 ---")
# print(tag_trends.head(36))


# 4. 시각화
plt.figure(figsize=(15, 7))
# 한글 깨짐 방지 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

sns.barplot(x='popular index', y='Tag', data=tag_trends.head(40), palette='muted',hue='Tag', legend=False)
plt.title('네이버 웹툰 태그 트렌드(Top 40)')
plt.xlabel('인기 지수')
plt.ylabel('태그')
plt.savefig('인기지수(막대그래프).png')
plt.show()


# # 1. 워드 클라우드 생성
# # tag_trends는 아까 만든 DataFrame (Tag, popular index 포함)
# word_counts = dict(zip(tag_trends['Tag'], tag_trends['popular index']))
#
# wc = WordCloud(font_path='malgun.ttf', # 한글 폰트 경로
#                background_color='white',
#                width=800, height=400).generate_from_frequencies(word_counts)
#
# plt.figure(figsize=(10, 5))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis('off')
# plt.savefig('인기지수(워드클라우드).png')
# plt.show()


# # 2. 트리맵 생성
# # 전체 데이터의 지수 합계 계산
# total_sum = tag_trends['popular index'].sum()
#
# # 상위 20개만 복사해서 새로운 컬럼(전체 대비 비율) 추가
# top20 = tag_trends.head(20).copy()
# top20['total_ratio'] = (top20['popular index'] / total_sum) * 100
#
# # 트리맵 생성
# fig = px.treemap(top20,
#                  path=['Tag'],
#                  values='popular index',
#                  title='네이버 웹툰 태그 인기지수 비중 (Top 20)')
#
# # 텍스트 템플릿 수정
# # %{customdata[0]}를 사용하여 미리 계산한 total_ratio를 불러옵니다.
# fig.update_traces(
#     customdata=top20[['total_ratio']], # 데이터를 트리맵에 전달
#     texttemplate="<b>%{label}</b><br>%{customdata[0]:.1f}%",
#     textinfo="label"
# )
#
# fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
# fig.show()
# fig.write_image("인기지수(트리맵).png")