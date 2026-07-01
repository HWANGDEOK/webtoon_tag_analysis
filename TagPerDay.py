import pandas as pd

# 1. 데이터 로드
df = pd.read_csv('naver_webtoon_tags_weighted.csv')

# 분석할 요일 리스트
days = ["월요웹툰", "화요웹툰", "수요웹툰", "목요웹툰", "금요웹툰", "토요웹툰", "일요웹툰"]

# 각 요일별 분석 결과를 담을 딕셔너리
day_reports = {}

for day in days:
    # 요일 필터링
    day_df = df[df['Day'] == day]

    #  해당 요일 분석
    # 인기 지수와 빈도 계산
    analysis = day_df.groupby('Tag').agg(
        popular_index=('Weight', 'sum'),
        count=('Tag', 'size')
    ).sort_values(by='popular_index', ascending=False).reset_index()

    # 해당 요일의 전체 대비 비중(%) 추가
    total_idx = analysis['popular_index'].sum()
    analysis['ratio(%)'] = (analysis['popular_index'] / total_idx) * 100

    # 딕셔너리에 결과 저장
    day_reports[day] = analysis

    # 파일 저장
    analysis.to_csv(f'분석_{day}.csv', index=False, encoding='utf-8-sig')

    print(f" {day} 분석 완료! (상위 태그: {analysis.iloc[0]['Tag']})")