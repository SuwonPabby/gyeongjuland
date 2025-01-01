from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import os
import json
import slack_sdk


def send_discord_message(text):
    discord_url = os.environ.get("DISCORD_GJWORLD_URL")
    message = {"content": text}
    requests.post(discord_url, data=message)


def send_slack_message(text):
    slack_token = os.environ.get("SLACK_GJWORLD_TOKEN")
    client = slack_sdk.WebClient(token=slack_token)

    response = client.chat_postMessage(channel="경주월드-알람", text=text)


if __name__ == "__main__":
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

    queries = ["드라켄", "파에톤", "스콜"]
    state = ""

    for query in queries:
        if f"<h5>{query}" in driver.page_source:
            state += "1"
            with open("temp.txt", "w") as f:
                f.write(driver.page_source)
        else:
            state += "0"

    with open("/home/ec2-user/gyeongjuland/state.txt", "r") as f:
        previous_state = f.read()
    text = ""
    print(previous_state)

    for s, ps, att in zip(state, previous_state, queries):
        if s == "1" and ps == "0":
            text += f"🛑'{att}'(이)가 운행이 중지되었습니다!\n"
        elif s == "0" and ps == "1":
            text += f"🔵'{att}'(이)가 운행을 시작했습니다!\n"

    if text:
        text = text.strip()
        text += "\n\nhttps://www.gjw.co.kr/Contents/contents.php?cmsNo=DA0200"
        # send_discord_message(text)
        send_slack_message(text)
        print(state)
        print(text)

    with open("/home/ec2-user/gyeongjuland/state.txt", "w") as f:
        f.write(state)

    # 드라이버 종료
    driver.quit()
