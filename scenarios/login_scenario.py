import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click_actions, input_actions, validation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_scenario(driver, user_id, user_pw):
    print("[시작] 정상 로그인 시나리오")
    click_actions.click_element(driver, "#btn_login", "로그인 버튼")
    input_actions.enter_text(driver, "#input_id", user_id, "ID 입력")
    input_actions.enter_text(driver, "#input_pw", user_pw, "PW 입력")
    click_actions.click_element(driver, "//*[text()='로그인 완료']", "로그인 완료")
    return validation.is_text_present(driver, "로그아웃", "로그인 완료")

def logout_scenario(driver):
    print("[시작] 로그아웃 및 팝업 제어")
    try:
        click_actions.click_element(driver, "#btn_logout", "로그아웃 클릭")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.dismiss()
        print("[성공] 로그아웃 취소")
        
        click_actions.click_element(driver, "#btn_logout", "로그아웃 재클릭")
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print("[성공] 로그아웃 처리 완료")
        return True
    except Exception as e:
        print(f"[실패] 로그아웃 중 에러: {e}")
        return False