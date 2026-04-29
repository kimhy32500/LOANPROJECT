import open_browser, time
from scenarios.login_scenario import login_scenario, logout_scenario
from scenarios.loan_scenario import loan_scenario, loan_scenario_return
from scenarios.loan_steps import (
    loan_scenario_select_job,
    loan_scenario_input_company,
    loan_scenario_input_business,
    loan_scenario_input_join_date,
    loan_scenario_input_business_date,
    loan_scenario_select_insurance,
    loan_scenario_input_income,
    loan_scenario_submit,
)
from assertions.loan_assertion import assert_loan_result


# ----------- 실행 ------------
driver = open_browser.open_browser()

if driver:

    if not login_scenario(driver, "admin", "1234"):
        print("❌ 로그인 실패: 테스트를 중단합니다.")
    else:
         # 직장인 케이스 - 연소득 2999 (실패)
        print("\n[시작] 직장인 / 공무원 시나리오")
        if loan_scenario(driver):
            loan_scenario_select_job(driver, "직장인 / 공무원")
            loan_scenario_input_company(driver, "루피")
            loan_scenario_input_join_date(driver)
            loan_scenario_input_income(driver, "2999")
            loan_scenario_submit(driver)
            assert_loan_result(driver, "직장인 / 공무원", expected_success=False)
            loan_scenario_return(driver)
        else:
            print("❌ 직장인 / 공무원 시나리오 진입 실패\n")

        # 개인사업자 케이스 - 연소득 3000 (성공)
        print("\n[시작] 개인사업자 시나리오")
        if loan_scenario(driver):
            loan_scenario_select_job(driver, "개인사업자")
            loan_scenario_input_business(driver, "루피")
            loan_scenario_input_business_date(driver)
            loan_scenario_input_income(driver, "3000")
            loan_scenario_submit(driver)
            assert_loan_result(driver, "개인사업자", expected_success=True)
            loan_scenario_return(driver)
        else:
            print("❌ 개인사업자 시나리오 진입 실패\n")

        # 프리랜서 케이스 - 연소득 3000 (성공)
        print("\n[시작] 프리랜서 시나리오")
        if loan_scenario(driver):
            loan_scenario_select_job(driver, "프리랜서")
            loan_scenario_select_insurance(driver, "지역 가입자")
            loan_scenario_input_income(driver, "3000")
            loan_scenario_submit(driver)
            assert_loan_result(driver, "프리랜서", expected_success=True)
            loan_scenario_return(driver)
        else:
            print("❌ 프리랜서 시나리오 진입 실패\n")
        
        # 무직 케이스 - 연소득 0 (실패)
        print("\n[시작] 무직 시나리오")
        if loan_scenario(driver):
            loan_scenario_select_job(driver, "무직")
            loan_scenario_select_insurance(driver, "피부양자")
            loan_scenario_input_income(driver, "0")
            loan_scenario_submit(driver)
            assert_loan_result(driver, "무직", expected_success=False)
            loan_scenario_return(driver)
        else:
            print("❌ 무직 시나리오 진입 실패\n")  
        
        logout_scenario(driver)
        print("로그아웃 : 테스트 완료")

time.sleep(5)
driver.quit()