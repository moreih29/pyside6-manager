# 유틸리티 및 도우미 컴포넌트 (Utility Components)

FluentUI는 개발을 보다 효율적으로 할 수 있도록 다양한 유틸리티 및 도우미 컴포넌트를 제공합니다. 이 문서에서는 각 컴포넌트의 주요 속성과 사용 예제를 설명합니다.

## 테마 (FluTheme)

애플리케이션의 테마를 관리하는 싱글톤 객체입니다.

### 주요 속성
- `dark`: 다크 모드 여부
- `darkMode`: 다크 모드 설정 (FluThemeType.DarkMode.Auto, Light, Dark, System)
- `primaryColor`: 주요 색상
- `backgroundColor`: 배경 색상
- `dividerColor`: 구분선 색상
- `fontPrimaryColor`: 주요 폰트 색상
- `fontSecondaryColor`: 보조 폰트 색상
- `fontTertiaryColor`: 세 번째 폰트 색상
- `itemNormalColor`: 항목 일반 색상
- `itemHoverColor`: 항목 호버 색상
- `itemPressColor`: 항목 누름 색상
- `animationEnabled`: 애니메이션 활성화 여부

### 사용 예제
```qml
import FluentUI

FluWindow {
    id: window
    width: 800
    height: 600
    title: "테마 예제"
    
    Column {
        anchors.centerIn: parent
        spacing: 20
        
        FluText {
            text: "현재 테마: " + (FluTheme.dark ? "다크" : "라이트")
            font.pixelSize: 16
        }
        
        FluToggleSwitch {
            text: "다크 모드"
            checked: FluTheme.dark
            onClicked: {
                FluTheme.darkMode = checked ? FluThemeType.DarkMode.Dark : FluThemeType.DarkMode.Light
            }
        }
        
        FluFilledButton {
            text: "시스템 테마 사용"
            onClicked: {
                FluTheme.darkMode = FluThemeType.DarkMode.System
            }
        }
    }
}
```

## 색상 (FluColors)

FluentUI의 색상 팔레트를 제공하는 클래스입니다.

### 주요 속성
- 다양한 색상 값 제공: Yellow, Orange, Red, Magenta, Purple, Blue, Teal, Green 등
- 각 색상은 기본, 라이트, 다크 변형 제공

### 사용 예제
```qml
import FluentUI

Grid {
    columns: 3
    spacing: 10
    
    Repeater {
        model: ["Yellow", "Orange", "Red", "Magenta", "Purple", "Blue", "Teal", "Green"]
        Rectangle {
            width: 100
            height: 100
            color: FluColors[modelData]
            
            FluText {
                anchors.centerIn: parent
                text: modelData
                color: "white"
            }
        }
    }
}
```

## 아이콘 (FluIcon / FluentIcons)

FluentUI 아이콘을 표시하는 컴포넌트입니다.

### 주요 속성
- `iconSource`: 아이콘 소스 (FluentIcons 열거형 사용)
- `iconSize`: 아이콘 크기
- `iconColor`: 아이콘 색상
- `horizontalAlignment`: 수평 정렬
- `verticalAlignment`: 수직 정렬

### 사용 예제
```qml
import FluentUI

Grid {
    columns: 4
    spacing: 10
    
    FluIcon {
        iconSource: FluentIcons.Home
        iconSize: 24
        iconColor: FluTheme.dark ? "white" : "black"
    }
    
    FluIcon {
        iconSource: FluentIcons.Settings
        iconSize: 24
        iconColor: FluTheme.dark ? "white" : "black"
    }
    
    FluIcon {
        iconSource: FluentIcons.Save
        iconSize: 24
        iconColor: FluTheme.primaryColor
    }
    
    FluIcon {
        iconSource: FluentIcons.Download
        iconSize: 24
        iconColor: FluColors.Blue
    }
}
```

## 텍스트 (FluText)

텍스트를 표시하는 컴포넌트입니다.

### 주요 속성
- `text`: 표시할 텍스트
- `font`: 폰트
- `color`: 텍스트 색상

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 10
    
    FluText {
        text: "기본 텍스트"
    }
    
    FluText {
        text: "커스텀 폰트 텍스트"
        font: FluTextStyle.Subtitle
    }
    
    FluText {
        text: "색상이 있는 텍스트"
        color: FluColors.Blue
    }
}
```

## 텍스트 스타일 (FluTextStyle)

FluentUI의 텍스트 스타일을 제공하는 싱글톤입니다.

### 주요 속성
- `Caption`: 작은 캡션 텍스트
- `Body`: 본문 텍스트
- `BodyStrong`: 강조된 본문 텍스트
- `Subtitle`: 부제목 텍스트
- `Title`: 제목 텍스트
- `TitleLarge`: 큰 제목 텍스트
- `Display`: 디스플레이 텍스트

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 15
    
    FluText {
        text: "Caption 스타일"
        font: FluTextStyle.Caption
    }
    
    FluText {
        text: "Body 스타일"
        font: FluTextStyle.Body
    }
    
    FluText {
        text: "BodyStrong 스타일"
        font: FluTextStyle.BodyStrong
    }
    
    FluText {
        text: "Subtitle 스타일"
        font: FluTextStyle.Subtitle
    }
    
    FluText {
        text: "Title 스타일"
        font: FluTextStyle.Title
    }
    
    FluText {
        text: "TitleLarge 스타일"
        font: FluTextStyle.TitleLarge
    }
    
    FluText {
        text: "Display 스타일"
        font: FluTextStyle.Display
    }
}
```

## 툴 (FluTools)

다양한 유틸리티 함수를 제공하는 유틸리티 클래스입니다.

### 주요 메서드
- `isMobile()`: 모바일 환경인지 확인
- `getJapaneseLunarDate()`: 일본 음력 날짜 반환
- `getChineseLunarDate()`: 중국 음력 날짜 반환
- `getCurrentWeek()`: 현재 주 반환
- `uuid()`: UUID 생성
- `isWin()`: Windows 환경인지 확인
- `isMacos()`: macOS 환경인지 확인
- `isLinux()`: Linux 환경인지 확인
- `formatTime()`: 시간 형식 변환
- `getFileNameWithSuffix()`: 확장자가 포함된 파일 이름 반환

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 10
    
    FluText {
        text: "현재 플랫폼: " + (FluTools.isWin() ? "Windows" : FluTools.isMacos() ? "macOS" : FluTools.isLinux() ? "Linux" : "Unknown")
    }
    
    FluText {
        text: "UUID: " + FluTools.uuid()
    }
    
    FluText {
        text: "현재 시간: " + FluTools.formatTime(new Date(), "yyyy-MM-dd hh:mm:ss")
    }
}
```

## 로더 (FluLoader)

동적으로 컴포넌트를 로드하는 컴포넌트입니다.

### 주요 속성
- `source`: 로드할 소스 URL

### 사용 예제
```qml
import FluentUI

FluLoader {
    width: 300
    height: 200
    source: "CustomComponent.qml"
}
```

## 원격 로더 (FluRemoteLoader)

원격 URL에서 QML을 동적으로 로드하는 컴포넌트입니다.

### 주요 속성
- `source`: 로드할 소스 URL
- `loading`: 로딩 중 여부
- `errorText`: 오류 텍스트

### 사용 예제
```qml
import FluentUI

FluRemoteLoader {
    width: 400
    height: 300
    source: "https://example.com/component.qml"
    onLoaded: {
        console.log("원격 컴포넌트가 로드되었습니다")
    }
    onError: function(errorString) {
        console.error("로드 오류: " + errorString)
    }
}
```

## 이벤트 버스 (FluEventBus)

컴포넌트 간 이벤트 통신을 위한 이벤트 버스 컴포넌트입니다.

### 주요 메서드
- `registerEvent(name, callback)`: 이벤트 등록
- `unregisterEvent(name)`: 이벤트 해제
- `post(name, data)`: 이벤트 발생

### 사용 예제
```qml
import FluentUI

// 이벤트 버스 싱글톤 정의
Item {
    id: root
    
    property var eventBus: FluEventBus {}
    
    Component.onCompleted: {
        // 이벤트 등록
        eventBus.registerEvent("customEvent", function(data) {
            console.log("이벤트 수신: " + data)
        })
    }
    
    Component.onDestruction: {
        // 이벤트 해제
        eventBus.unregisterEvent("customEvent")
    }
    
    // 이벤트 발생 예제
    FluButton {
        text: "이벤트 발생"
        onClicked: {
            root.eventBus.post("customEvent", "안녕하세요!")
        }
    }
}
```

## 이미지 (FluImage)

이미지를 표시하는 컴포넌트입니다.

### 주요 속성
- `source`: 이미지 소스 URL
- `fillMode`: 채우기 모드
- `asynchronous`: 비동기 로드 여부
- `radius`: 테두리 반경

### 사용 예제
```qml
import FluentUI

FluImage {
    width: 200
    height: 150
    source: "qrc:/images/example.jpg"
    fillMode: Image.PreserveAspectCrop
    radius: 8
}
```

## 아크릴 효과 (FluAcrylic)

아크릴(반투명) 효과를 적용하는 컴포넌트입니다.

### 주요 속성
- `source`: 효과를 적용할 소스
- `tintColor`: 틴트 색상
- `tintOpacity`: 틴트 불투명도
- `noiseOpacity`: 노이즈 불투명도
- `radius`: 블러 반경

### 사용 예제
```qml
import FluentUI

Rectangle {
    width: 800
    height: 600
    
    Image {
        anchors.fill: parent
        source: "qrc:/images/background.jpg"
        fillMode: Image.PreserveAspectCrop
    }
    
    FluAcrylic {
        width: 300
        height: 200
        anchors.centerIn: parent
        source: Image { source: "qrc:/images/background.jpg" }
        tintColor: FluTheme.dark ? Qt.rgba(0, 0, 0, 1) : Qt.rgba(1, 1, 1, 1)
        tintOpacity: 0.8
        noiseOpacity: 0.03
        radius: 30
        
        FluText {
            anchors.centerIn: parent
            text: "아크릴 효과 예제"
            font: FluTextStyle.Title
        }
    }
}
```

## QR 코드 (FluQRCode)

QR 코드를 생성하고 표시하는 컴포넌트입니다.

### 주요 속성
- `text`: QR 코드로 변환할 텍스트
- `color`: QR 코드 색상
- `margin`: 여백

### 사용 예제
```qml
import FluentUI

FluQRCode {
    width: 200
    height: 200
    text: "https://example.com"
    color: FluTheme.dark ? "white" : "black"
    margin: 2
}
```

## 포커스 직사각형 (FluFocusRectangle)

키보드 포커스를 시각적으로 표시하는 컴포넌트입니다.

### 주요 속성
- `visible`: 표시 여부
- `radius`: 테두리 반경
- `color`: 테두리 색상

### 사용 예제
```qml
import FluentUI

FluButton {
    id: button
    text: "포커스 직사각형 예제"
    
    FluFocusRectangle {
        visible: button.activeFocus
        radius: 5
        anchors.fill: parent
    }
}
```

## 복사 가능한 텍스트 (FluCopyableText)

클릭 시 텍스트를 클립보드에 복사할 수 있는 텍스트 컴포넌트입니다.

### 주요 속성
- `text`: 표시 및 복사할 텍스트
- `tipText`: 툴팁 텍스트
- `showCopyIcon`: 복사 아이콘 표시 여부
- `color`: 텍스트 색상

### 사용 예제
```qml
import FluentUI

FluCopyableText {
    text: "복사 가능한 텍스트입니다. 클릭하여 복사하세요."
    tipText: "클립보드에 복사되었습니다!"
    showCopyIcon: true
    color: FluColors.Blue
}
```

## 그림자 (FluShadow)

요소에 그림자 효과를 추가하는 컴포넌트입니다.

### 주요 속성
- `radius`: 그림자 반경
- `color`: 그림자 색상
- `offsetX`: X축 오프셋
- `offsetY`: Y축 오프셋

### 사용 예제
```qml
import FluentUI

Rectangle {
    width: 200
    height: 100
    color: FluTheme.dark ? "#3c3c3c" : "white"
    radius: 5
    
    FluShadow {
        radius: 40
        color: Qt.rgba(0, 0, 0, 0.2)
        offsetX: 0
        offsetY: 10
    }
    
    FluText {
        anchors.centerIn: parent
        text: "그림자 효과"
    }
}
```

## 클립 (FluClip)

내용을 지정된 형태로 클리핑하는 컴포넌트입니다.

### 주요 속성
- `radius`: 테두리 반경

### 사용 예제
```qml
import FluentUI

FluClip {
    width: 150
    height: 150
    radius: 75
    
    Image {
        width: parent.width
        height: parent.height
        source: "qrc:/images/profile.jpg"
        fillMode: Image.PreserveAspectCrop
    }
}
``` 