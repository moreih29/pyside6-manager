# 입력 컴포넌트 (Input Controls)

FluentUI는 사용자로부터 데이터를 입력받기 위한 다양한 입력 컴포넌트를 제공합니다. 이 문서에서는 각 입력 컴포넌트의 주요 속성과 사용 예제를 설명합니다.

## 텍스트 박스 (FluTextBox)

단일 라인 텍스트를 입력받기 위한 컴포넌트입니다.

### 주요 속성
- `text`: 텍스트 내용
- `placeholderText`: 입력 전 표시되는 안내 텍스트
- `disabled`: 비활성화 여부 (기본값: false)
- `iconSource`: 아이콘 소스 (FluentIcons 사용)
- `readOnly`: 읽기 전용 여부
- `selectByMouse`: 마우스로 텍스트 선택 가능 여부 (기본값: true)
- `cleanEnabled`: 텍스트 지우기 버튼 표시 여부 (기본값: true)

### 신호 (Signals)
- `commit(string text)`: 텍스트 입력 완료 시(Enter/Return 키 누름) 발생

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluTextBox {
        placeholderText: qsTr("Single-line Input Box")
        disabled: disableSwitch.checked
        cleanEnabled: true
        onCommit: function(text) {
            console.log("입력된 텍스트: " + text)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 멀티라인 텍스트 박스 (FluMultilineTextBox)

여러 줄의 텍스트를 입력받기 위한 컴포넌트입니다.

### 주요 속성
- `text`: 텍스트 내용
- `placeholderText`: 입력 전 표시되는 안내 텍스트
- `disabled`: 비활성화 여부 (기본값: false)
- `readOnly`: 읽기 전용 여부
- `wrapMode`: 텍스트 줄바꿈 모드

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluMultilineTextBox {
        id: multilineTextBox
        width: 300
        height: 150
        placeholderText: qsTr("Multi-line Input Box")
        disabled: disableSwitch.checked
        wrapMode: Text.Wrap
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 비밀번호 박스 (FluPasswordBox)

비밀번호 입력을 위한 컴포넌트입니다.

### 주요 속성
- `text`: 텍스트 내용
- `placeholderText`: 입력 전 표시되는 안내 텍스트
- `disabled`: 비활성화 여부 (기본값: false)
- `iconSource`: 아이콘 소스 (FluentIcons 사용)
- `revealPasswordButtonEnabled`: 비밀번호 표시 버튼 활성화 여부

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluPasswordBox {
        placeholderText: qsTr("Please enter your password")
        disabled: disableSwitch.checked
        revealPasswordButtonEnabled: true
        onCommit: function(text) {
            console.log("비밀번호가 입력되었습니다")
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 콤보 박스 (FluComboBox)

드롭다운 목록에서 항목을 선택할 수 있는 컴포넌트입니다.

### 주요 속성
- `model`: 표시할 항목 모델
- `currentIndex`: 현재 선택된 인덱스
- `currentText`: 현재 선택된 텍스트
- `disabled`: 비활성화 여부 (기본값: false)
- `placeholderText`: 아무것도 선택되지 않았을 때 표시되는 텍스트

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluComboBox {
        model: ["옵션 1", "옵션 2", "옵션 3"]
        placeholderText: "선택하세요"
        disabled: disableSwitch.checked
        onCurrentIndexChanged: {
            console.log("선택된 항목: " + currentText)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 자동 완성 검색 박스 (FluAutoSuggestBox)

검색 및 자동 완성 기능을 제공하는 컴포넌트입니다.

### 주요 속성
- `items`: 자동 완성 항목 목록
- `text`: 입력 텍스트
- `placeholderText`: 입력 전 표시되는 안내 텍스트
- `caseSensitive`: 대소문자 구분 여부
- `iconSource`: 아이콘 소스 (FluentIcons 사용)
- `disabled`: 비활성화 여부 (기본값: false)

### 신호 (Signals)
- `textChanged(string text)`: 텍스트 변경 시 발생
- `itemClicked(var item)`: 항목 클릭 시 발생

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluAutoSuggestBox {
        placeholderText: qsTr("AutoSuggestBox")
        iconSource: FluentIcons.Search
        disabled: disableSwitch.checked
        items: [
            {title: "Apple"},
            {title: "Banana"},
            {title: "Orange"},
            {title: "Grape"}
        ]
        onItemClicked: function(item) {
            console.log("선택된 항목: " + item.title)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 체크 박스 (FluCheckBox)

선택 여부를 표시하는 체크 박스 컴포넌트입니다.

### 주요 속성
- `text`: 체크 박스 텍스트
- `checked`: 체크 상태
- `disabled`: 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluCheckBox {
        text: qsTr("동의합니다")
        disabled: disableSwitch.checked
        onCheckedChanged: {
            console.log("체크 상태: " + checked)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 라디오 버튼 (FluRadioButton)

여러 옵션 중 하나를 선택하는 컴포넌트입니다.

### 주요 속성
- `text`: 라디오 버튼 텍스트
- `checked`: 체크 상태
- `disabled`: 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import QtQuick
import FluentUI

Column {
    spacing: 10
    
    Row {
        spacing: 20
        
        Column {
            spacing: 5
            
            FluRadioButton {
                id: option1
                text: qsTr("옵션 1")
                checked: true
                disabled: disableSwitch.checked
                onClicked: {
                    if (checked) option2.checked = false
                }
            }
            
            FluRadioButton {
                id: option2
                text: qsTr("옵션 2")
                disabled: disableSwitch.checked
                onClicked: {
                    if (checked) option1.checked = false
                }
            }
        }
        
        FluToggleSwitch {
            id: disableSwitch
            text: qsTr("Disabled")
        }
    }
}
```

## 라디오 버튼 그룹 (FluRadioButtons)

라디오 버튼을 그룹으로 관리하는 컴포넌트입니다.

### 주요 속성
- `spacing`: 버튼 간 간격
- `currentIndex`: 현재 선택된 인덱스
- `model`: 표시할 항목 모델
- `disabled`: 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluRadioButtons {
        model: ["옵션 1", "옵션 2", "옵션 3"]
        disabled: disableSwitch.checked
        onCurrentIndexChanged: {
            console.log("선택된 인덱스: " + currentIndex)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 슬라이더 (FluSlider)

범위 내에서 값을 선택할 수 있는 슬라이더 컴포넌트입니다.

### 주요 속성
- `value`: 현재 값
- `from`: 최소값
- `to`: 최대값
- `stepSize`: 단계 크기
- `disabled`: 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluSlider {
        width: 200
        from: 0
        to: 100
        stepSize: 1
        disabled: disableSwitch.checked
        onValueChanged: {
            console.log("슬라이더 값: " + value)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 레인지 슬라이더 (FluRangeSlider)

범위 내에서 두 값의 범위를 선택할 수 있는 슬라이더 컴포넌트입니다.

### 주요 속성
- `first.value`: 첫 번째 핸들의 값
- `second.value`: 두 번째 핸들의 값
- `from`: 최소값
- `to`: 최대값
- `stepSize`: 단계 크기
- `disabled`: 비활성화 여부 (기본값: false)

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluRangeSlider {
        width: 200
        from: 0
        to: 100
        stepSize: 1
        first.value: 25
        second.value: 75
        disabled: disableSwitch.checked
        onFirstValueChanged: {
            console.log("첫 번째 값: " + first.value)
        }
        onSecondValueChanged: {
            console.log("두 번째 값: " + second.value)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 스핀 박스 (FluSpinBox)

숫자 값을 입력하고 조절할 수 있는 컴포넌트입니다.

### 주요 속성
- `value`: 현재 값
- `from`: 최소값
- `to`: 최대값
- `stepSize`: 단계 크기
- `disabled`: 비활성화 여부 (기본값: false)
- `editable`: 직접 편집 가능 여부

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluSpinBox {
        from: 0
        to: 100
        value: 50
        stepSize: 1
        disabled: disableSwitch.checked
        onValueChanged: {
            console.log("스핀 박스 값: " + value)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
```

## 토글 스위치 (FluToggleSwitch)

켜기/끄기 상태를 전환하는 스위치 컴포넌트입니다.

### 주요 속성
- `text`: 스위치 텍스트
- `checked`: 체크 상태
- `disabled`: 비활성화 여부 (기본값: false)
- `textRight`: 텍스트 위치가 오른쪽인지 여부 (기본값: true)
- `checkColor`: 체크 상태일 때 색상 (기본값: FluTheme.primaryColor)

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 20
    
    FluToggleSwitch {
        text: qsTr("알림 켜기")
        disabled: disableSwitch.checked
        onClicked: {
            console.log("토글 상태: " + checked)
        }
    }
    
    FluToggleSwitch {
        id: disableSwitch
        text: qsTr("Disabled")
    }
}
``` 