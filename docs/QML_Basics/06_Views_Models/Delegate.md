# Delegate (모델-뷰)

**모듈:** 관련 없음 (개념 설명)

## 개요

모델-뷰 아키텍처에서 **델리게이트(Delegate)** 는 모델(Model)의 각 데이터 항목을 뷰(View)에서 어떻게 시각적으로 표현할지를 정의하는 QML 컴포넌트 템플릿입니다. 뷰(`ListView`, `GridView`, `TableView` 등)는 모델의 항목 수만큼 이 델리게이트 컴포넌트의 인스턴스를 (필요에 따라) 생성하여 화면에 표시합니다.

델리게이트는 모델 데이터와 UI 표현을 연결하는 핵심적인 역할을 수행하며, 모델-뷰 패턴의 유연성과 재사용성을 가능하게 합니다.

## 역할

*   **데이터 시각화**: 모델의 각 항목 데이터를 가져와 사용자 인터페이스 요소(텍스트, 이미지, 도형 등)로 변환하여 표시합니다.
*   **상호작용 처리**: 각 항목에 대한 사용자 입력(클릭, 터치 등)을 처리할 수 있습니다 (예: `MouseArea` 사용).
*   **상태 표현**: 모델 항목의 상태(예: 선택 여부)에 따라 시각적 표현을 다르게 할 수 있습니다.

## 사용 방법

델리게이트는 일반적으로 뷰 컴포넌트(`ListView`, `GridView` 등)의 `delegate` 프로퍼티에 `Component` 타입으로 정의됩니다.

```qml
import QtQuick

ListView {
    width: 200; height: 200
    model: ListModel {
        ListElement { itemText: "Apple"; itemColor: "red" }
        ListElement { itemText: "Banana"; itemColor: "yellow" }
        ListElement { itemText: "Orange"; itemColor: "orange" }
    }

    // delegate 프로퍼티에 Component 정의
    delegate: Component {
        // Component 내부의 최상위 아이템이 각 모델 항목을 대표
        Rectangle {
            id: itemRoot
            width: ListView.view.width // 부모 ListView 너비 사용
            height: 40
            color: itemColor // 모델 역할(role) 직접 접근

            Text {
                anchors.centerIn: parent
                // model. 접두사로 역할 접근 또는 직접 접근
                text: "Item " + index + ": " + model.itemText
                color: Qt.contrastColor(itemRoot.color)
            }

            // 각 항목 클릭 처리
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // 클릭 시 현재 항목 인덱스를 ListView의 currentIndex로 설정
                    ListView.view.currentIndex = index
                    console.log("Clicked on:", itemText, "at index", index)
                }
            }

            // 현재 선택된 항목인지 여부에 따라 테두리 표시
            border.color: ListView.isCurrentItem ? "blue" : "transparent"
            border.width: ListView.isCurrentItem ? 2 : 0
        }
    } // End of Component
}
```

## 컨텍스트 프로퍼티 (Context Properties)

델리게이트 컴포넌트 내부에서는 뷰와 모델에 대한 정보에 접근할 수 있는 특별한 **컨텍스트 프로퍼티** 들이 제공됩니다. 이를 통해 모델 데이터와 뷰의 상태를 활용하여 델리게이트를 동적으로 구성할 수 있습니다.

주요 컨텍스트 프로퍼티는 다음과 같습니다 (뷰의 종류에 따라 약간의 차이가 있을 수 있음):

| 이름           | 타입    | 설명                                                                                                                                     |
| :------------- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------- |
| `index`        | `int`   | 현재 델리게이트 인스턴스가 나타내는 모델 항목의 인덱스 (0부터 시작).                                                                             |
| `model`        | `object`| (`TableView`의 `delegate` 제외) `ListModel` 등에서 정의된 역할(role) 이름에 직접 접근할 수 있게 해주는 객체. `model.roleName` 형태로도 사용 가능.      |
| `modelData`    | `variant`| 현재 항목의 기본 데이터. 모델이 단순 값(숫자, 문자열) 또는 JavaScript 객체일 때 주로 사용됩니다. `ListModel`에서는 역할 이름으로 직접 접근하는 것이 일반적입니다. |
| *역할 이름*    | `variant`| (`ListModel` 사용 시) 모델에 정의된 각 역할(role) 이름. 델리게이트 내에서 해당 이름으로 직접 값에 접근할 수 있습니다 (예: `name`, `itemColor`).             |
| `ListView.view`| `ListView`| (ListView의 델리게이트 내) 부모 `ListView` 인스턴스에 접근. `ListView.view.width` 와 같이 사용.                                                      |
| `GridView.view`| `GridView`| (GridView의 델리게이트 내) 부모 `GridView` 인스턴스에 접근. `GridView.view.cellWidth` 와 같이 사용.                                                   |
| `TableView.view`| `TableView`| (TableView의 델리게이트 내) 부모 `TableView` 인스턴스에 접근.                                                                             |
| `ListView.isCurrentItem` | `bool` | (ListView의 델리게이트 내) 현재 델리게이트가 `ListView`의 `currentItem`인지 여부.                                                              |
| `GridView.isCurrentItem` | `bool` | (GridView의 델리게이트 내) 현재 델리게이트가 `GridView`의 `currentItem`인지 여부.                                                              |
| `row`          | `int`   | (TableView의 `delegate` 및 `rowDelegate` 내) 현재 셀 또는 행의 인덱스 (`index`와 유사).                                                            |
| `column`       | `int`   | (TableView의 `delegate` 내) 현재 셀의 열 인덱스.                                                                                             |
| `selected`     | `bool`  | (TableView의 `delegate` 및 `rowDelegate` 내) 현재 셀 또는 행이 선택되었는지 여부.                                                             |
| `current`      | `bool`  | (TableView의 `delegate` 내) 현재 셀이 `TableView`의 `currentCell`인지 여부 (`currentRow` 및 `currentColumn`과 일치).                             |

**참고:** `TableView`의 셀 델리게이트(`delegate`)에서는 모델의 역할 이름에 직접 접근할 수 없습니다. 대신 `modelData` (해당 셀의 값) 또는 `model` (전체 모델 객체)을 통해 접근해야 합니다.

## 성능 고려사항

*   **델리게이트 경량화**: 델리게이트는 모델의 항목 수만큼 생성될 수 있으므로 (특히 `reuseItems: false`인 경우), 가능한 한 가볍고 빠르게 로드되도록 작성해야 합니다. 복잡한 로직이나 많은 수의 아이템 포함은 피하는 것이 좋습니다.
*   **아이템 재사용 (`reuseItems`)**: Qt 6.0부터 뷰는 기본적으로 화면 밖으로 나간 델리게이트 아이템을 재사용합니다 (`reuseItems: true`). 이는 성능 향상에 매우 중요합니다. 재사용 시 델리게이트 내부 상태 관리에 주의해야 할 수 있습니다 (필요 시 상태 초기화 등).
*   **필요한 데이터만 로딩**: 델리게이트 내에서 필요한 모델 데이터만 사용하고, 불필요한 연산이나 바인딩은 최소화합니다.

## 참고 사항

*   델리게이트는 `Component` 요소 안에 정의되어야 합니다.
*   `Component` 내부의 최상위 아이템이 각 모델 항목을 대표하는 시각적 요소가 됩니다.
*   컨텍스트 프로퍼티를 활용하여 모델 데이터와 뷰 상태에 따라 동적인 UI를 구성할 수 있습니다.
*   복잡한 델리게이트는 별도의 `.qml` 파일로 분리하여 재사용성과 가독성을 높일 수 있습니다. 