import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

# 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set_context("talk")
plt.figure(figsize=(15, 10))


# 1. 데이터 불러오기
df_analysis = pd.read_csv('tag_efficiency_analysis.csv')

# 2. 빈도수 100 이하, 인기지수 6000 이하
df_focused = df_analysis[(df_analysis['Count'] <= 100) &
                         (df_analysis['popular index'] <= 6000) &
                         (df_analysis['Efficiency Index'] >= 30)].copy()

# 3. 산점도 그리기
scatter = sns.scatterplot(
    data=df_focused,
    x='Count',
    y='popular index',
    size='Efficiency Index',
    hue='Efficiency Index',
    sizes=(100, 1000),
    palette='coolwarm',
    alpha=0.6,
    edgecolor='gray'
)

# 4. 텍스트 라벨 추가 (상위 50개 표시)
texts = []
top_n = 50
for i in range(min(len(df_focused), top_n)):
    texts.append(plt.text(
        df_focused.iloc[i]['Count'],
        df_focused.iloc[i]['popular index'],
        df_focused.iloc[i]['Tag'],
        fontsize=11,
        fontweight='bold'
    ))

# 5. 겹칠 경우 텍스트로 인지
adjust_text(
    texts,
    arrowprops=dict(arrowstyle='->', color='red', lw=0.5),
    expand_points=(1.5, 1.5),
    expand_text=(1.2, 1.2)
)

# 6. 그래프 장식
plt.title('지표 종합 산점도', fontsize=18, pad=20)
plt.xlabel('빈도수', fontsize=14)
plt.ylabel('인기지표', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Efficiency Index')

plt.tight_layout()
plt.savefig('tag_total_chart.png', dpi=300)
plt.show()