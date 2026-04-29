import pytest
import json
import os
import open_browser
from scenarios.login_scenario import login_scenario, logout_scenario
from scenarios.loan_scenario import loan_scenario, loan_scenario_return
from scenarios.loan_steps import *
from assertions.loan_assertion import assert_loan_result

# 1. JSON 데이터를 읽어오는 함수
def load_test_data():
    file_path = os.path.join("data", "test_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# [Fixture] 브라우저 관리
@pytest.fixture(scope="module")
def driver():
    _driver = open_browser.open_browser()
    # 공통 로그인 (딱 한 번만 수행)
    if not login_scenario(_driver, "admin", "1234"):
        pytest.exit("❌ 로그인 실패로 전체 테스트를 중단합니다.")
    yield _driver
    _driver.quit()

# 2. 데이터 기반 테스트 (Data-Driven Test)
# JSON에 있는 케이스 개수만큼 이 함수가 자동으로 반복 실행됩니다.
@pytest.mark.parametrize("data", load_test_data())
def test_loan_all_cases(driver, data):
    print(f"\n[시작] {data['case_name']}")
    
    # 시나리오 진입
    assert loan_scenario(driver), f"{data['case_name']} 진입 실패"
    
    # 직업 선택
    loan_scenario_select_job(driver, data['job_type'])
    
    # 직업별 분기 처리 (데이터에 값이 있을 때만 실행)
    if "company" in data and data['job_type'] == "직장인 / 공무원":
        loan_scenario_input_company(driver, data['company'])
        loan_scenario_input_join_date(driver)
    elif "company" in data and data['job_type'] == "개인사업자":
        loan_scenario_input_business(driver, data['company'])
        loan_scenario_input_business_date(driver)
    elif "insurance" in data:
        loan_scenario_select_insurance(driver, data['insurance'])
    
    # 공통 입력 및 제출
    loan_scenario_input_income(driver, data['income'])
    loan_scenario_submit(driver)
    
    # 결과 검증
    assert assert_loan_result(driver, data['job_type'], data['expected_success'])
    
    # 리턴 (다음 테스트를 위해 홈으로)
    loan_scenario_return(driver)

# [마지막] 로그아웃 (모든 케이스 종료 후)
def test_cleanup(driver):
    logout_scenario(driver)