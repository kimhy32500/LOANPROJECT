from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enter_text(driver, locator, text, name):
    try:
        current_ctx = driver.current_context
        by_type = By.XPATH if locator.startswith("//") else By.CSS_SELECTOR
        wait = WebDriverWait(driver, 10)
        
        # 요소 대기
        field = wait.until(EC.element_to_be_clickable((by_type, locator)))
        
        # 조작 단계 세분화
        field.click() 
        field.clear()
        field.send_keys(text)
        
        print(f"[성공] {name} 입력 완료 (값: {text})")
        return True
    except Exception as e:
        print(f"[실패] {name} 입력 단계 중단: {str(e).splitlines()[0]}")
        driver.save_screenshot(f"./screenshots/fail_input_{name}.png")
        return False