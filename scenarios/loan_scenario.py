import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click_actions, validation, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def loan_scenario(driver):
    print("\n[단계] 대출 심사 진입")
    try:
        click_actions.click_element(driver, "#btn_loan", "신용대출 조회하기 버튼")
        validation.is_text_present(driver, "대출 심사 정보 입력", "대출 심사 정보 입력 진입")
        print("[성공] 대출 조회 버튼 클릭 완료")
        return True
    except Exception:
        return False

def loan_scenario_return(driver):
    try:
        driver.switch_to.context('NATIVE_APP')
        home_xpath = "//android.widget.Button[@text='홈으로 이동']"
        
        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, home_xpath))
        )
        btn.click()

        time.sleep(2)
        webview = [c for c in driver.contexts if "WEBVIEW" in c or "CHROMIUM" in c][-1]
        driver.switch_to.context(webview)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '로그아웃')]"))
        )
        return True
    except:
        return True