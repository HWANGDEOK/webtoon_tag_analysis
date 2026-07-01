import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 불러오기
df_analysis = pd.read_csv('tag_efficiency_analysis.csv')

# 2. 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 3. 상위 50개 태그 추출
top_efficiency = df_analysis.head(50)
print(len(df_analysis))

# 4. 시각화 설정
plt.figure(figsize=(12, 8))
sns.barplot(
    data=top_efficiency,
    x='Efficiency Index',
    y='Tag',
    palette='viridis',
    hue = 'Tag',
    legend = False
)

plt.title('웹툰 태그별 효율성 지표', fontsize=16, pad=20)
plt.xlabel('효율성', fontsize=12)
plt.ylabel('태그', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)

# 6. 결과 출력 및 저장
plt.tight_layout()
plt.savefig('tag_efficiency_chart.png', dpi=300)
plt.show()