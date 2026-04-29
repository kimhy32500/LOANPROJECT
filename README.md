# 신용대출 심사 자동화 테스트 프로젝트
Appium과 Selenium을 활용한 하이브리드 앱 대출 시나리오 자동화 테스트 프로젝트입니다.

## 테스트 시연 (Demo)
<p align="center">
  <img src="images/Loan_TestAutomation.gif" width="600">
</p>

## 1. 주요 특징
##    ✅ POM (Page Object Model) 디자인 패턴 적용
###   유지보수: 페이지별(Login, Input, Result)로 객체를 분리하여 UI 변경 시 해당 페이지만 수정하면 되도록 설계했습니다.
###   가독성: 테스트 시나리오와 저수준의 액션(Click, Input) 코드를 분리하여 비즈니스 로직을 한눈에 파악할 수 있습니다.

##    ✅ 하이브리드 앱 컨텍스트 제어
###   Native & Webview 스위칭: 앱의 네이티브 버튼과 웹뷰 내부의 HTML 요소를 자유롭게 오가며 제어합니다.
###   유연한 탐색: XPath와 CSS Selector를 상황에 맞게 활용하여 정확하게 요소를 타겟팅합니다.

###   ✅ 예외 처리 및 검증 (Validation)
###   검증 로직: 각 단계별로 성공/실패 여부를 판단하는 Validation 모듈을 구축했습니다.
###   에러 로깅: 동작 실패 시 스크린샷을 자동 저장하여 디버깅 효율을 높였습니다.

## 2. 프로젝트 구조

```text
LOANPROJECT/ (최상위 폴더)
├── app/                  # [Target] 테스트 대상 웹사이트 소스
├── assertions/           # [Validation] 결과 판정 로직
│   └── loan_assertion.py
├── scenarios/            # [Scenario] 주요 테스트 시나리오 조각들
│   ├── loan_scenario.py
│   ├── loan_steps.py
│   └── login_scenario.py
├── images/               # [Doc] README용 GIF 파일 보관함
├── screenshots/          # [Log] 에러 발생 시 스크린샷 저장 폴더
├── click_actions.py      # [Util] 공통 클릭 액션
├── input_actions.py      # [Util] 공통 입력 액션
├── open_browser.py       # [Util] 드라이버 설정 및 실행
├── validation.py         # [Util] 요소 확인 및 검증 유틸
├── README.md             # 프로젝트 설명서
└── regression_main.py    # [Runner] 전체 시나리오 실행 메인 파일
```


## 3. 사전 준비 (Prerequisites)
    * **Python 3.12.3+**
    * **Appium Server** (v2.x 권장)
    * **Android Emulator** (API 30 이상 권장)
    * **ChromeDriver**: 에뮬레이터 내 Chrome 버전과 일치하는 드라이버

## 4. 설치 및 실행
```bash
# 저장소 클론
git clone `https://github.com/kimhy32500/LOANPROJECT.git`
cd LOANPROJECT

# 라이브러리 설치
pip install -r requirements.txt

# 테스트 실행
python regression_main.py

> ⚠️ **실행 전 주의사항**
> 1. **Appium Server**가 실행 중이어야 합니다. (기본 포트: 4723)
> 2. **Android Emulator**가 구동된 상태여야 합니다.
> 3. 에뮬레이터 내의 **Chrome 브라우저 버전**과 `webdriver-manager`가 관리하는 버전이 일치해야 합니다.