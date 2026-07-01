import pandas as pd

# 1. 데이터 불러오기
tag_counts = pd.read_csv('tag_counts_results.csv')
tag_trends = pd.read_csv('tag_trends_results.csv')

# 2. Tag 컬럼 기준으로 병합
final_analysis = pd.merge(tag_counts, tag_trends, on='Tag')

# 3. 효율 지표 계산 (인기지표를 빈도수로 나누기)
final_analysis['Efficiency Index'] = final_analysis['popular index'] / final_analysis['Count']

# 4. 효율성 지표 기준 내림차순
final_analysis = final_analysis.sort_values(by='Efficiency Index', ascending=False)

# 5. 결과 저장
final_analysis.to_csv('tag_efficiency_analysis.csv', index=False, encoding='utf-8-sig')