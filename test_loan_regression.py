import pytest
import time
import open_browser
from scenarios.login_scenario import login_scenario, logout_scenario
from scenarios.loan_scenario import loan_scenario, loan_scenario_return
from scenarios.loan_steps import * # 모든 스텝 임포트
from assertions.loan_assertion import assert_loan_result

# [Fixture] 테스트 시작 전 브라우저를 띄우고, 종료 후 닫아주는 장치
@pytest.fixture(scope="module")
def driver():
    _driver = open_browser.open_browser()
    yield _driver
    time.sleep(5)
    _driver.quit()

# [테스트 1] 로그인 테스트
def test_login(driver):
    success = login_scenario(driver, "admin", "1234")
    assert success is True, "❌ 로그인 실패: 이후 테스트를 진행할 수 없습니다."

# [테스트 2] 직장인 시나리오
def test_office_worker_loan(driver):
    assert loan_scenario(driver), "직장인 시나리오 진입 실패"
    loan_scenario_select_job(driver, "직장인 / 공무원")
    loan_scenario_input_company(driver, "루피")
    loan_scenario_input_join_date(driver)
    loan_scenario_input_income(driver, "2999")
    loan_scenario_submit(driver)
    # assert_loan_result 내부에 검증 로직이 True/False를 반환하도록 설계되어 있어야 함
    assert assert_loan_result(driver, "직장인 / 공무원", expected_success=False)
    loan_scenario_return(driver)

# [테스트 3] 개인사업자 시나리오
def test_business_owner_loan(driver):
    assert loan_scenario(driver), "개인사업자 시나리오 진입 실패"
    loan_scenario_select_job(driver, "개인사업자")
    loan_scenario_input_business(driver, "루피")
    loan_scenario_input_business_date(driver)
    loan_scenario_input_income(driver, "3000")
    loan_scenario_submit(driver)
    assert assert_loan_result(driver, "개인사업자", expected_success=True)
    loan_scenario_return(driver)

# [테스트 4] 프리랜서 시나리오
def test_freelancer_loan(driver):
    assert loan_scenario(driver), "프리랜서 시나리오 진입 실패"
    loan_scenario_select_job(driver, "프리랜서")
    loan_scenario_select_insurance(driver, "지역 가입자")
    loan_scenario_input_income(driver, "3000")
    loan_scenario_submit(driver)
    assert assert_loan_result(driver, "프리랜서", expected_success=True)
    loan_scenario_return(driver)

# [마지막] 로그아웃
def test_logout_and_finish(driver):
    logout_scenario(driver)
    print("로그아웃 : 테스트 완료")