from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def click_element(driver, locator, element_name):
    try:
        # 현재 컨텍스트를 로그에 포함하여 위치 파악 용이하게 개선
        current_ctx = driver.current_context
        by_type = By.XPATH if locator.startswith("//") else By.CSS_SELECTOR
        
        print(f"[시도] {element_name} 클릭")
        
        wait = WebDriverWait(driver, 10)
        btn = wait.until(EC.element_to_be_clickable((by_type, locator)))
        btn.click()

        print(f"[성공] {element_name} 클릭 완료")
        return True
    
    except Exception as e:
        print(f"[실패] {element_name} 클릭 에러 발생!")
        print(f"- 위치: {locator}")
        print(f"- 상세 정보: {str(e).splitlines()[0]}") # 첫 줄만 출력하여 가독성 확보
        driver.save_screenshot(f"./screenshots/fail_click_{element_name}.png")
        return False