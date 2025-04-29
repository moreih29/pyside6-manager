# ListModel

**모듈:** `import QtQuick`

## 개요

`ListModel`은 QML에서 동적인 데이터 목록을 정의하는 데 사용되는 가장 기본적인 모델 요소입니다. 각 목록 항목은 하나 이상의 데이터 **역할(role)** 을 가질 수 있으며, 이 역할들은 뷰의 델리게이트(delegate)에서 접근하여 데이터를 표시하는 데 사용됩니다.

`ListModel`은 QML 코드 내에서 직접 데이터를 정의하거나, JavaScript를 사용하여 동적으로 데이터를 추가, 수정, 삭제할 수 있는 편리한 방법을 제공합니다.

## 기반 클래스

*   `QObject` (QML 타입 시스템의 일부)

## 주요 프로퍼티

| 이름    | 타입   | 기본값 | 설명                                                          |
| :------ | :----- | :----- | :------------------------------------------------------------ |
| `count` | `int`  | (읽기 전용) | 모델에 포함된 항목의 총 개수.                               |
| `dynamicRoles` | `bool` | `false` | `true`로 설정하면 모델이 생성된 후에도 새로운 역할을 동적으로 추가할 수 있습니다. 성능에 영향을 줄 수 있으므로 필요한 경우에만 사용합니다. |

## 주요 메소드

`ListModel`은 JavaScript를 통해 모델 데이터를 조작하는 다양한 메소드를 제공합니다.

| 이름                           | 파라미터                                        | 반환타입 | 설명                                                                                                |
| :----------------------------- | :---------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------- |
| `append(jsobject item)`        | `object`: 추가할 항목 데이터 (역할 이름: 값)     | -        | 모델의 끝에 새 항목을 추가합니다.                                                                   |
| `insert(int index, jsobject item)` | `int`: 삽입할 위치 인덱스, `object`: 추가할 항목 | -        | 지정된 인덱스에 새 항목을 삽입합니다.                                                               |
| `remove(int index, int count)` | `int`: 삭제 시작 인덱스, `int`: 삭제할 개수(기본값 1) | -        | 지정된 인덱스부터 `count`개의 항목을 제거합니다.                                                    |
| `clear()`                      | -                                               | -        | 모델의 모든 항목을 제거합니다.                                                                      |
| `set(int index, jsobject item)`| `int`: 수정할 항목 인덱스, `object`: 새 항목 데이터 | -        | 지정된 인덱스의 항목 데이터를 새 데이터로 교체합니다. `item` 객체에 포함된 역할만 업데이트됩니다.         |
| `setProperty(int index, string property, variant value)` | `int`: 인덱스, `string`: 역할 이름, `variant`: 새 값 | -        | 지정된 인덱스 항목의 특정 역할(`property`) 값을 `value`로 설정합니다.                                 |
| `get(int index)`               | `int`: 가져올 항목 인덱스                          | `object` | 지정된 인덱스의 항목 데이터를 JavaScript 객체 (역할 이름: 값) 형태로 반환합니다.                             |
| `move(int from, int to, int count)` | `int`: 이동 시작 인덱스, `int`: 이동 목표 인덱스, `int`: 이동할 개수 | -        | `from` 인덱스부터 `count`개의 항목을 `to` 인덱스로 이동합니다.                                        |

## 주요 시그널

`ListModel`은 데이터 변경 시 뷰를 업데이트하기 위해 내부적으로 시그널을 사용하지만, 일반적으로 QML 코드에서 직접 이러한 시그널에 연결하는 경우는 드뭅니다. 뷰 컴포넌트(`ListView` 등)가 이러한 변경 사항을 감지하고 자동으로 UI를 업데이트합니다.

## 예제

### 예제 1: QML에서 직접 정의

```qml
import QtQuick

ListView {
    width: 200; height: 250

    model: ListModel {
        id: fruitModel

        ListElement {
            name: "Apple"
            cost: 2.50
            color: "red"
        }
        ListElement {
            name: "Orange"
            cost: 3.00
            color: "orange"
        }
        ListElement {
            name: "Banana"
            cost: 1.75
            color: "yellow"
        }
    }

    delegate: Text {
        // 델리게이트에서 모델 역할(role) 이름으로 데이터 접근
        text: "Fruit: " + name + " ($ " + cost.toFixed(2) + ")"
        color: model.color // model. 접두사 사용 가능
        font.pointSize: 12
        width: parent.width // 너비를 ListView에 맞춤
        padding: 5
    }
}
```

### 예제 2: JavaScript로 동적 조작

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300; height: 400
    visible: true

    ListModel {
        id: dynamicModel
        // 초기에 빈 모델
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: dynamicModel
            clip: true

            delegate: Rectangle {
                width: listView.width
                height: 40
                color: index % 2 === 0 ? "lightgray" : "white"
                border.color: "gray"

                RowLayout {
                    anchors.fill: parent
                    anchors.margins: 5
                    Label { text: model.itemText }
                    Item { Layout.fillWidth: true } // 공간 채우기
                    Button {
                        text: "Remove"
                        onClicked: dynamicModel.remove(index) // 해당 인덱스 항목 제거
                    }
                }
            }
        }

        RowLayout {
            TextField {
                id: newItemInput
                Layout.fillWidth: true
                placeholderText: "Enter new item text"
            }
            Button {
                text: "Add"
                onClicked: {
                    if (newItemInput.text.trim() !== "") {
                        // append 메소드로 새 항목 추가
                        dynamicModel.append({ itemText: newItemInput.text.trim() })
                        newItemInput.text = "" // 입력 필드 초기화
                    }
                }
            }
        }
        Button {
            text: "Clear All"
            Layout.alignment: Qt.AlignRight
            onClicked: dynamicModel.clear()
        }
    }
}
```

## 참고 사항

*   `ListModel`의 각 항목은 `ListElement`를 사용하여 QML 내에서 정의됩니다.
*   `ListElement` 내부에 정의된 프로퍼티들이 해당 항목의 **역할(role)** 이 됩니다. 역할 이름은 델리게이트에서 직접 사용하거나 `model.` 접두사를 붙여 사용할 수 있습니다 (`name` 또는 `model.name`).
*   JavaScript를 사용하여 `ListModel`을 조작할 때는 `id`를 부여하고 해당 `id`를 통해 메소드(`append`, `insert`, `remove`, `set`, `setProperty`, `get`, `move`, `clear`)를 호출합니다.
*   `set` 메소드는 제공된 객체에 포함된 역할만 업데이트하는 반면, `setProperty`는 특정 역할 하나만 업데이트합니다.
*   대량의 데이터를 다루거나 C++ 백엔드와 데이터를 연동해야 하는 경우에는 C++ 기반 모델(`QAbstractListModel` 등)을 사용하는 것이 더 효율적입니다. 