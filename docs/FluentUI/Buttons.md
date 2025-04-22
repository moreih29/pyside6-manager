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

FluButton {
    text: "기본 버튼"
    onClicked: {
        console.log("버튼이 클릭되었습니다")
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

FluFilledButton {
    text: "강조 버튼"
    onClicked: {
        console.log("강조 버튼이 클릭되었습니다")
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

FluTextButton {
    text: "텍스트 버튼"
    onClicked: {
        console.log("텍스트 버튼이 클릭되었습니다")
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

FluToggleButton {
    text: "토글 버튼"
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

FluLoadingButton {
    id: loadingButton
    text: "로딩 버튼"
    onClicked: {
        loading = true
        // 일정 시간 후 로딩 상태 해제
        timer.start()
    }

    Timer {
        id: timer
        interval: 2000
        onTriggered: {
            loadingButton.loading = false
        }
    }
}
```

## 진행 버튼 (FluProgressButton)

진행 상태를 표시할 수 있는 버튼입니다.

### 주요 속성
- `text`: 버튼에 표시될 텍스트
- `progress`: 진행률 (0-100)
- `loading`: 로딩 상태 여부
- `disabled`: 버튼 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import FluentUI

FluProgressButton {
    id: progressButton
    text: "진행 버튼"
    onClicked: {
        loading = true
        progress = 0
        progressTimer.start()
    }

    Timer {
        id: progressTimer
        interval: 100
        repeat: true
        onTriggered: {
            progressButton.progress += 5
            if (progressButton.progress >= 100) {
                progressButton.loading = false
                progressButton.progress = 0
                stop()
            }
        }
    }
}
``` 