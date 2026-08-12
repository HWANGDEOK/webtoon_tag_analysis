# 🔍 네이버 웹툰 트렌드 분석 및 인사이트 도출

- 네이버 웹툰의 인기 태그 데이터를 분석하여 최신 트렌드를 도출하고, 신입 작가를 위한 최적의 작품 키워드 인사이트를 제공한 프로젝트

[블로그 내용](https://wadow00.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%9B%B9%ED%88%B0-%ED%83%9C%EA%B7%B8-%EB%B6%84%EC%84%9D%EC%9D%84-%ED%86%B5%ED%95%9C-%ED%8A%B8%EB%A0%8C%EB%93%9C-%EB%B6%84%EC%84%9D-%EB%B0%8F-%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8)

## 📌 1. 프로젝트 개요

- **주제**: 네이버 인기 웹툰 태그 데이터를 기반으로 트렌드 분석
- **목적**: 소재 선정이 고민인 신입 웹툰 작가에게 데이터 기반 장르 추천


## 🛠️ 2. 기술 스택

- **Language**: Python(3.14.3)
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Selenium, Undetected-Chromeriver


## 📝 3. 데이터 전처리

- **텍스트 정제** : 태그 텍스트에서 특수문자(#) 및 공백을 제거하고 통계 분석에 적합한 데이터 형태로 변환.
- **불용어 필터링** : 웹툰의 속성과는 거리가 멀다고 생각하는 태그는 불용어로 직접 제어하여 필터링.
- **파생변수 생성** :
    - 트렌드를 파악하기 위해 태그 빈도수만 계산하지 않고, 요일별 상위권 작품의 태그에는 높은 가중치를 차등 부여하여 '**인지지수**' 파생변수 생성.
    - 블루오션을 파악하기 위해 빈도에 비해 인기지수가 높은 태그를 찾기 위해 '**효율**' 파생변수 생성.
 


## 📈 4. 분석 결과
<img width="450" height="225" alt="Image" src="https://github.com/user-attachments/assets/13a1f029-472d-4296-bea6-ae53aac37f3d" />
<img width="420" height="300" alt="Image" src="https://github.com/user-attachments/assets/7056ca67-b6bf-45e1-a455-42567203a5e7" />
<img width="900" height="600" alt="Image" src="https://github.com/user-attachments/assets/b2216ae4-8105-47a2-bc0d-4dd485a65ed6" />
<br>
**판무(판타지무협)** 이라는 장르적 기반을 확립하는 것을 추천하며, 근본적으로 무협이기에 인지지수가 높게 나타난 **성장물**의 특징 또한 포함하는 것을 추천한다.<br>
하지만 장르적 기반이 아닌 부가적인 특징은 개인이 추구하는 방향에 맞게 자유로이 설정하는 것이 개인의 색깔을 나타내는 것에 도움을 될 것으로 생각된다.
