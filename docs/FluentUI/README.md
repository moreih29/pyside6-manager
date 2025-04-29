# Fluent UI 컴포넌트 라이브러리

Fluent UI는 Qt Quick(QML)을 위한 Microsoft Fluent Design 시스템 기반의 UI 컴포넌트 라이브러리입니다. 데스크톱 애플리케이션을 위한 풍부하고 현대적인 인터페이스를 쉽게 구축할 수 있도록 다양한 컨트롤과 스타일을 제공합니다.

## 시작하기
Fluent UI를 사용하여 애플리케이션 개발을 시작하는 기본적인 단계입니다.

### 설치 가이드

pyside6-manager에 기본적으로 포함되어 있습니다.
```bash
pip install pyside6-manager 
```

### 초기 앱 생성

#### 1. QML 초기화 (main.qml)

```qml
import QtQuick 2.15
import QtQuick.Layouts 1.15
import FluentUI 1.0

FluWindow {
    id: window
    title: "My FluentUI App"
    width: 1000
    height: 668
    minimumWidth: 400
    minimumHeight: 300

    ColumnLayout {
        anchors.centerIn: parent
        width: parent.width * 0.6
        spacing: 15 

        FluText {
            Layout.alignment: Qt.AlignHCenter
            text: qsTr("Welcome to FluentUI!")
            font: FluTextStyle.TitleLarge
            horizontalAlignment: Text.AlignHCenter
        }

        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 15

            FluTextBox {
                id: nameInput
                placeholderText: qsTr("Enter your name")
            }

            FluButton {
                Layout.alignment: Qt.AlignHCenter
                text: qsTr("Send")
                onClicked: {
                    var inputText = nameInput.text.trim()
                    if (inputText) {
                        window.showSuccess(qsTr("Hello, %1!").arg(inputText), 3000)
                    } else {
                        window.showWarning(qsTr("Please enter your name."), 3000)
                    }
                }
            }
        }
    }
}
```

#### 2. Python 초기화 (main.py)

```python
import sys
from pathlib import Path

from pyside6_manager.qml.FluentUI import QFluentGuiApplication

ROOT = Path(__file__).parent.resolve()

app = QFluentGuiApplication(sys.argv, application_display_name="FluentUI App")
app.run(ROOT / "main.qml", base_path=ROOT)
```



## 컴포넌트

Fluent UI 컴포넌트는 기능별로 분류되어 있습니다. 각 링크를 클릭하면 해당 컴포넌트의 상세 설명을 확인할 수 있습니다.

### 레이아웃 (Layout)

*   [Layouts](./Layouts.md): 기본적인 레이아웃 컨테이너 및 유틸리티.
*   [GroupBox](./GroupBox.md): 콘텐츠를 그룹화하는 컨테이너.
*   [Expander](./Expander.md): 확장 및 축소가 가능한 콘텐츠 섹션.
*   [Frameless](./Frameless.md): 프레임 없는 창 관련 기능 (주로 내부 사용).

### 네비게이션 (Navigation)

*   [NavigationView](./NavigationView.md): 앱의 주요 네비게이션 구조 제공.
*   [BreadcrumbBar](./BreadcrumbBar.md): 현재 위치 경로 표시.
*   [Pivot](./Pivot.md): 콘텐츠 섹션 간 전환 탭.
*   [TabView](./TabView.md): 탭 기반 인터페이스.
*   [Pagination](./Pagination.md): 페이지 번호 기반 네비게이션.

### 입력 (Inputs)

*   [Buttons](./Buttons.md): 다양한 형태의 버튼.
*   [CheckBox](./CheckBox.md): 체크박스.
*   [ComboBox](./ComboBox.md): 드롭다운 목록 선택.
*   [RadioButton](./RadioButton.md): 라디오 버튼 그룹.
*   [Slider](./Slider.md): 값 범위 선택 슬라이더.
*   [ToggleSwitch](./ToggleSwitch.md): 켜기/끄기 스위치.
*   [TimePicker](./TimePicker.md): 시간 선택.
*   [DatePicker](./DatePicker.md): 날짜 선택.
*   [CalendarPicker](./CalendarPicker.md): 달력 형태 날짜 선택.
*   [ColorPicker](./ColorPicker.md): 색상 선택.
*   [RatingControl](./RatingControl.md): 별점 등급 입력.
*   [ShortcutPicker](./ShortcutPicker.md): 단축키 입력.
*   [AutoSuggestBox](./AutoSuggestBox.md): 자동 완성 제안 입력 상자.
*   [Watermark](./Watermark.md): 입력 필드 워터마크 (플레이스홀더).
*   [Captcha](./Captcha.md): 보안 문자 입력.

### 데이터 표시 (Data Display)

*   [Text](./Text.md): 텍스트 표시 및 서식 관련 컴포넌트.
*   [Image](./Image.md): 이미지 표시.
*   [Badge](./Badge.md): 상태나 알림 표시 뱃지.
*   [Tooltip](./Tooltip.md): 마우스 오버 시 추가 정보 표시.
*   [InfoBar](./InfoBar.md): 정보, 성공, 경고, 오류 메시지 표시.
*   [Progress](./Progress.md): 진행 상태 표시 (바, 링).
*   [TableView](./TableView.md): 테이블 형태 데이터 표시.
*   [TreeView](./TreeView.md): 계층 구조 데이터 표시.
*   [Chart](./Chart.md): 다양한 종류의 차트.
*   [Timeline](./Timeline.md): 시간 순서 이벤트 표시.
*   [QRCode](./QRCode.md): QR 코드 생성 및 표시.
*   [Clip](./Clip.md): 텍스트 클리핑 유틸리티.

### 피드백 (Feedback)

*   [Dialogs](./Dialogs.md): 대화 상자 (메시지 박스, 커스텀 다이얼로그 등).
*   [Sheet](./Sheet.md): 화면 하단/상단에서 나타나는 시트.
*   [Tour](./Tour.md): 사용자 인터페이스 기능 안내.
*   [WindowResultLauncher](./WindowResultLauncher.md): 창 실행 및 결과 처리.

### 창 및 페이지 (Window & Page)

*   [Window](./Window.md): 기본 애플리케이션 창.
*   [Page](./Page.md): `NavigationView` 등에서 사용되는 페이지 컨테이너.
*   [AppBar](./AppBar.md): 앱 상단 또는 하단 바.

### 메뉴 및 스크롤링 (Menu & Scrolling)

*   [Menu](./Menu.md): 컨텍스트 메뉴, 드롭다운 메뉴 등.
*   [ScrollingControls](./ScrollingControls.md): 스크롤 관련 컨트롤 및 기능.

### 시각 효과 및 스타일링 (Visual Effects & Styling)

*   [Acrylic](./Acrylic.md): 아크릴 배경 효과.
*   [Rectangle](./Rectangle.md): 사각형 기반 스타일링 및 레이아웃 요소.
*   [TextStyle](./TextStyle.md): 미리 정의된 텍스트 스타일.
*   [Theme](./Theme.md): 앱 전체 테마 (라이트/다크 모드 등).

### 기타 유틸리티 및 컨트롤 (Other Utilities & Controls)

*   [FlipView](./FlipView.md): 항목 간 플립 전환 뷰.
*   [Carousel](./Carousel.md): 회전 목마 형태 콘텐츠 표시.
*   [EventBus](./EventBus.md): 컴포넌트 간 통신을 위한 이벤트 버스.
*   [Router](./Router.md): 페이지 라우팅 관리.
*   [RemoteLoader](./RemoteLoader.md): 원격 콘텐츠 로딩.
*   [InternalControls](./InternalControls.md): 라이브러리 내부 사용 컨트롤.
*   [App](./App.md): 애플리케이션 레벨 유틸리티 및 설정.


## 문서 형식 가이드

컴포넌트 문서는 다음 형식을 따릅니다.

1.  **제목**: `# Fluent UI [컴포넌트 그룹명] 컴포넌트`
2.  **개요**: 컴포넌트 그룹에 대한 간략한 설명 및 기반 Qt Quick 컨트롤 언급.
3.  **공통 임포트 방법**: 해당 그룹의 컴포넌트 사용에 필요한 일반적인 import 구문.
4.  **공통 기능 및 속성 (선택 사항)**: 그룹 내 여러 컴포넌트가 공유하는 기능, 프로퍼티, 메소드, 시그널 설명.
5.  **개별 컴포넌트 섹션**: `## [컴포넌트 이름]`
    *   **설명**: 컴포넌트의 역할과 특징.
    *   **주요 상속 프로퍼티/시그널 (선택 사항)**: 기반 클래스로부터 상속받는 중요한 멤버 목록.
    *   **고유/특징적 프로퍼티**: 해당 컴포넌트만의 프로퍼티 또는 동작 방식이 특별한 프로퍼티.
    *   **고유 메소드**: 해당 컴포넌트만의 메소드.
    *   **고유 시그널**: 해당 컴포넌트만의 시그널.
    *   **예제**: 간단한 사용 예시 코드.
    *   **참고 사항**: 주의할 점이나 추가 정보.

### 테이블 형식

문서 내 프로퍼티, 메소드, 시그널 정보는 다음 테이블 형식을 사용합니다.

**프로퍼티 테이블:**

| 이름     | 타입     | 기본값 | 설명           |
| :------- | :------- | :----- | :------------- |
| `propName` | `propType` | `값`   | 프로퍼티 설명. |

**메소드 테이블:**

| 이름         | 파라미터                   | 반환타입     | 설명         |
| :----------- | :------------------------- | :----------- | :----------- |
| `methodName` | `paramType`: `paramName` | `returnType` | 메소드 설명. |

**시그널 테이블:**

| 이름         | 파라미터                   | 반환타입 | 설명         |
| :----------- | :------------------------- | :------- | :----------- |
| `signalName` | `paramType`: `paramName` | -        | 시그널 설명. |