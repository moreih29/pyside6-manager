# Rectangle

`Rectangle`은 화면에 사각형을 그리는 가장 기본적인 QML 컴포넌트입니다. 단색 또는 그라데이션으로 채울 수 있으며, 테두리와 둥근 모서리를 설정할 수 있습니다.

## 모듈 정보

```qml
import QtQuick 2.15 // 또는 사용하는 Qt Quick 버전
```

## 개요

`Rectangle`은 `Item`을 상속받아 위치(`x`, `y`), 크기(`width`, `height`) 등의 기본 속성을 가지며, 추가적으로 사각형의 시각적 표현을 제어하는 프로퍼티들을 제공합니다. 배경색, 테두리 스타일, 모서리 둥글기 등을 설정하여 다양한 UI 요소(버튼 배경, 컨테이너 영역, 구분선 등)의 기초로 활용됩니다.

## 기반 클래스

`Item`

## 주요 프로퍼티

| 이름     | 타입         | 기본값                 | 설명                                                                                                                               |
| :------- | :----------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `color`  | `color`      | `"white"`             | 사각형을 채우는 색상입니다. `transparent`로 설정하여 테두리만 있는 사각형을 만들 수도 있습니다.                                                                 |
| `radius` | `real`       | `0`                    | 모든 모서리의 둥글기 반경(radius)입니다. 값이 클수록 모서리가 더 둥글어집니다. 너비/높이의 절반 이상이면 원이나 타원에 가까워집니다.                                           |
| `border` | `QtObject`   | (테두리 객체)          | 사각형 테두리 속성을 관리하는 객체입니다. 하위 프로퍼티로 `width` (두께), `color` (색상) 등을 가집니다.                                                               |
| `gradient`| `Gradient` 또는 `list<GradientStop>` | `null` | 사각형을 채우는 그라데이션 효과를 정의합니다. `Gradient` 객체를 직접 할당하거나, `GradientStop` 객체 리스트를 할당하여 간단한 선형 그라데이션을 만들 수 있습니다. `color` 프로퍼티와 동시에 사용되지 않습니다. |

**`border` 객체 하위 프로퍼티:**

| 이름    | 타입    | 기본값        | 설명                 |
| :------ | :------ | :------------ | :------------------- |
| `width` | `int`   | `1`           | 테두리 선의 두께입니다.   |
| `color` | `color` | `"black"`   | 테두리 선의 색상입니다.   |

**`Gradient` 객체 (예시):**

```qml
Rectangle {
    gradient: Gradient {
        GradientStop { position: 0.0; color: "lightblue" }
        GradientStop { position: 1.0; color: "darkblue" }
    }
}
// 위 코드는 아래 리스트 방식과 동일 (수직 선형 그라데이션)
Rectangle {
    gradient: [ 
        GradientStop { position: 0.0; color: "lightblue" },
        GradientStop { position: 1.0; color: "darkblue" }
    ]
}
```

## 주요 시그널

주로 `Item`으로부터 상속받은 `<propertyName>Changed` 시그널(예: `colorChanged`, `widthChanged` 등)을 사용합니다. `Rectangle` 자체의 고유 시그널은 일반적으로 사용되지 않습니다.

## 예제

```qml
import QtQuick 2.15
import QtQuick.Layouts 1.15

RowLayout {
    spacing: 10

    // 기본 파란색 사각형
    Rectangle {
        width: 80; height: 80
        color: "blue"
    }
    
    // 둥근 모서리와 두꺼운 검은 테두리
    Rectangle {
        width: 80; height: 80
        color: "lightgreen"
        radius: 10
        border.width: 3
        border.color: "black"
    }
    
    // 투명 배경, 빨간 테두리만 있는 사각형
    Rectangle {
        width: 80; height: 80
        color: "transparent"
        border.color: "red"
        border.width: 2
    }
    
    // 수평 그라데이션 (Gradient 객체 사용)
    Rectangle {
        width: 120; height: 80
        gradient: Gradient {
            orientation: Gradient.Horizontal // 수평 방향 설정
            GradientStop { position: 0.0; color: "yellow" }
            GradientStop { position: 0.5; color: "orange" }
            GradientStop { position: 1.0; color: "red" }
        }
        radius: 5
    }
}
```

## 참고 사항

*   **기본 블록**: `Rectangle`은 QML UI 디자인에서 가장 기본적이고 자주 사용되는 시각적 요소 중 하나입니다.
*   **컨테이너 역할**: 다른 아이템들을 담는 배경이나 컨테이너로 흔히 사용됩니다.
*   **`radius`와 테두리**: `radius` 값이 설정되면 테두리도 둥글게 처리됩니다.
*   **성능**: 간단한 사각형은 매우 효율적으로 렌더링됩니다. 하지만 매우 많은 `Rectangle`을 사용하거나 복잡한 `gradient`를 적용하면 성능에 영향을 줄 수 있습니다. 