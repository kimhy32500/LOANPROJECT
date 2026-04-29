import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def assert_loan_result(driver, job_name, expected_success=True):
    try:
        wait = WebDriverWait(driver, 15)

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '홈으로 이동')]")))
        
        time.sleep(1)

        retry_btns = driver.find_elements(By.XPATH, "//*[contains(text(), '정보 수정하여 재심사')]")
        is_retry_visible = any(btn.is_displayed() for btn in retry_btns)

        actual_result = not is_retry_visible

        if actual_result == expected_success:
            status = "승인" if actual_result else "거절"
            print(f"✅ [PASS] {job_name}: {status} 화면이 노출됨")
            return True
        else:
            expected_str = "승인" if expected_success else "거절"
            actual_str = "승인" if actual_result else "거절"
            print(f"❌ [FAIL] {job_name}: {actual_str} 화면이 노출됨")
            return False

    except Exception as e:
        print(f"❌ [SYSTEM ERROR] {job_name}: 검증 중 오류 발생 ({e})")
        return False