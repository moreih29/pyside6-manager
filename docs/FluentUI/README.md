# FluentUI 컴포넌트 라이브러리

FluentUI는 Qt/QML 기반의 모던하고 아름다운 사용자 인터페이스를 구축하기 위한 컴포넌트 라이브러리입니다. Microsoft의 Fluent Design System 디자인 언어를 기반으로 하며, 다양한 컴포넌트와 유틸리티를 제공합니다.

## 주요 특징

- 다크 모드와 라이트 모드 지원
- 반응형 디자인
- 풍부한 컴포넌트 세트
- 사용자 정의 가능한 테마
- 다국어 지원
- 접근성 기능

## 컴포넌트 개요

FluentUI는 다음과 같은 카테고리의 컴포넌트를 제공합니다:

### 1. [버튼 컴포넌트](./Buttons.md)

사용자의 액션을 촉진하는 다양한 스타일의 버튼:
- `FluButton`: 표준 버튼
- `FluFilledButton`: 채워진 강조 버튼
- `FluTextButton`: 텍스트 전용 버튼
- `FluIconButton`: 아이콘 전용 버튼
- `FluToggleButton`: 토글 상태를 가진 버튼
- `FluDropDownButton`: 메뉴가 있는 드롭다운 버튼
- `FluLoadingButton`: 로딩 상태를 표시할 수 있는 버튼
- `FluProgressButton`: 진행률을 표시할 수 있는 버튼

### 2. [입력 컴포넌트](./InputControls.md)

사용자로부터 데이터를 입력받는 컴포넌트:
- `FluTextBox`: 텍스트 입력
- `FluPasswordBox`: 비밀번호 입력
- `FluMultilineTextBox`: 여러 줄 텍스트 입력
- `FluComboBox`: 드롭다운 선택 상자
- `FluCheckBox`: 체크박스
- `FluRadioButton`: 라디오 버튼
- `FluSlider`: 슬라이더
- `FluColorPicker`: 색상 선택
- `FluDatePicker`: 날짜 선택
- `FluTimePicker`: 시간 선택
- `FluCalendarPicker`: 달력 선택
- `FluRatingControl`: 별점 평가

### 3. [레이아웃 컴포넌트](./LayoutControls.md)

UI 구조와 탐색을 위한 컴포넌트:
- `FluWindow`: 메인 창
- `FluPage`: 페이지
- `FluNavigationView`: 탐색 메뉴
- `FluTabView`: 탭 뷰
- `FluExpander`: 확장 가능한 패널
- `FluSplitView`: 분할 뷰
- `FluStaggeredLayout`: 계단식 레이아웃
- `FluFlipView`: 플립 뷰
- `FluBreadcrumbBar`: 경로 표시줄
- `FluPivot`: 피벗 탭
- `FluCarousel`: 이미지 캐러셀

### 4. [다이얼로그 및 알림 컴포넌트](./DialogsAndNotifications.md)

사용자에게 정보를 전달하거나 상호작용을 위한 컴포넌트:
- `FluContentDialog`: 내용 다이얼로그
- `FluInfoBar`: 정보/알림 바
- `FluSheet`: 바텀 시트
- `FluPopup`: 팝업 창
- `FluTooltip`: 툴팁
- `FluTour`: 사용자 가이드 투어
- `FluMenu`: 메뉴

### 5. [데이터 시각화 컴포넌트](./DataVisualization.md)

데이터를 시각적으로 표현하는 컴포넌트:
- `FluBadge`: 배지
- `FluProgressBar`: 진행 표시줄
- `FluProgressRing`: 진행 링
- `FluChart`: 차트
- `FluTimeline`: 타임라인
- `FluTableView`: 테이블 뷰
- `FluTreeView`: 트리 뷰
- `FluPagination`: 페이지네이션
- `FluStatusView`: 상태 표시
- `FluWatermark`: 워터마크

### 6. [유틸리티 및 도우미 컴포넌트](./UtilityComponents.md)

공통 기능과 유틸리티:
- `FluTheme`: 테마 관리
- `FluColors`: 색상 팔레트
- `FluIcon`: 아이콘 표시
- `FluText`: 텍스트 컴포넌트
- `FluTextStyle`: 텍스트 스타일
- `FluTools`: 유틸리티 함수
- `FluLoader`: 동적 컴포넌트 로딩
- `FluRemoteLoader`: 원격 QML 로딩
- `FluEventBus`: 이벤트 통신
- `FluImage`: 이미지 표시
- `FluAcrylic`: 반투명 효과
- `FluQRCode`: QR 코드 생성
- `FluFocusRectangle`: 포커스 표시
- `FluCopyableText`: 복사 가능 텍스트
- `FluShadow`: 그림자 효과
- `FluClip`: 내용 클리핑

### 7. [고급 사용 예제](./AdvancedExamples.md)

FluentUI를 활용한 복잡한 UI 패턴 및 시나리오:
- 네비게이션 뷰 레이아웃
- 응답형 레이아웃
- 테마 전환 애니메이션
- 데이터 바인딩 및 모델 사용
- 드래그 앤 드롭 기능

## 시작하기

### QML에서 FluentUI 사용하기

```qml
import QtQuick
import FluentUI

// Window 대신 FluWindow를 최상위 아이템으로 사용합니다.
FluWindow {
    width: 800
    height: 600
    visible: true
    title: "FluentUI 예제"
    
    FluText {
        anchors.centerIn: parent
        text: "FluentUI에 오신 것을 환영합니다!"
        font: FluTextStyle.Title
    }
}
```

### 테마 설정하기

```qml
import FluentUI

FluWindow {
    width: 800
    height: 600
    title: "테마 예제"
    
    Column {
        anchors.centerIn: parent
        spacing: 20
        
        FluText {
            text: "현재 테마: " + (FluTheme.dark ? "다크" : "라이트")
            font.pixelSize: 16
        }
        
        FluToggleSwitch {
            text: "다크 모드"
            checked: FluTheme.dark
            onClicked: {
                if(FluTheme.dark){
                    FluTheme.darkMode = FluThemeType.Light
                }else{
                    FluTheme.darkMode = FluThemeType.Dark
                }
            }
        }
        
        FluFilledButton {
            text: "시스템 테마 사용"
            onClicked: {
                FluTheme.darkMode = FluThemeType.System
            }
        }
    }
}
```

### Python에서 FluentUI 등록하기

```python
import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from FluentUI import FluentUI

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
context = engine.rootContext()

# FluentUI 유형 등록
FluentUI.registerTypes(engine)

qml_file = QUrl("main.qml")  # 메인 QML 파일 경로
engine.load(qml_file)

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
``` 