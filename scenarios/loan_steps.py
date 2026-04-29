import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click_actions, input_actions, validation, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def loan_scenario_select_job(driver, job_name):
    print(f"[진행] 직업 선택: {job_name}")
    try:
        click_actions.click_element(driver, "#job", "선택창") 
        driver.switch_to.context('NATIVE_APP')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//*[@text='{job_name}']"))).click()
        driver.switch_to.context([c for c in driver.contexts if "WEBVIEW" in c or "CHROMIUM" in c][-1])
        return True
    except Exception as e:
        print(f"[실패] 직업 선택 중 에러: {e}")
        if driver.context == 'NATIVE_APP': driver.switch_to.context('CHROMIUM')
        return False
    
def loan_scenario_input_company(driver, comp_name):
    print(f"[입력] 직장명: {comp_name}")
    input_actions.enter_text(driver, "#comp_name", comp_name, "직장명")
    click_actions.click_element(driver, "//label[contains(text(), '직장명')]", "포커스 해제")
    return True

def loan_scenario_input_business(driver, biz_name):
    print(f"[입력] 사업장명: {biz_name}")
    input_actions.enter_text(driver, "#biz_name", biz_name, "사업장명")
    click_actions.click_element(driver, "//label[contains(text(), '사업장')]", "포커스 해제")
    return True

def loan_scenario_input_join_date(driver):
    print("[진행] 입사월 설정 (Native)")
    try:
        driver.switch_to.context('NATIVE_APP')
        time.sleep(1)
        locators = ["//android.widget.Spinner", "//*[contains(@resource-id, 'spinner')]", "//android.widget.EditText"]
        spinner = None
        for xpath in locators:
            try:
                spinner = driver.find_element(By.XPATH, xpath)
                if spinner: break
            except: continue

        if not spinner: raise Exception("스피너를 찾을 수 없음")
        spinner.click()
        
        confirm = "//*[@text='설정' or @text='확인' or @resource-id='android:id/button1']"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, confirm))).click()
        return True
    except Exception as e:
        print(f"[실패] 입사월 설정 에러: {e}")
        return False
    finally:
        driver.switch_to.context([c for c in driver.contexts if 'WEBVIEW' in c or 'CHROMIUM' in c][-1])

def loan_scenario_input_business_date(driver):
    print("[진행] 개업일 설정 (Native)")
    try:
        driver.switch_to.context('NATIVE_APP')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.DatePicker")))
        click_actions.click_element(driver, "//android.widget.DatePicker", "날짜 선택")
        click_actions.click_element(driver, "//android.widget.Button[@resource-id='android:id/button1']", "확인 버튼")
        return True
    except Exception as e:
        print(f"[실패] 개업일 설정 에러: {e}")
        return False
    finally:
        driver.switch_to.context([c for c in driver.contexts if "CHROMIUM" in c or "WEBVIEW" in c][-1])

def loan_scenario_select_insurance(driver, health):
    print(f"[진행] 건강보험 선택: {health}")
    try:
        click_actions.click_element(driver, "#health_type", "선택창") 
        driver.switch_to.context('NATIVE_APP')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//*[@text='{health}']"))).click()
        return True
    except Exception as e:
        print(f"[실패] 보험 선택 에러: {e}")
        return False
    finally:
        driver.switch_to.context([c for c in driver.contexts if "CHROMIUM" in c or "WEBVIEW" in c][-1])

def loan_scenario_input_income(driver, income_amount):
    print(f"[입력] 연소득: {income_amount}")
    input_actions.enter_text(driver, "#income", str(income_amount), "연소득")
    try:
        driver.find_element(By.CSS_SELECTOR, "#income").send_keys(Keys.RETURN)
    except: pass
    return validation.is_text_present(driver, "심사 신청하기", "심사 신청하기 노출")

def loan_scenario_submit(driver):
    try:
        driver.switch_to.context('NATIVE_APP')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='심사 신청하기']"))
        ).click()

        time.sleep(3)

        webview = [c for c in driver.contexts if "WEBVIEW" in c or "CHROMIUM" in c][-1]
        driver.switch_to.context(webview)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '홈으로')]"))
        )
        return True
    except:
        return False