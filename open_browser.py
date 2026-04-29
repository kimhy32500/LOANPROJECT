from appium import webdriver
from appium.options.common.base import AppiumOptions

def open_browser():
    try:
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "browserName": "Chrome",
            "appium:deviceName": "emulator-5554",
            "appium:noReset": False,
            "appium:fullReset": False,
            "appium:newCommandTimeout": 300,        # 세션 유지 시간 연장
            "appium:adbExecTimeout": 60000,         # ADB 명령 대기 시간 연장
            "appium:uiautomator2ServerLaunchTimeout": 60000, # 서버 실행 대기 연장
            "appium:systemPort": 8200,              # 포트 고정 (충돌 방지)
            "appium:ensureWebviewsHavePages": True  # 웹뷰 안정성 강화
        })

        print("[정보] Appium 서버 연결 시도 중...")
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        
        target_url = "http://10.0.2.2:5500/app/index.html"
        driver.get(target_url)
        print(f"[성공] 브라우저 실행 및 URL 이동 완료: {target_url}")
        return driver
    
    except Exception as e:
        print("\n" + "!" * 60)
        # 상단에 에러의 성격(초기화 실패)을 명확히 명시
        print(" [CRITICAL ERROR] 드라이버 초기화 실패 ".center(60, " "))
        print("!" * 60)
        
        # 실제 시스템 에러 메시지 출력
        print(f"\n▶ 상세 에러 내용 (System Message):")
        print(f"   {e}")
        
        print("\n" + "=" * 60)
        print(" 🔍 환경 체크리스트 (실행 전 확인 필수)")
        print("=" * 60)
        print(" 1. Appium Server  : 연결 가능 상태인가? (http://127.0.0.1:4723)")
        print(" 2. Emulator       : 'emulator-5554'가 켜져 있는가?")
        print(" 3. Chrome Version : 에뮬레이터 크롬과 드라이버 버전이 맞는가?")
        print(" 4. Target URL     : 테스트 대상 웹 서버가 구동 중인가?")
        print("-" * 60)
        print("! 위 항목을 확인하신 후 다시 실행해 주세요.\n")
        
        return None