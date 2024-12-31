from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome 옵션 설정
options = Options()
options.add_argument("--headless")  # GUI 없이 실행
options.add_argument("--disable-gpu")  # GPU 비활성화
options.add_argument("--no-sandbox")  # 보안 관련 설정
options.add_argument("--disable-dev-shm-usage")  # 메모리 사용량 최소화

# ChromeDriver 경로 설정
# service = Service("/usr/bin/chromedriver")  # chromedriver의 경로

# WebDriver 생성
driver = webdriver.Chrome(options=options)

# 동적 웹사이트로 이동
url = "https://www.gjw.co.kr/Contents/contents.php?cmsNo=DA0200"
driver.get(url)

# 페이지가 완전히 로드되기를 기다리는 코드 (Optional)
driver.implicitly_wait(10)  # 최대 10초 대기

# 페이지 소스에서 특정 문구 검색
target_text = "드라켄"  # 확인하려는 문구
if target_text in driver.page_source:
    print(f"'{target_text}' 문구가 페이지에 있습니다.")
else:
    print(f"'{target_text}' 문구를 찾을 수 없습니다.")

# 드라이버 종료
driver.quit()
