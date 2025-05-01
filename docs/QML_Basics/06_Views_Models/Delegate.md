# Delegate (모델-뷰)

## 개요

모델-뷰 아키텍처에서 **델리게이트(Delegate)** 는 모델(Model)의 각 데이터 항목을 뷰(View)에서 어떻게 시각적으로 표현할지를 정의하는 QML 컴포넌트 템플릿입니다. 뷰(`ListView`, `GridView`, `TableView`, `PathView` 등)는 모델의 항목 수만큼 이 델리게이트 컴포넌트의 인스턴스를 (필요에 따라) 생성하여 화면에 표시합니다.

델리게이트는 모델 데이터와 UI 표현을 연결하는 핵심적인 역할을 수행하며, 모델-뷰 패턴의 유연성과 재사용성을 가능하게 합니다.

## 역할

*   **데이터 시각화**: 모델의 각 항목 데이터를 가져와 사용자 인터페이스 요소(텍스트, 이미지, 도형 등)로 변환하여 표시합니다.
*   **상호작용 처리**: 각 항목에 대한 사용자 입력(클릭, 터치 등)을 처리할 수 있습니다 (예: `MouseArea` 사용).
*   **상태 표현**: 모델 항목의 상태(예: 선택 여부, 현재 항목 여부)에 따라 시각적 표현을 다르게 할 수 있습니다.

## 사용 방법

델리게이트는 일반적으로 뷰 컴포넌트(`ListView`, `GridView` 등)의 `delegate` 프로퍼티에 `Component` 타입으로 정의됩니다.

```qml
import QtQuick
import QtQuick.Controls // TableView 예시용
import QtQml.Models // ListModel 임포트

// ListView 예시
Window { // 루트 요소 추가
    width: 200; height: 200
    visible: true
    title: "Delegate Example (ListView)"

    ListView {
        id: listView // ListView에 ID 추가
        // width: 200; height: 200 // 부모 크기 사용
        anchors.fill: parent
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
                width: listView.width // ID를 사용하여 ListView 너비 참조
                height: 40
                color: itemColor // 모델 역할(role) 직접 접근 (ListModel 사용 시)

                Text {
                    anchors.centerIn: parent
                    // model. 접두사로 역할 접근 또는 직접 접근
                    text: "Item " + index + ": " + model.itemText
                    color: "black" // 검은색으로 고정
                }

                // 각 항목 클릭 처리
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        // 클릭 시 현재 항목 인덱스를 ListView의 currentIndex로 설정 (ID 사용)
                        listView.currentIndex = index
                        console.log("Clicked on:", itemText, "at index", index)
                    }
                }

                // 현재 선택된 항목인지 여부에 따라 테두리 표시 (ID와 currentIndex 비교)
                border.color: listView.currentIndex === index ? "blue" : "transparent"
                border.width: listView.currentIndex === index ? 2 : 0
            }
        } // End of Component
    }
}
```

## 컨텍스트 프로퍼티 (Context Properties)

델리게이트 컴포넌트 내부에서는 뷰와 모델에 대한 정보에 접근할 수 있는 특별한 **컨텍스트 프로퍼티** 들이 제공됩니다. 이를 통해 모델 데이터와 뷰의 상태를 활용하여 델리게이트를 동적으로 구성할 수 있습니다.

주요 컨텍스트 프로퍼티는 뷰의 종류에 따라 약간의 차이가 있을 수 있습니다:

| 프로퍼티         | 타입        | 설명                                                                                                                                                                                                                            | 주요 사용 뷰                                        |
| :--------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------- |
| `index`          | `int`       | 현재 델리게이트 인스턴스가 나타내는 모델 항목의 인덱스 (0부터 시작).                                                                                                                                                                  | `ListView`, `GridView`, `PathView`                      |
| `model`          | `object`    | **(QtQuick Views)** `ListModel` 등에서 정의된 역할(role) 이름에 직접 접근할 수 있게 해주는 객체. `model.roleName` 형태로도 사용 가능.<br>**주의:** `TableView`의 셀 `delegate`에서는 이 방식으로 역할에 접근할 수 **없습니다**. 전체 모델 객체 자체를 참조합니다. | `ListView`, `GridView`, `PathView` (역할 접근용), `TableView` (모델 객체 접근용) |
| `modelData`      | `variant`   | 현재 항목의 기본 데이터 값. 모델 타입에 따라 의미가 다릅니다:<br><ul><li>단순 모델 (숫자, 리스트): 해당 인덱스의 값.</li><li>객체 모델: 해당 인덱스의 JavaScript 객체.</li><li>`ListModel`: 일반적으로 역할 이름으로 직접 접근하므로 잘 사용 안 함.</li><li>`TableView` 셀 `delegate`: **해당 셀의 데이터 값** (해당 `row`, `column`의 `role`에 해당하는 값).</li></ul> | 모든 뷰                                             |
| *역할 이름*      | `variant`   | **(ListModel 사용 시)** 모델에 정의된 각 역할(role) 이름. 델리게이트 내에서 해당 이름으로 직접 값에 접근할 수 있습니다 (예: `name`, `itemColor`).                                                                                          | `ListView`, `GridView`, `PathView`                      |
| `*.view`         | View 타입   | 부모 뷰 인스턴스에 접근 (`ListView.view`, `GridView.view`, `PathView.view`, `TableView.view`).                                                                                                                                     | 모든 뷰                                             |
| `*.isCurrentItem`| `bool`      | 현재 델리게이트가 뷰의 `currentItem`인지 여부 (`ListView.isCurrentItem`, `GridView.isCurrentItem`).                                                                                                                             | `ListView`, `GridView`                                |
| `PathView.onPath`| `bool`      | (PathView) 현재 델리게이트가 `pathItemCount`에 의해 실제로 경로 상에 배치되었는지 여부.                                                                                                                                            | `PathView`                                          |
| `PathView.percentage`| `real`  | (PathView) 현재 델리게이트가 경로 상 어느 지점인지 백분율(0.0 ~ 1.0).                                                                                                                                                              | `PathView`                                          |
| `PathView.position` | `real`  | (PathView) 현재 델리게이트가 경로 상 어느 지점인지 픽셀 단위 거리.                                                                                                                                                                | `PathView`                                          |
| `PathView.angle`   | `real`  | (PathView) 현재 델리게이트 위치에서의 경로 접선 각도 (도 단위).                                                                                                                                                                 | `PathView`                                          |
| `row`            | `int`       | **(TableView)** 현재 셀 또는 행의 인덱스 (`index`와 유사).                                                                                                                                                                     | `TableView` (delegate, rowDelegate)                 |
| `column`         | `int`       | **(TableView)** 현재 셀의 열 인덱스.                                                                                                                                                                                         | `TableView` (delegate, headerDelegate)              |
| `selected`       | `bool`      | **(TableView)** 현재 셀 또는 행이 선택되었는지 여부 (`selectionModel` 기준).                                                                                                                                                       | `TableView` (delegate, rowDelegate)                 |
| `current`        | `bool`      | **(TableView)** 현재 셀이 `TableView`의 `currentCell`인지 여부 (`currentRow` 및 `currentColumn`과 일치).                                                                                                                           | `TableView` (delegate)                              |

**참고:** `TableView`의 셀 델리게이트(`delegate`)에서는 모델의 역할 이름에 직접 접근할 수 없으므로, 셀 데이터를 표시하려면 `modelData`를 사용해야 합니다.

## 성능 고려사항

*   **델리게이트 경량화**: 델리게이트는 모델의 항목 수만큼 생성될 수 있으므로 가능한 한 가볍고 빠르게 로드되도록 작성해야 합니다. 복잡한 로직이나 많은 수의 시각적 아이템 포함은 스크롤 성능 저하의 주요 원인이 됩니다.
*   **아이템 재사용 (`reuseItems`)**: Qt 6.0부터 `ListView`, `GridView`는 기본적으로 화면 밖으로 나간 델리게이트 아이템을 재사용합니다 (`reuseItems: true`). 이는 메모리 사용량을 줄이고 성능을 크게 향상시킵니다. 델리게이트를 재사용할 때는 이전 상태가 남아있을 수 있으므로, 델리게이트가 새 데이터로 업데이트될 때 필요한 상태(예: `CheckBox`의 `checked` 상태)를 명시적으로 설정/초기화해야 할 수 있습니다.
*   **필요한 데이터만 로딩**: 델리게이트 내에서 필요한 모델 데이터만 사용하고, 불필요한 연산이나 복잡한 바인딩은 최소화합니다.

## 참고 사항

*   델리게이트는 `Component` 요소 안에 정의되어야 합니다.
*   `Component` 내부의 최상위 아이템이 각 모델 항목을 대표하는 시각적 요소가 됩니다.
*   컨텍스트 프로퍼티를 활용하여 모델 데이터와 뷰 상태에 따라 동적인 UI를 구성할 수 있습니다.
*   복잡한 델리게이트는 별도의 `.qml` 파일로 분리하여 재사용성과 가독성을 높일 수 있습니다. 이 경우 분리된 파일의 루트 아이템이 델리게이트 역할을 합니다.

## 관련 공식 문서

*   [ListView QML Type (Delegate Context)](https://doc.qt.io/qt-6/qml-qtquick-listview.html#delegate-context) (및 GridView, PathView)
*   [TableView QML Type (Delegate Context)](https://doc.qt.io/qt-6/qml-qtquick-controls-tableview.html#delegate-context)
*   [DelegateModel QML Type](https://doc.qt.io/qt-6/qml-qtqml-models-delegatemodel.html) (델리게이트 자체를 조작하는 모델)
*   [Qt Quick Controls - Delegates](https://doc.qt.io/qt-6/qtquickcontrols-delegates.html) (컨트롤에서 사용되는 델리게이트 패턴) 