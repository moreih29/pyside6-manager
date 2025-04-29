# BorderImage

`BorderImage`는 하나의 소스 이미지를 사용하여 크기 조절이 가능한 테두리와 배경을 그리는 QML 컴포넌트입니다. 이미지의 특정 영역을 테두리로 사용하고 나머지 영역을 배경으로 사용하여, 요소의 크기가 변경되더라도 테두리는 왜곡되지 않고 배경만 늘어나거나 반복되도록 할 수 있습니다.

## 모듈 정보

```qml
import QtQuick 2.15 // 또는 사용하는 Qt Quick 버전
```

## 개요

`BorderImage`는 소스 이미지를 9개의 영역(모서리 4개, 가로 테두리 2개, 세로 테두리 2개, 중앙 배경 1개)으로 나누어 처리합니다. `border` 프로퍼티 그룹을 통해 각 테두리 영역의 크기를 지정하면, `BorderImage` 요소의 크기가 변경될 때 다음과 같이 동작합니다:

*   **모서리 영역**: 원본 크기 그대로 유지됩니다.
*   **가로/세로 테두리 영역**: 지정된 `horizontalTileMode`와 `verticalTileMode`에 따라 늘어나거나(Stretch), 반복되거나(Repeat), 반올림하여 반복(Round)됩니다.
*   **중앙 배경 영역**: 지정된 `horizontalTileMode`와 `verticalTileMode`에 따라 늘어나거나, 반복되거나, 반올림하여 반복됩니다.

이 방식은 버튼, 프레임, 패널 등 다양한 크기로 사용될 수 있는 UI 요소의 배경과 테두리를 효율적으로 만드는 데 매우 유용합니다.

## 기반 클래스

`Item`

## 주요 프로퍼티

| 이름                  | 타입         | 기본값                       | 설명                                                                                                                                                                |
| :-------------------- | :----------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `source`              | `url`        | `""`                       | 테두리와 배경으로 사용할 소스 이미지의 URL입니다.                                                                                                                     |
| `border`              | `QtObject`   | (테두리 객체)              | 소스 이미지에서 각 테두리 영역의 크기(픽셀 단위)를 지정하는 그룹 객체입니다. 하위 프로퍼티로 `left`, `right`, `top`, `bottom`을 가집니다.                                                             |
| `horizontalTileMode`  | `enum`       | `BorderImage.Stretch`        | 수평 방향 테두리 및 배경 영역의 타일링(반복/늘리기) 모드를 지정합니다. (`Stretch`, `Repeat`, `Round`)                                                                       |
| `verticalTileMode`    | `enum`       | `BorderImage.Stretch`        | 수직 방향 테두리 및 배경 영역의 타일링 모드를 지정합니다. (`Stretch`, `Repeat`, `Round`)                                                                              |
| `status`              | `readonly enum`| `Image.Null`                 | 이미지 로딩 상태입니다. (`Null`, `Ready`, `Loading`, `Error`)                                                                                                       |
| `progress`            | `readonly real`| `0.0`                        | 이미지 다운로드 진행률 (0.0 ~ 1.0) 입니다.                                                                                                                        |
| `smooth`, `mipmap`, `asynchronous`, `cache` | `bool`    | (`Image` 기본값과 동일)   | `Image` 요소와 동일한 의미의 프로퍼티들입니다.                                                                                                                          |

**`border` 객체 하위 프로퍼티:**

| 이름     | 타입    | 기본값 | 설명                                                              |
| :------- | :------ | :----- | :---------------------------------------------------------------- |
| `left`   | `int`   | `0`    | 소스 이미지 왼쪽에서 테두리로 사용할 영역의 너비(픽셀)입니다.                   |
| `right`  | `int`   | `0`    | 소스 이미지 오른쪽에서 테두리로 사용할 영역의 너비(픽셀)입니다.                 |
| `top`    | `int`   | `0`    | 소스 이미지 위쪽에서 테두리로 사용할 영역의 높이(픽셀)입니다.                   |
| `bottom` | `int`   | `0`    | 소스 이미지 아래쪽에서 테두리로 사용할 영역의 높이(픽셀)입니다.                 |

## 주요 시그널

| 이름            | 파라미터 | 반환타입 | 설명                                       |
| :-------------- | :------- | :------- | :--------------------------------------- |
| `statusChanged` | -        | -        | `status` 프로퍼티 값이 변경될 때 발생합니다.       |
| `progressChanged`| -       | -        | `progress` 프로퍼티 값이 변경될 때 발생합니다.   |

## 예제

다음은 30x30 픽셀 크기의 소스 이미지를 사용하여 크기가 다른 버튼 모양을 만드는 예제입니다. 소스 이미지(`button_border.png`)는 각 테두리가 10픽셀이라고 가정합니다.

```qml
import QtQuick 2.15
import QtQuick.Layouts 1.15

RowLayout {
    spacing: 10

    // 소스 이미지 (가정: 30x30 크기, 각 테두리 10px)
    Image { 
        source: "qrc:/images/button_border.png" // 실제 경로로 변경 필요
        width: 30; height: 30
        visible: false // 화면에 직접 표시하지 않음
    }

    // 작은 크기 버튼
    BorderImage {
        width: 80; height: 40
        source: "qrc:/images/button_border.png"
        border { left: 10; top: 10; right: 10; bottom: 10 } // 각 테두리 영역 10px 지정
        // 기본값: Stretch 모드
        
        Text { 
            text: "Small"
            anchors.centerIn: parent
        }
    }

    // 큰 크기 버튼 (테두리는 늘어나지 않고 배경만 늘어남)
    BorderImage {
        width: 150; height: 50
        source: "qrc:/images/button_border.png"
        border { left: 10; top: 10; right: 10; bottom: 10 }
        
        Text { 
            text: "Large (Stretch)"
            anchors.centerIn: parent
        }
    }
    
    // 반복 모드 버튼
    BorderImage {
        width: 200; height: 60
        source: "qrc:/images/button_border.png"
        border { left: 10; top: 10; right: 10; bottom: 10 }
        horizontalTileMode: BorderImage.Repeat // 수평 반복
        verticalTileMode: BorderImage.Repeat   // 수직 반복
        
        Text { 
            text: "Large (Repeat)"
            anchors.centerIn: parent
        }
    }
}
```

## 참고 사항

*   **소스 이미지 준비**: `BorderImage`를 효과적으로 사용하려면 9개 영역으로 나누기 적합한 소스 이미지를 미리 준비해야 합니다. 각 모서리, 테두리, 배경 영역이 명확하게 구분되는 이미지가 좋습니다.
*   **`border` 값 설정**: `border`의 `left`, `right`, `top`, `bottom` 값은 소스 이미지 기준의 픽셀 크기입니다. 이 값을 정확하게 설정해야 원하는 결과를 얻을 수 있습니다.
*   **Tile Mode**: `horizontalTileMode`와 `verticalTileMode`를 조절하여 테두리와 배경이 늘어나는 방식(`Stretch`), 반복되는 방식(`Repeat`), 또는 픽셀 경계에 맞춰 반복되는 방식(`Round`)을 선택할 수 있습니다. 