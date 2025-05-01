# Image

`Image` 컴포넌트는 로컬 파일 시스템이나 네트워크에서 이미지를 로드하여 화면에 표시하는 데 사용됩니다.

## 모듈 정보

```qml
import QtQuick 2.15 // 또는 사용하는 Qt Quick 버전
```

## 개요

`Image` 요소는 `source` 프로퍼티에 지정된 URL로부터 이미지 데이터를 가져와 렌더링합니다. 다양한 이미지 형식(PNG, JPG, GIF, SVG 등)을 지원하며, 이미지 크기 조절 방식(`fillMode`), 비동기 로딩, 로딩 상태 표시, 캐싱 등 이미지 표시에 필요한 여러 기능을 제공합니다.

## 기반 클래스

`Item`

## 주요 프로퍼티

| 이름              | 타입                 | 기본값                       | 설명                                                                                                                                                                         |
| :---------------- | :------------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source`          | `url`                | `""`                       | 로드할 이미지의 URL(경로)입니다. 로컬 파일 경로(`"images/logo.png"`, `"file:///path/to/image.jpg"`), QRC 경로(`"qrc:/res/icon.svg"`), 또는 네트워크 URL(`"https://..."`)을 지정할 수 있습니다. |
| `fillMode`        | `enum`               | `Image.PreserveAspectFit`    | 이미지 크기가 `Image` 요소의 크기와 다를 때 이미지를 어떻게 조절할지 지정합니다. (`PreserveAspectFit`, `PreserveAspectCrop`, `Stretch`, `Tile`, `TileVertically`, `TileHorizontally`, `Pad`) |
| `status`          | `readonly enum`      | `Image.Null`                 | 이미지 로딩 상태를 나타내는 읽기 전용 프로퍼티입니다. (`Null`, `Ready`, `Loading`, `Error`)                                                                                |
| `progress`        | `readonly real`      | `0.0`                        | 이미지 다운로드 진행률 (0.0 ~ 1.0) 입니다. 네트워크 이미지 로딩 시에만 의미가 있습니다.                                                                                    |
| `sourceSize`      | `size`               | `Qt.size(0, 0)`              | 원본 이미지의 픽셀 크기입니다. 로딩이 완료되어야 유효한 값을 가집니다. SVG 이미지의 경우, 렌더링될 크기를 지정하는 데 사용될 수도 있습니다.                                                      |
| `paintedWidth`, `paintedHeight` | `readonly real` | (계산됨)                     | 실제로 화면에 그려진 이미지의 너비와 높이입니다. `fillMode` 설정에 따라 `width`, `height`와 다를 수 있습니다.                                                               |
| `smooth`          | `bool`               | `true`                       | 이미지를 확대/축소할 때 부드럽게 처리할지 여부입니다. 픽셀 아트 등에는 `false`로 설정하는 것이 좋을 수 있습니다.                                                                          |
| `mipmap`          | `bool`               | `false`                      | 밉맵(mipmap) 필터링 사용 여부입니다. 이미지 축소 시 품질을 향상시킬 수 있지만 메모리 사용량이 증가합니다.                                                                        |
| `asynchronous`    | `bool`               | `false`                      | 이미지를 비동기적으로 로드할지 여부입니다. `true`로 설정하면 이미지 로딩 중에도 UI 스레드가 멈추지 않아 반응성이 향상됩니다. 특히 네트워크 이미지나 큰 이미지에 유용합니다.                                |
| `cache`           | `bool`               | `true`                       | 이미지 로딩 시 캐시를 사용할지 여부입니다. `false`로 설정하면 항상 원본 소스에서 이미지를 다시 로드합니다.                                                                         |
| `mirror`          | `bool`               | `false`                      | 이미지를 수평으로 반전시킬지 여부입니다.                                                                                                                     |
| `autoTransform`   | `bool`               | `false`                      | 이미지 파일의 EXIF 정보 등에 포함된 방향(orientation) 정보를 자동으로 감지하여 이미지를 회전시킬지 여부입니다.                                                                      |

## 주요 시그널

| 이름            | 파라미터 | 반환타입 | 설명                                               |
| :-------------- | :------- | :------- | :----------------------------------------------- |
| `statusChanged` | -        | -        | `status` 프로퍼티 값이 변경될 때(예: 로딩 시작, 완료, 오류) 발생합니다. |
| `progressChanged`| -       | -        | `progress` 프로퍼티 값이 변경될 때 발생합니다.                       |

## 예제

```qml
import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15 // BusyIndicator 사용을 위해 추가

Window {
    width: 220 // GridLayout 열 2개와 spacing 고려
    height: 220 // GridLayout 행 2개와 spacing 고려
    visible: true
    title: "Image Examples"

    GridLayout {
        anchors.fill: parent
        anchors.margins: 10 // 보기 좋게 여백 추가
        columns: 2
        spacing: 10

        // 로컬 이미지 로드 (QRC 경로 예시)
        Image {
            // 참고: 아래 source는 예시 경로입니다.
            // 실제 이미지를 로드하려면 유효한 qrc 경로 또는 파일 경로로 변경해야 합니다.
            source: "qrc:/example/res/image/logo.png" // 실제 경로로 변경 필요!
            width: 100; height: 100
            fillMode: Image.PreserveAspectFit // 비율 유지하며 맞춤
            Text { // 이미지가 없을 경우를 대비한 안내 텍스트
                anchors.centerIn: parent
                text: "Local Image (placeholder)"
                visible: parent.status == Image.Error || parent.status == Image.Null
            }
        }

        // 네트워크 이미지 비동기 로드 및 로딩 상태 표시
        Item {
            width: 100; height: 100
            Image {
                id: networkImage
                anchors.fill: parent
                source: "https://picsum.photos/100" // 예시 URL
                asynchronous: true // 비동기 로딩 활성화
                fillMode: Image.Stretch // 영역 채우기
            }
            BusyIndicator { // 로딩 중 표시
                anchors.centerIn: parent
                running: networkImage.status === Image.Loading
            }
            Text { // 에러 시 표시
                anchors.centerIn: parent
                text: "Error"
                color: "red"
                visible: networkImage.status === Image.Error
            }
            Component.onCompleted: {
                console.log("Network image initial status:", networkImage.status)
            }
            Connections { // 상태 변경 시 로그 출력
                target: networkImage
                function onStatusChanged() { console.log("Network image status:", networkImage.status) }
            }
        }

        // 이미지 채우기 모드: PreserveAspectCrop
        Rectangle { // Clip 효과를 위해 Rectangle 사용
            width: 100; height: 100
            color: "lightgray"
            clip: true
            Image {
                anchors.centerIn: parent
                // 참고: 아래 source는 예시 경로입니다.
                source: "qrc:/example/res/image/landscape.jpg" // 실제 경로로 변경 필요!
                width: parent.width; height: parent.height
                fillMode: Image.PreserveAspectCrop // 비율 유지하며 영역 자르기
                Text { // 이미지가 없을 경우를 대비한 안내 텍스트
                    anchors.centerIn: parent
                    text: "Crop Image (placeholder)"
                    visible: parent.status == Image.Error || parent.status == Image.Null
                }
            }
        }

        // SVG 이미지 로드 (sourceSize 지정 권장, QRC 경로 예시)
        Image {
            // 참고: 아래 source는 예시 경로입니다.
            source: "qrc:/example/res/svg/qt_logo.svg" // 실제 경로로 변경 필요!
            sourceSize: Qt.size(100, 100) // SVG 렌더링 크기 지정
            width: 100; height: 100
            Text { // 이미지가 없을 경우를 대비한 안내 텍스트
                anchors.centerIn: parent
                text: "SVG Image (placeholder)"
                visible: parent.status == Image.Error || parent.status == Image.Null
            }
        }
    }
}
```

## 참고 사항

*   **경로**: `source`에 지정하는 경로는 QML 파일의 위치를 기준으로 하거나, `qrc:` (Qt Resource System), `file:` (로컬 파일 시스템 절대 경로), `http:`/`https:` (네트워크 URL) 등의 스킴을 사용할 수 있습니다.
*   **비동기 로딩**: 네트워크 이미지나 용량이 큰 로컬 이미지는 `asynchronous: true`로 설정하여 UI 멈춤 현상을 방지하는 것이 좋습니다. 로딩 중임을 나타내는 UI(예: `BusyIndicator`)를 함께 사용하는 것이 사용자 경험에 도움이 됩니다.
*   **SVG 지원**: QML은 SVG 이미지 렌더링을 지원합니다. `sourceSize`를 지정하여 원하는 크기로 SVG를 렌더링할 수 있습니다.
*   **메모리 관리**: 사용하지 않는 큰 이미지는 `source`를 빈 문자열(`""`)로 설정하여 메모리에서 해제하는 것을 고려할 수 있습니다.

## 공식 문서 링크

*   [Qt Quick Image QML Type](https://doc.qt.io/qt-6/qml-qtquick-image.html) 