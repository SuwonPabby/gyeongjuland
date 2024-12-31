from selenium import webdriver
from selenium.webdriver.common.by import By

# 브라우저 드라이버 실행 (ChromeDriver 예제)
driver = webdriver.Chrome()  # ChromeDriver 경로를 지정할 수도 있음

# 동적 웹사이트로 이동
url = "https://www.gjw.co.kr/Contents/contents.php?cmsNo=DA0200"
driver.get(url)

# 페이지가 완전히 로드되기를 기다리는 코드 (Optional)
driver.implicitly_wait(10)  # 최대 10초 대기

# 페이지 소스에서 특정 문구 검색
target_text = "스콜"  # 확인하려는 문구
if target_text in driver.page_source:
    print(f"'{target_text}' 문구가 페이지에 있습니다.")
else:
    print(f"'{target_text}' 문구를 찾을 수 없습니다.")

# 드라이버 종료
driver.quit()
