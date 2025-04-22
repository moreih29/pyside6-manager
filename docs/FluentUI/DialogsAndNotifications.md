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
- `darkMode`: 다크 모드 여부

### 사용 예제
```qml
import FluentUI

FluContentDialog {
    id: dialog
    title: "다이얼로그 제목"
    message: "다이얼로그 내용 메시지입니다."
    buttonFlags: FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
    negativeText: "취소"
    positiveText: "확인"
    
    onNegativeClicked: {
        console.log("취소 버튼 클릭됨")
    }
    
    onPositiveClicked: {
        console.log("확인 버튼 클릭됨")
    }
}

// 다이얼로그 표시
Button {
    text: "다이얼로그 열기"
    onClicked: dialog.open()
}
```

## 정보 표시줄 (FluInfoBar)

간단한 정보, 경고, 오류 등을 표시하는 컴포넌트입니다.

### 주요 속성
- `title`: 제목
- `message`: 메시지
- `token`: 정보 표시 시간 (밀리초, 0: 무제한)
- `severity`: 심각도 (FluInfoBarType.Info, Success, Warning, Error, Critical)
- `iconVisible`: 아이콘 표시 여부
- `closeButtonVisible`: 닫기 버튼 표시 여부

### 사용 예제
```qml
import FluentUI

FluInfoBar {
    id: infoBar
    title: "정보"
    message: "작업이 성공적으로 완료되었습니다."
    token: 3000  // 3초 후 자동으로 사라짐
    severity: FluInfoBarType.Success
    closeButtonVisible: true
}

// 정보 표시줄 표시
Button {
    text: "정보 표시"
    onClicked: infoBar.open()
}
```

## 시트 (FluSheet)

화면 하단에서 올라오는 시트 형태의 다이얼로그입니다.

### 주요 속성
- `contentWidth`: 내용 너비
- `contentHeight`: 내용 높이
- `coverWidth`: 커버 너비
- `coverHeight`: 커버 높이
- `coverRadius`: 커버 테두리 반경

### 사용 예제
```qml
import FluentUI

FluSheet {
    id: sheet
    contentWidth: 400
    contentHeight: 300
    
    // 시트 내용
    Rectangle {
        anchors.fill: parent
        color: FluTheme.dark ? Qt.rgba(50/255,50/255,50/255,1) : Qt.rgba(240/255,240/255,240/255,1)
        
        FluText {
            anchors.centerIn: parent
            text: "시트 내용입니다."
        }
        
        FluFilledButton {
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 20
            text: "닫기"
            onClicked: sheet.close()
        }
    }
}

// 시트 표시
Button {
    text: "시트 열기"
    onClicked: sheet.open()
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
Button {
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
Button {
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
Button {
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