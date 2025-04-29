# StackLayout

**모듈:** `import QtQuick.Layouts`

## 개요

`StackLayout`은 자식 아이템들을 카드 덱처럼 겹쳐 쌓는 레이아웃입니다. 한 번에 하나의 아이템만 보이며, `currentIndex` 프로퍼티를 사용하여 현재 보이는 아이템을 제어합니다. 주로 탭 위젯, 설정 페이지, 마법사(Wizard) 인터페이스 등 여러 페이지나 뷰를 전환하며 보여줘야 하는 경우에 유용하게 사용됩니다.

`StackLayout` 내의 모든 자식 아이템들은 기본적으로 레이아웃의 전체 크기를 차지하도록 크기가 조절됩니다. `Layout` Attached Properties는 `StackLayout`의 자식에게는 일반적으로 적용되지 않지만, `StackLayout` 자체를 다른 레이아웃 안에 배치할 때는 사용할 수 있습니다.

## 주요 프로퍼티

| 이름          | 타입       | 기본값 | 설명                                                               | 
| :------------ | :--------- | :----- | :----------------------------------------------------------------- |
| `count`       | `int`      | -      | (읽기 전용) 레이아웃에 포함된 아이템의 총 개수.                   | 
| `currentIndex`| `int`      | 0      | 현재 화면에 보이는 자식 아이템의 인덱스.                           | 
| `currentItem` | `Item`     | -      | (읽기 전용) 현재 화면에 보이는 자식 아이템 객체.                   | 

## 주요 시그널

| 이름               | 파라미터 | 반환타입 | 설명                                        | 
| :----------------- | :------- | :------- | :------------------------------------------ |
| `currentIndexChanged` | -        | -        | `currentIndex` 값이 변경될 때 발생하는 시그널. | 

## 예제

```qml
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls // Buttons for example

Window {
    width: 300
    height: 200
    visible: true
    title: "StackLayout Example"

    ColumnLayout { // 전체 구조를 위한 ColumnLayout
        anchors.fill: parent
        spacing: 5

        StackLayout {
            id: stackLayout
            Layout.fillWidth: true
            Layout.fillHeight: true // 사용 가능한 높이를 채움
            currentIndex: 0 // 첫 번째 아이템을 처음에 표시

            Rectangle {
                color: "lightblue"
                Text { anchors.centerIn: parent; text: "Page 1" }
            }
            Rectangle {
                color: "lightgreen"
                Text { anchors.centerIn: parent; text: "Page 2" }
            }
            Rectangle {
                color: "lightcoral"
                Text { anchors.centerIn: parent; text: "Page 3" }
            }
        }

        RowLayout { // 페이지 전환 버튼 영역
            Layout.alignment: Qt.AlignCenter // 버튼들을 중앙 정렬
            spacing: 10

            Button {
                text: "Previous"
                enabled: stackLayout.currentIndex > 0
                onClicked: stackLayout.currentIndex--
            }
            Button {
                text: "Next"
                enabled: stackLayout.currentIndex < stackLayout.count - 1
                onClicked: stackLayout.currentIndex++
            }
        }
    }
}
```

## 참고 사항

*   `StackLayout`의 자식 아이템들은 보통 `visible` 프로퍼티를 직접 제어하지 않습니다. 레이아웃이 `currentIndex`에 따라 자동으로 아이템의 표시 여부를 관리합니다.
*   `StackLayout`에 동적으로 아이템을 추가하거나 제거할 수 있습니다. 이때 `count`와 `currentIndex`가 적절히 업데이트됩니다.
*   애니메이션 효과와 함께 페이지 전환을 구현하려면 `SwipeView` (QtQuick.Controls) 또는 상태(States) 및 트랜지션(Transitions)을 사용하는 것을 고려할 수 있습니다. 