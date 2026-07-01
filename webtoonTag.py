import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pandas as pd

options = uc.ChromeOptions()
options.add_argument('--no-first-run')
options.add_argument('--no-service-authorisation')
options.add_argument('--password-store=basic')

# 수집 데이터 저장 리스트
webtoon_data_list = []

try:
    driver = uc.Chrome(options=options, version_main=146)

    driver.get("https://nid.naver.com/nidlogin.login")
    print("--------------------------------------------------")
    print("--- 로그인 대기 중 ---")
    print("--------------------------------------------------")
    input("준비완료 후 엔터 입력.")

    driver.get("https://comic.naver.com/webtoon")
    time.sleep(2)

    days = ["월요웹툰", "화요웹툰", "수요웹툰", "목요웹툰", "금요웹툰", "토요웹툰", "일요웹툰"]

    for day_name in days:
        print(f"\n--- {day_name} 수집 시작 ---")
        day_xpath = f"//h3[contains(text(), '{day_name}')]/following-sibling::ul"

        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, day_xpath)))

        link_selector = f"{day_xpath}//a[@class='Poster__link--sopnC']"
        links = driver.find_elements(By.XPATH, link_selector)
        total_in_day = len(links)

        for i in range(total_in_day):
            current_links = driver.find_elements(By.XPATH, link_selector)
            target = current_links[i]

            # 순위 기반 가중치 계산(높은 순위는 더 많은 가중치)
            weight = (total_in_day - i)

            try:
                title_el = target.find_element(By.XPATH, "./ancestor::li//span[@class='ContentTitle__title--e3qXt']")
                webtoon_title = title_el.text
            except:
                webtoon_title = "제목 없음"

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            time.sleep(random.uniform(1.0, 1.5))
            target.click()

            # 상세 페이지 태그 수집 및 정제
            tag_selector = "a.TagGroup__tag--xu0OH"
            refined_tags = []
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, tag_selector)))
                tag_elements = driver.find_elements(By.CSS_SELECTOR, tag_selector)

                # '#'제거, 양쪽 공백 제거, 빈 값 제외
                for tag_el in tag_elements:
                    raw_tag = tag_el.text.strip().replace('#', '')
                    if raw_tag:  # 내용이 있는 경우만 추가
                        refined_tags.append(raw_tag)
            except:
                pass  # 태그가 없는 경우 빈 리스트 유지

            # 데이터 리스트에 추가
            if refined_tags:
                for t in refined_tags:
                    webtoon_data_list.append({
                        'Day': day_name,
                        'Title': webtoon_title,
                        'Rank': i + 1,
                        'Weight': weight,
                        'Tag': t
                    })

            print(f"[{i + 1}/{total_in_day}] {webtoon_title} | 정제된 태그: {', '.join(refined_tags)}")

            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, day_xpath)))
            time.sleep(random.uniform(0.5, 1.0))

    # 수집 완료 후 csv로 저장
    if webtoon_data_list:
        df = pd.DataFrame(webtoon_data_list)
        df.to_csv('naver_webtoon_tags_weighted.csv', index=False, encoding='utf-8-sig')
        print("\n--------------------------------------------------")
        print(f"수집 끝. 총 {len(df)}개의 태그 저장.")
        print("--------------------------------------------------")

except Exception as e:
    print(f"\n오류 발생: {e}")

finally:
    driver.quit()