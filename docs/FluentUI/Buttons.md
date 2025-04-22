# 버튼 컴포넌트 (Button Components)

FluentUI는 다양한 상황에 적합한 여러 버튼 스타일을 제공합니다. 이 문서에서는 각 버튼 컴포넌트의 주요 속성과 사용 예제를 설명합니다.

## 기본 버튼 (FluButton)

기본 버튼 컴포넌트로, 일반적인 작업에 사용됩니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `disabled`: 버튼 비활성화 여부 (기본값: false)
- `normalColor`: 일반 상태 배경색
- `hoverColor`: 마우스 호버 시 배경색
- `disableColor`: 비활성화 상태 배경색
- `textColor`: 텍스트 색상
- `contentDescription`: 접근성을 위한 설명

### 사용 예제
```qml
import FluentUI
import QtQuick

FluButton{
    text: qsTr("Standard Button")
    disabled: false
    onClicked: {
        console.log("Standard Button Clicked")
    }
}
```

## 채워진 버튼 (FluFilledButton)

강조된 액션을 위한 채워진 스타일의 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `disabled`: 버튼 비활성화 여부 (기본값: false)
- `normalColor`: 일반 상태 배경색 (기본값: FluTheme.primaryColor)
- `hoverColor`: 마우스 호버 시 배경색
- `pressedColor`: 누른 상태 배경색
- `disableColor`: 비활성화 상태 배경색
- `textColor`: 텍스트 색상

### 사용 예제
```qml
import FluentUI
import QtQuick

FluFilledButton{
    text: qsTr("Filled Button")
    disabled: false
    onClicked: {
        console.log("Filled Button Clicked")
    }
}
```

## 텍스트 버튼 (FluTextButton)

최소한의 스타일이 적용된 텍스트 형태의 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `disabled`: 버튼 비활성화 여부 (기본값: false)
- `font`: 텍스트 폰트
- `textColor`: 텍스트 색상
- `contentDescription`: 접근성을 위한 설명

### 사용 예제
```qml
import FluentUI
import QtQuick

FluTextButton{
    text: qsTr("Text Button")
    disabled: false
    onClicked: {
        console.log("Text Button Clicked")
    }
}
```

## 아이콘 버튼 (FluIconButton)

아이콘만 표시하는 버튼입니다.

### 주요 속성
- `iconSource`: 표시할 아이콘 소스 (FluentIcons 사용)
- `iconSize`: 아이콘 크기
- `iconColor`: 아이콘 색상
- `disabled`: 버튼 비활성화 여부 (기본값: false)
- `display`: 표시 방식

### 사용 예제
```qml
import FluentUI

FluIconButton {
    iconSource: FluentIcons.Add
    iconSize: 16
    onClicked: {
        console.log("아이콘 버튼이 클릭되었습니다")
    }
}
```

## 토글 버튼 (FluToggleButton)

두 가지 상태(활성화/비활성화)를 전환할 수 있는 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `checked`: 체크 상태
- `checkColor`: 체크 상태일 때 색상 (기본값: FluTheme.primaryColor)
- `disabled`: 버튼 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import FluentUI
import QtQuick

FluToggleButton{
    text: qsTr("Toggle Button")
    disabled: false
    onClicked: {
        console.log("토글 상태: " + checked)
    }
}
```

## 드롭다운 버튼 (FluDropDownButton)

클릭 시 메뉴가 표시되는 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `items`: 드롭다운에 표시될 메뉴 아이템들
- `disabled`: 버튼 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import FluentUI

FluDropDownButton {
    text: "드롭다운 버튼"
    items: [
        FluMenuItem {
            text: "옵션 1"
            onClicked: console.log("옵션 1 선택됨")
        },
        FluMenuItem {
            text: "옵션 2"
            onClicked: console.log("옵션 2 선택됨")
        }
    ]
}
```

## 로딩 버튼 (FluLoadingButton)

로딩 상태를 표시할 수 있는 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `loading`: 로딩 상태 여부
- `disabled`: 버튼 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import FluentUI
import QtQuick

FluLoadingButton{
    text: qsTr("Loading Button")
    loading: false
    onClicked: {
        // 로딩 시작
        loading = true
        
        // 작업 완료 후 로딩 끝내기
        // loading = false 
    }
}
```

## 진행 버튼 (FluProgressButton)

진행 상태를 표시할 수 있는 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `progress`: 진행률 (0.0 ~ 1.0)
- `disabled`: 버튼 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import FluentUI
import QtQuick

FluProgressButton{
    id: progressButton
    text: qsTr("Progress Button")
    progress: 0
    onClicked: {
        progressButton.progress = 0
        
        // 진행률 증가 예시 (실제로는 작업에 따라 업데이트)
        // Timer 등을 사용하여 progress 값을 0부터 1까지 조절
        timer.restart()
    }
    
    Timer {
        id: timer
        interval: 200
        repeat: true
        onTriggered: {
            progressButton.progress = (progressButton.progress + 0.1).toFixed(1)
            if(progressButton.progress >= 1.0) {
                stop()
            }
        }
    }
}
```

## 키보드 지원

모든 버튼 컴포넌트는 Tab 키로 포커스를 이동하고 Space 키로 클릭 이벤트를 실행할 수 있습니다. 