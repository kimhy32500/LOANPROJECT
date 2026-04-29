from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def is_text_present(driver, text, name):
    try:
        current_ctx = driver.current_context
        wait = WebDriverWait(driver, 7) # 입사월 이슈를 고려해 시간을 조금 늘렸습니다.
        
        xpath = f"//*[contains(text(), '{text}')]"
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        
        print(f"[검증 성공] '{name}' 노출")
        return True
    
    except TimeoutException:
        print(f"[검증 실패] '{name}' 문구가 7초 이내에 나타나지 않음 (텍스트: {text})")
        return False
    except Exception as e:
        print(f"[검증 에러] {name} 확인 중 예상치 못한 오류: {str(e).splitlines()[0]}")
        return False