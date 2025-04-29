# 포커스 (Focus)

**모듈:** `import QtQuick`

## 개요

QML에서 포커스(Focus)는 현재 키보드 입력을 받아들일 아이템을 결정하는 메커니즘입니다. 사용자가 키보드를 사용하여 인터페이스와 상호작용할 때(예: 텍스트 입력, 버튼 활성화, 항목 선택 등), 어떤 아이템이 해당 입력을 처리할지 지정하는 것이 중요합니다.

포커스 관리는 주로 `Item`의 `focus`와 `activeFocus` 프로퍼티, 그리고 `FocusScope` 컴포넌트를 통해 이루어집니다.

## 상세 설명

### 기본 프로퍼티

*   **`focus` (타입: `bool`, 기본값: `false`)**: 아이템이 키보드 포커스를 받을 *수 있는지* 여부를 나타냅니다. `true`로 설정된 아이템만 `activeFocus` 상태가 될 수 있습니다. 사용자와 상호작용하는 컨트롤이나 `Keys` Attached Property를 사용하는 아이템에 `true`를 설정합니다.
*   **`activeFocus` (타입: `bool`, 기본값: `false`, 읽기 전용*)**: 아이템이 현재 활성 키보드 포커스를 가지고 *있는지* 여부를 나타냅니다. `Window` 또는 `FocusScope` 내에서 단 하나의 아이템만 `activeFocus`가 `true`일 수 있으며, 이 아이템이 키보드 입력을 받습니다. (`forceActiveFocus()` 메소드로 변경 가능)
*   **`activeFocusOnTab` (타입: `bool`, 기본값: `false`)**: Tab 키로 포커스를 이동할 때 이 아이템이 포커스 체인(focus chain)에 포함될지 여부를 결정합니다. `focus`와 `activeFocusOnTab`이 모두 `true`인 아이템들 사이에서만 Tab 이동이 일어납니다.

### 주요 메소드

*   **`forceActiveFocus(reason)`**: 특정 아이템에 활성 포커스를 강제로 설정합니다. 해당 아이템의 `focus` 프로퍼티가 `true`여야 합니다.
*   **`nextItemInFocusChain()`, `previousItemInFocusChain()`**: Tab 또는 Shift+Tab 시 다음에 포커스를 받을 아이템을 반환합니다.

### FocusScope 컴포넌트

`FocusScope`는 포커스 관리를 위한 컨테이너 역할을 하는 보이지 않는 아이템입니다.

*   **독립적인 포커스 체인:** `FocusScope` 내부에 있는 아이템들은 자신만의 독립적인 포커스 체인(Tab 순서)을 가집니다. 사용자가 Tab 키를 누르면 `FocusScope` 내부에서 포커스가 순환합니다.
*   **포커스 위임:** `FocusScope` 자체가 `activeFocus`를 가질 수 있으며, 이때 실제 키보드 이벤트는 `FocusScope` 내부에서 마지막으로 `activeFocus`를 가졌던 아이템 등으로 전달될 수 있습니다.
*   **활용:** 복잡한 UI 컴포넌트나 대화상자 등에서 내부 요소들의 포커스 흐름을 외부와 분리하고 관리하는 데 유용합니다.

## 예제

```qml
import QtQuick

Window {
    width: 400
    height: 150
    visible: true
    title: "Focus Example"

    // 기본 포커스 체인 (Window가 관리)
    Row {
        id: topRow
        spacing: 10
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 10

        Button { id: btn1; text: "Button 1"; focus: true; activeFocusOnTab: true }
        Button { id: btn2; text: "Button 2"; focus: true; activeFocusOnTab: true }
    }

    // FocusScope를 사용한 독립적인 포커스 체인
    FocusScope {
        id: focusScope
        width: parent.width; height: 50
        anchors.top: topRow.bottom
        anchors.topMargin: 20

        property alias scopeText: scopeStatus.text

        focus: true // FocusScope 자체도 포커스를 받을 수 있음
        activeFocusOnTab: true // Tab으로 이 Scope에 진입 가능

        Keys.onPressed: {
            // Scope가 포커스를 가졌을 때 키 이벤트 처리 (내부 아이템이 포커스 없으면)
            console.log("FocusScope received key", event.key)
            scopeStatus.text = "FocusScope has focus (key: " + event.key + ")"
        }

        Row {
            anchors.centerIn: parent
            spacing: 10

            TextField {
                id: input1
                placeholderText: "Input 1"
                focus: true // 기본적으로 true
                activeFocusOnTab: true // 기본적으로 true
                Keys.onPressed: focusScope.scopeText = "Input 1 has focus"
            }
            TextField {
                id: input2
                placeholderText: "Input 2"
                focus: true
                activeFocusOnTab: true
                Keys.onPressed: focusScope.scopeText = "Input 2 has focus"
            }
            Button { // 이 버튼은 Tab으로 포커스 받지 않음
                id: btnInScope
                text: "Scope Btn"
                focus: true
                activeFocusOnTab: false // Tab 순서에서 제외
                MouseArea { anchors.fill: parent; onClicked: parent.forceActiveFocus() }
                Keys.onPressed: focusScope.scopeText = "Scope Btn has focus"
            }
        }

        // FocusScope 내에서 마지막 활성 포커스 아이템을 추적할 수 있음
        // Component.onCompleted: { input1.forceActiveFocus() } // 시작 시 input1에 포커스
    }

    Text { // 상태 표시용
        id: scopeStatus
        anchors.top: focusScope.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 10
        text: "Tab between elements. Click 'Scope Btn' to focus it."
    }
}

// --- Button.qml (간단한 버튼 구현) ---
import QtQuick

Rectangle {
    id: buttonRoot
    width: childrenRect.width + 20
    height: childrenRect.height + 10
    color: activeFocus ? "orange" : "lightgray"
    border.color: "gray"
    radius: 3

    property alias text: buttonText.text

    // focus, activeFocusOnTab 등은 외부에서 설정

    Text {
        id: buttonText
        anchors.centerIn: parent
        text: "Button"
    }

    MouseArea {
        anchors.fill: parent
        onClicked: buttonRoot.forceActiveFocus()
    }

    Keys.onSpacePressed: {
        console.log(buttonText.text + " activated by Space")
        event.accepted = true
    }
    Keys.onReturnPressed: {
        console.log(buttonText.text + " activated by Enter")
        event.accepted = true
    }
}
// --- TextField.qml (간단한 텍스트 필드 구현) ---
import QtQuick

Rectangle {
    id: textFieldRoot
    width: 100; height: 30
    color: "white"
    border.color: activeFocus ? "orange" : "darkgray"

    property alias text: textInput.text
    property alias placeholderText: textInput.placeholderText

    // focus, activeFocusOnTab 등은 외부에서 설정 (TextInput 기본값 사용)

    TextInput {
        id: textInput
        anchors.fill: parent
        anchors.margins: 5
        focus: true // TextInput은 기본적으로 focus가 true
        font.pixelSize: 14

        // 입력 필드가 활성 포커스를 가질 때 부모 Rectangle도 표시 업데이트
        onActiveFocusChanged: {
            if (activeFocus) textFieldRoot.border.color = "orange"
            else textFieldRoot.border.color = "darkgray"
        }
    }
}

```

## 참고 사항

*   키보드 포커스 관리는 사용자 경험에 큰 영향을 미칩니다. 논리적인 Tab 순서를 제공하고, 현재 포커스 위치를 시각적으로 명확히 표시하는 것이 중요합니다.
*   `KeyNavigation` Attached Property를 사용하여 화살표 키를 이용한 포커스 이동을 구현할 수도 있습니다.
*   모바일 환경 등 터치 기반 인터페이스에서는 키보드 포커스의 중요성이 상대적으로 낮을 수 있지만, 접근성(Accessibility) 측면에서는 여전히 중요합니다. 