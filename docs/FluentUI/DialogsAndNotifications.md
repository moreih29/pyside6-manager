# 다이얼로그 및 알림 컴포넌트 (Dialogs and Notifications)

FluentUI는 사용자와의 상호작용을 위한 다양한 다이얼로그와 알림 컴포넌트를 제공합니다. 이 문서에서는 각 컴포넌트의 주요 속성과 사용 예제를 설명합니다.

## 콘텐츠 다이얼로그 (FluContentDialog)

커스텀 내용을 표시할 수 있는 다이얼로그 컴포넌트입니다.

### 주요 속성
- `title`: 다이얼로그 제목
- `message`: 다이얼로그 메시지
- `buttonFlags`: 버튼 플래그 (FluContentDialogType.NegativeButton, PositiveButton, NeutralButton)
- `negativeText`: 부정 버튼 텍스트 (기본값: "취소")
- `positiveText`: 긍정 버튼 텍스트 (기본값: "확인")
- `neutralText`: 중립 버튼 텍스트 (기본값: "적용")
- `contentDelegate`: 커스텀 컨텐츠를 위한 delegate (Component 타입)
- `darkMode`: 다크 모드 여부

### 신호 (Signals)
- `negativeClicked`: 부정 버튼 클릭 시 발생
- `positiveClicked`: 긍정 버튼 클릭 시 발생
- `neutralClicked`: 중립 버튼 클릭 시 발생

### 사용 예제 - 두 개 버튼 다이얼로그
```qml
import QtQuick
import FluentUI

FluContentDialog {
    id: dialog
    title: qsTr("Friendly Reminder")
    message: qsTr("Are you sure you want to opt out?")
    buttonFlags: FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
    negativeText: qsTr("Cancel")
    positiveText: qsTr("OK")
    
    onNegativeClicked: {
        console.log("Cancel 버튼 클릭됨")
    }
    
    onPositiveClicked: {
        console.log("OK 버튼 클릭됨")
    }
}

// 다이얼로그 표시
FluButton {
    text: qsTr("Show Double Button Dialog")
    onClicked: dialog.open()
}
```

### 사용 예제 - 세 개 버튼 다이얼로그
```qml
import QtQuick
import FluentUI

FluContentDialog {
    id: dialog
    title: qsTr("Friendly Reminder")
    message: qsTr("Are you sure you want to opt out?")
    buttonFlags: FluContentDialogType.NeutralButton | FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
    negativeText: qsTr("Cancel")
    positiveText: qsTr("OK")
    neutralText: qsTr("Minimize")
    
    onNegativeClicked: {
        console.log("Cancel 버튼 클릭됨")
    }
    
    onPositiveClicked: {
        console.log("OK 버튼 클릭됨")
    }
    
    onNeutralClicked: {
        console.log("Minimize 버튼 클릭됨")
    }
}

// 다이얼로그 표시
FluButton {
    text: qsTr("Show Triple Button Dialog")
    onClicked: dialog.open()
}
```

### 사용 예제 - 커스텀 콘텐츠 다이얼로그
```qml
import QtQuick
import FluentUI

FluContentDialog {
    id: dialog
    title: qsTr("Friendly Reminder")
    message: qsTr("Data is loading, please wait...")
    buttonFlags: FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
    negativeText: qsTr("Unload")
    positiveText: qsTr("OK")
    
    contentDelegate: Component {
        Item {
            implicitWidth: parent.width
            implicitHeight: 80
            
            FluProgressRing {
                anchors.centerIn: parent
            }
        }
    }
    
    onNegativeClicked: {
        console.log("Unload 버튼 클릭됨")
    }
    
    onPositiveClicked: {
        console.log("OK 버튼 클릭됨")
    }
}

// 다이얼로그 표시
FluButton {
    text: qsTr("Custom Content Dialog")
    onClicked: dialog.open()
}
```

## 정보 표시줄 (FluInfoBar)

간단한 정보, 경고, 오류 등을 표시하는 컴포넌트입니다. FluentUI는 전역 함수로 여러 타입의 정보 표시줄을 손쉽게 표시할 수 있도록 도와줍니다.

### 전역 함수
- `showInfo(message, duration, actionButtonText)`: 정보 메시지 표시
- `showWarning(message, duration, actionButtonText)`: 경고 메시지 표시
- `showError(message, duration, actionButtonText)`: 오류 메시지 표시
- `showSuccess(message, duration, actionButtonText)`: 성공 메시지 표시
- `showLoading()`: 로딩 메시지 표시
- `clearAllInfo()`: 모든 정보 메시지 닫기

### 매개변수
- `message`: 표시할 메시지
- `duration`: 표시 시간(밀리초, 0: 수동으로 닫을 때까지 표시)
- `actionButtonText`: 액션 버튼에 표시될 텍스트

### 사용 예제 - 기본 정보 표시
```qml
import QtQuick
import FluentUI

Column {
    spacing: 10
    
    FluButton {
        text: qsTr("Info")
        onClicked: {
            showInfo(qsTr("This is an InfoBar in the Info Style"))
        }
    }
    
    FluButton {
        text: qsTr("Warning")
        onClicked: {
            showWarning(qsTr("This is an InfoBar in the Warning Style"))
        }
    }
    
    FluButton {
        text: qsTr("Error")
        onClicked: {
            showError(qsTr("This is an InfoBar in the Error Style"))
        }
    }
    
    FluButton {
        text: qsTr("Success")
        onClicked: {
            showSuccess(qsTr("This is an InfoBar in the Success Style"))
        }
    }
}
```

### 사용 예제 - 수동으로 닫는 정보 표시
```qml
import QtQuick
import FluentUI

Item {
    property var info1
    
    Column {
        spacing: 10
        
        FluButton {
            text: qsTr("InfoBar that needs to be turned off manually")
            onClicked: {
                showInfo(qsTr("This is an InfoBar in the Info Style"), 0, qsTr("Manual shutdown is supported"))
            }
        }
        
        Row {
            spacing: 5
            
            FluButton {
                text: (info1 ? qsTr("close '%1'") : qsTr("show '%1")).arg("info1")
                onClicked: {
                    if (info1) {
                        info1.close()
                        info1 = null
                        return
                    }
                    info1 = showInfo(qsTr("This is an '%1'").arg("info1"), 0)
                }
            }
            
            FluButton {
                text: qsTr("clear all info")
                onClicked: {
                    clearAllInfo()
                }
            }
        }
    }
}
```

## 시트 (FluSheet)

화면 다양한 방향에서 슬라이드되는 시트 형태의 다이얼로그입니다.

### 주요 속성
- `title`: 시트 제목
- `contentWidth`: 내용 너비
- `contentHeight`: 내용 높이
- `coverWidth`: 커버 너비
- `coverHeight`: 커버 높이
- `coverRadius`: 커버 테두리 반경

### 메서드
- `open(type)`: 시트를 지정된 방향(FluSheetType.Top, Right, Bottom, Left)에서 열기

### 사용 예제
```qml
import QtQuick
import FluentUI

Item {
    FluSheet {
        id: sheet
        title: qsTr("Title")
        
        FluText {
            text: qsTr("Some contents...\nSome contents...\nSome contents...")
            anchors {
                left: parent.left
                leftMargin: 10
            }
        }
    }
    
    Column {
        spacing: 10
        
        Row {
            spacing: 10
            
            FluButton {
                width: 80
                height: 30
                text: qsTr("top")
                onClicked: {
                    sheet.open(FluSheetType.Top)
                }
            }
            
            FluButton {
                width: 80
                height: 30
                text: qsTr("right")
                onClicked: {
                    sheet.open(FluSheetType.Right)
                }
            }
        }
        
        Row {
            spacing: 10
            
            FluButton {
                width: 80
                height: 30
                text: qsTr("bottom")
                onClicked: {
                    sheet.open(FluSheetType.Bottom)
                }
            }
            
            FluButton {
                width: 80
                height: 30
                text: qsTr("left")
                onClicked: {
                    sheet.open(FluSheetType.Left)
                }
            }
        }
    }
}
```

## 팝업 (FluPopup)

커스텀 내용을 팝업으로 표시하는 컴포넌트입니다.

### 주요 속성
- `closePolicy`: 닫기 정책
- `contentWidth`: 내용 너비
- `contentHeight`: 내용 높이
- `blurSource`: 블러 효과 소스
- `blurRadius`: 블러 효과 반경
- `blurVisible`: 블러 효과 표시 여부
- `backgroundVisible`: 배경 표시 여부

### 사용 예제
```qml
import QtQuick
import FluentUI

FluPopup {
    id: popup
    backgroundVisible: true
    contentWidth: 300
    contentHeight: 200
    
    // 팝업 내용
    Rectangle {
        anchors.fill: parent
        color: FluTheme.dark ? Qt.rgba(50/255,50/255,50/255,1) : Qt.rgba(240/255,240/255,240/255,1)
        radius: 5
        
        FluText {
            anchors.centerIn: parent
            text: "팝업 내용입니다."
        }
        
        FluFilledButton {
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 20
            text: "닫기"
            onClicked: popup.close()
        }
    }
}

// 팝업 표시
FluButton {
    text: "팝업 열기"
    onClicked: popup.open()
}
```

## 툴팁 (FluTooltip)

요소에 마우스를 올릴 때 툴팁을 표시하는 컴포넌트입니다.

### 주요 속성
- `text`: 툴팁 텍스트
- `delay`: 표시 지연 시간 (밀리초)
- `timeout`: 표시 시간 (밀리초)
- `font`: 폰트
- `textColor`: 텍스트 색상
- `backgroundColor`: 배경 색상

### 사용 예제
```qml
import QtQuick
import FluentUI

FluButton {
    text: "버튼"
    
    FluTooltip {
        text: "이것은 버튼입니다."
        delay: 500
        timeout: 3000
    }
}
```

## 투어 (FluTour)

UI 요소에 대한 가이드 투어를 제공하는 컴포넌트입니다.

### 주요 속성
- `model`: 투어 항목 모델
- `spacing`: 투어와 타겟 사이의 간격
- `stepIndex`: 현재 단계 인덱스
- `nextButtonText`: 다음 버튼 텍스트
- `previousButtonText`: 이전 버튼 텍스트
- `finishButtonText`: 완료 버튼 텍스트
- `skipButtonText`: 건너뛰기 버튼 텍스트

### 사용 예제
```qml
import QtQuick
import FluentUI

// 투어 대상 요소들
Rectangle {
    id: rect1
    width: 100
    height: 100
    color: "red"
}

Rectangle {
    id: rect2
    width: 100
    height: 100
    color: "blue"
    x: 150
}

// 투어 정의
FluTour {
    id: tour
    anchors.fill: parent
    model: [
        {
            target: rect1,
            title: "빨간색 사각형",
            description: "이것은 빨간색 사각형입니다.",
            position: FluTourType.Bottom
        },
        {
            target: rect2,
            title: "파란색 사각형",
            description: "이것은 파란색 사각형입니다.",
            position: FluTourType.Right
        }
    ]
    
    onFinished: {
        console.log("투어 완료")
    }
}

// 투어 시작
FluButton {
    text: "투어 시작"
    onClicked: tour.start()
}
```

## 메뉴 (FluMenu)

컨텍스트 메뉴나 드롭다운 메뉴로 사용할 수 있는 컴포넌트입니다.

### 주요 속성
- `width`: 메뉴 너비
- `closePolicy`: 닫기 정책

### 사용 예제
```qml
import QtQuick
import FluentUI

FluMenu {
    id: menu
    
    FluMenuItem {
        text: "새 파일"
        iconSource: FluentIcons.Document
        onClicked: console.log("새 파일 메뉴 클릭됨")
    }
    
    FluMenuItem {
        text: "열기"
        iconSource: FluentIcons.OpenFile
        onClicked: console.log("열기 메뉴 클릭됨")
    }
    
    FluMenuSeparator {}
    
    FluMenuItem {
        text: "저장"
        iconSource: FluentIcons.Save
        onClicked: console.log("저장 메뉴 클릭됨")
    }
    
    FluMenuItem {
        text: "다른 이름으로 저장"
        iconSource: FluentIcons.SaveAs
        onClicked: console.log("다른 이름으로 저장 메뉴 클릭됨")
    }
}

// 메뉴 표시
FluButton {
    text: "메뉴 열기"
    onClicked: menu.popup()
}
```

## 메뉴 바 (FluMenuBar)

애플리케이션 상단에 메뉴를 표시하는 컴포넌트입니다.

### 주요 속성
- `model`: 메뉴 항목 모델

### 사용 예제
```qml
import QtQuick
import FluentUI

FluMenuBar {
    id: menuBar
    width: parent.width
    
    FluMenuBarItem {
        title: "파일"
        
        FluMenuItem {
            text: "새 파일"
            iconSource: FluentIcons.Document
            onClicked: console.log("새 파일 메뉴 클릭됨")
        }
        
        FluMenuItem {
            text: "열기"
            iconSource: FluentIcons.OpenFile
            onClicked: console.log("열기 메뉴 클릭됨")
        }
        
        FluMenuSeparator {}
        
        FluMenuItem {
            text: "종료"
            iconSource: FluentIcons.Cancel
            onClicked: console.log("종료 메뉴 클릭됨")
        }
    }
    
    FluMenuBarItem {
        title: "편집"
        
        FluMenuItem {
            text: "실행 취소"
            iconSource: FluentIcons.Undo
            onClicked: console.log("실행 취소 메뉴 클릭됨")
        }
        
        FluMenuItem {
            text: "다시 실행"
            iconSource: FluentIcons.Redo
            onClicked: console.log("다시 실행 메뉴 클릭됨")
        }
    }
    
    FluMenuBarItem {
        title: "도움말"
        
        FluMenuItem {
            text: "정보"
            iconSource: FluentIcons.Info
            onClicked: console.log("정보 메뉴 클릭됨")
        }
    }
}
```

## 윈도우 다이얼로그 (FluWindowDialog)

별도의 창에 다이얼로그를 표시하는 컴포넌트입니다.

### 주요 속성
- `title`: 다이얼로그 제목
- `width`: 너비
- `height`: 높이
- `fixSize`: 크기 고정 여부
- `appBarVisible`: 앱 바 표시 여부
- `appBarHeight`: 앱 바 높이

### 사용 예제
```qml
import QtQuick
import FluentUI

FluWindowDialog {
    id: windowDialog
    title: "윈도우 다이얼로그"
    width: 400
    height: 300
    appBarVisible: true
    
    // 다이얼로그 내용
    Column {
        anchors.centerIn: parent
        spacing: 20
        
        FluText {
            text: "윈도우 다이얼로그 내용입니다."
        }
        
        FluFilledButton {
            text: "닫기"
            onClicked: windowDialog.close()
        }
    }
}

// 윈도우 다이얼로그 표시
FluButton {
    text: "윈도우 다이얼로그 열기"
    onClicked: windowDialog.open()
}
```

## 배지 (FluBadge)

숫자나 텍스트 배지를 표시하는 컴포넌트입니다.

### 주요 속성
- `count`: 카운트 값
- `color`: 배지 색상
- `textColor`: 텍스트 색상
- `showZero`: 0 표시 여부
- `dot`: 점 형태로 표시 여부
- `position`: 위치 (FluBadgeType.TopRight, TopLeft, BottomRight, BottomLeft)

### 사용 예제
```qml
import QtQuick
import FluentUI

FluBadge {
    id: badge
    count: 5
    color: "red"
    textColor: "white"
    
    Rectangle {
        width: 50
        height: 50
        color: "#f0f0f0"
    }
}

// 배지 카운트 변경
FluButton {
    text: "카운트 증가"
    onClicked: badge.count++
}
```

## 캐러셀 (FluCarousel)

이미지나 컨텐츠를 슬라이드쇼 형태로 표시하는 컴포넌트입니다.

### 주요 속성
- `model`: 표시할 항목 모델
- `delegate`: 아이템 표시 방식
- `autoPlay`: 자동 재생 여부
- `loopPlay`: 반복 재생 여부
- `intervalTime`: 자동 재생 간격 (밀리초)
- `indicatorPosition`: 인디케이터 위치 (FluCarouselType.Bottom, Top, Left, Right)
- `currentIndex`: 현재 인덱스

### 사용 예제
```qml
import QtQuick
import FluentUI

FluCarousel {
    width: 600
    height: 300
    autoPlay: true
    loopPlay: true
    intervalTime: 3000
    
    model: [
        "qrc:/images/image1.jpg",
        "qrc:/images/image2.jpg",
        "qrc:/images/image3.jpg"
    ]
    
    delegate: Image {
        source: modelData
        width: parent.width
        height: parent.height
        fillMode: Image.PreserveAspectCrop
    }
}
``` 