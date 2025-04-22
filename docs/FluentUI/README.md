# FluentUI 컴포넌트 라이브러리

FluentUI는 Qt/QML 기반의 모던하고 아름다운 사용자 인터페이스를 구축하기 위한 컴포넌트 라이브러리입니다. Microsoft의 Fluent Design System 디자인 언어를 기반으로 하며, 다양한 컴포넌트와 유틸리티를 제공합니다.

## 주요 특징

- 다크 모드와 라이트 모드 지원
- 반응형 디자인
- 풍부한 컴포넌트 세트
- 사용자 정의 가능한 테마
- 다국어 지원
- 접근성 기능

## 문서 구성

이 문서는 FluentUI 컴포넌트 라이브러리에 포함된 다양한 컴포넌트와 기능을 설명하는 내용을 담고 있습니다. 각 문서는 컴포넌트의 주요 속성과 사용 예제를 포함하고 있습니다.

### 컴포넌트 카테고리

1. [버튼 컴포넌트](./Buttons.md)
   - FluButton, FluFilledButton, FluTextButton, FluIconButton 등

2. [입력 컴포넌트](./InputControls.md)
   - FluTextBox, FluPasswordBox, FluComboBox, FluCheckBox 등

3. [레이아웃 컴포넌트](./LayoutControls.md)
   - FluWindow, FluPage, FluNavigationView, FluTabView 등

4. [다이얼로그 및 알림 컴포넌트](./DialogsAndNotifications.md)
   - FluContentDialog, FluInfoBar, FluPopup, FluTooltip 등

5. [데이터 시각화 컴포넌트](./DataVisualization.md)
   - FluChart, FluProgressBar, FluTimeline, FluTreeView 등

6. [유틸리티 및 도우미 컴포넌트](./UtilityComponents.md)
   - FluTheme, FluColors, FluIcon, FluTools 등

## 시작하기

FluentUI를 사용하기 위해서는 다음과 같은 단계를 따르세요:

### 1. 설치

```bash
pip install pyside6-manager
```

### 2. 프로젝트에 임포트

```python
from pyside_manager.qml.FluentUI import init, registerTypes
```

### 3. QML에서 사용

```qml
import QtQuick
import FluentUI

// Window 대신 FluWindow를 최상위 아이템으로 사용합니다.
FluWindow {
    width: 800
    height: 600
    visible: true // visible 속성 추가
    title: "FluentUI 예제"
    
    FluText {
        anchors.centerIn: parent
        text: "FluentUI에 오신 것을 환영합니다!"
        font: FluTextStyle.Title
    }
}
```

## 테마 관리

FluentUI는 테마를 쉽게 관리할 수 있는 `FluTheme` 싱글톤 객체를 제공합니다.

```qml
import FluentUI

FluWindow {
    id: window
    width: 800
    height: 600
    title: "테마 예제"
    
    Component.onCompleted: {
        // 다크 모드 설정
        FluTheme.darkMode = FluThemeType.DarkMode.Dark
        
        // 시스템 테마 따르기
        // FluTheme.darkMode = FluThemeType.DarkMode.System
    }
}
```

## 고급 예제

더 복잡한 UI 구성을 위한 고급 예제는 각 컴포넌트 문서를 참고하세요. 일반적인 패턴과 권장 사항은 다음과 같습니다:

1. **네비게이션 레이아웃**: `FluNavigationView`를 사용하여 탐색 구조를 구성하세요.
2. **응답형 UI**: `FluWindow`의 너비에 따라 레이아웃을 조정하세요.
3. **일관된 테마**: `FluTheme`의 색상 변수를 활용하여 일관된 디자인을 유지하세요.
4. **아이콘 활용**: `FluIcon`과 `FluentIcons` 열거형을 활용하여 일관된 아이콘을 사용하세요.

## 기여하기

FluentUI 프로젝트에 기여하거나 버그를 신고하려면 GitHub 저장소를 방문하세요.

## 라이선스

FluentUI는 MIT 라이선스 하에 배포됩니다. 