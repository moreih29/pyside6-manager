# 레이아웃 컴포넌트 (Layout Controls)

FluentUI는 UI 요소를 구성하고 배치하기 위한 다양한 레이아웃 컴포넌트를 제공합니다. 이 문서에서는 각 레이아웃 컴포넌트의 주요 속성과 사용 예제를 설명합니다.

## 윈도우 (FluWindow)

기본 윈도우 컴포넌트로, 애플리케이션의 주요 창을 나타냅니다.

### 주요 속성
- `title`: 윈도우 제목
- `width`: 윈도우 너비
- `height`: 윈도우 높이
- `darkMode`: 다크 모드 설정 (FluThemeType.DarkMode.Auto, Light, Dark, System)
- `showInTaskbar`: 작업 표시줄에 표시 여부
- `fixSize`: 크기 고정 여부
- `appBarVisible`: 앱 바 표시 여부
- `fitsSystemBar`: 시스템 바 포함 여부
- `blur`: 블러 효과 적용 여부
- `closeDestory`: 닫을 때 파괴 여부
- `minimumWidth`: 최소 너비
- `minimumHeight`: 최소 높이
- `maximumWidth`: 최대 너비
- `maximumHeight`: 최대 높이

### 사용 예제
```qml
import FluentUI

FluWindow {
    id: window
    width: 800
    height: 600
    title: "FluentUI 윈도우"
    appBarVisible: true
    minimumWidth: 500
    minimumHeight: 400
    
    FluText {
        anchors.centerIn: parent
        text: "FluentUI 윈도우 예제"
        font.pixelSize: 20
    }
}
```

## 페이지 (FluPage)

내용을 표시하는 페이지 컴포넌트입니다.

### 주요 속성
- `title`: 페이지 제목
- `appBar`: 앱 바 컴포넌트

### 사용 예제
```qml
import FluentUI

FluPage {
    title: "페이지 제목"
    
    FluText {
        anchors.centerIn: parent
        text: "페이지 내용"
        font.pixelSize: 16
    }
}
```

## 내비게이션 뷰 (FluNavigationView)

사이드 내비게이션을 제공하는 컴포넌트입니다.

### 주요 속성
- `title`: 내비게이션 뷰 제목
- `logo`: 로고 이미지 URL
- `items`: 내비게이션 항목들 (FluPaneItem 사용)
- `footerItems`: 하단 내비게이션 항목들
- `displayMode`: 표시 모드 (FluNavigationViewType.Auto, Left, Top, LeftCompact, LeftMinimal)
- `pageMode`: 페이지 모드 (FluNavigationViewType.Stack, NoStack)
- `autoSuggestBox`: 검색 박스 컴포넌트
- `topPadding`: 상단 여백

### 사용 예제
```qml
import FluentUI

FluWindow {
    id: window
    width: 1000
    height: 640
    title: "FluNavigationView 예제"
    
    FluNavigationView {
        anchors.fill: parent
        title: "내비게이션 뷰"
        
        items: FluObject {
            FluPaneItem {
                title: "홈"
                icon: FluentIcons.Home
                onTapped: {
                    // 홈 탭 클릭 처리
                }
            }
            
            FluPaneItemExpander {
                title: "설정"
                icon: FluentIcons.Settings
                
                FluPaneItem {
                    title: "일반 설정"
                    icon: FluentIcons.Personalize
                    onTapped: {
                        // 일반 설정 탭 클릭 처리
                    }
                }
                
                FluPaneItem {
                    title: "테마 설정"
                    icon: FluentIcons.Color
                    onTapped: {
                        // 테마 설정 탭 클릭 처리
                    }
                }
            }
            
            FluPaneItemSeparator {}
            
            FluPaneItem {
                title: "도움말"
                icon: FluentIcons.Help
                onTapped: {
                    // 도움말 탭 클릭 처리
                }
            }
        }
        
        footerItems: FluObject {
            FluPaneItem {
                title: "로그아웃"
                icon: FluentIcons.SignOut
                onTapped: {
                    // 로그아웃 처리
                }
            }
        }
    }
}
```

## 탭 뷰 (FluTabView)

여러 탭을 전환하며 내용을 표시하는 컴포넌트입니다.

### 주요 속성
- `currentIndex`: 현재 선택된 탭 인덱스
- `addButtonVisibility`: 탭 추가 버튼 표시 여부
- `closeButtonVisibility`: 탭 닫기 버튼 표시 여부
- `tabWidthBehavior`: 탭 너비 동작 방식
- `contentItemData`: 탭 내용 데이터

### 신호 (Signals)
- `tabCloseRequested(int index)`: 탭 닫기 요청 시 발생
- `newTabClicked()`: 새 탭 버튼 클릭 시 발생

### 사용 예제
```qml
import FluentUI

FluTabView {
    width: 600
    height: 400
    addButtonVisibility: FluTabViewType.Visible
    closeButtonVisibility: FluTabViewType.OnHover
    
    // 초기 탭 아이템 추가
    Component.onCompleted: {
        addTab("탭 1", "탭 1의 내용입니다.")
        addTab("탭 2", "탭 2의 내용입니다.")
    }
    
    // 탭 추가 함수
    function addTab(title, content) {
        var tab = {
            title: title,
            contentItem: contentComponent
        }
        contentItemData.push({text: content})
        appendTab(tab)
    }
    
    // 탭 컨텐츠 컴포넌트
    Component {
        id: contentComponent
        FluText {
            text: modelData.text
            anchors.centerIn: parent
        }
    }
    
    // 새 탭 요청 처리
    onNewTabClicked: {
        addTab("새 탭", "새 탭의 내용입니다.")
    }
    
    // 탭 닫기 요청 처리
    onTabCloseRequested: function(index) {
        removeTab(index)
        contentItemData.splice(index, 1)
    }
}
```

## 테이블 뷰 (FluTableView)

표 형태로 데이터를 표시하는 컴포넌트입니다.

### 주요 속성
- `columnSource`: 열 정의
- `tableSource`: 테이블 데이터 소스
- `sortEnabled`: 정렬 기능 활성화 여부
- `hoverEnabled`: 마우스 호버 효과 활성화 여부
- `selectionMode`: 선택 모드 (FluTableViewType.None, Single, Multiple)
- `rowHeight`: 행 높이
- `headerHeight`: 헤더 높이
- `headerVisible`: 헤더 표시 여부

### 사용 예제
```qml
import FluentUI

FluTableView {
    width: 600
    height: 400
    columnSource: [
        { title: "이름", dataIndex: "name", width: 120 },
        { title: "나이", dataIndex: "age", width: 80 },
        { title: "주소", dataIndex: "address", width: 200 }
    ]
    tableSource: [
        { name: "홍길동", age: 20, address: "서울시 강남구" },
        { name: "김철수", age: 25, address: "부산시 해운대구" },
        { name: "이영희", age: 22, address: "인천시 남동구" }
    ]
    sortEnabled: true
    hoverEnabled: true
    selectionMode: FluTableViewType.Single
    
    onRowClicked: function(row) {
        console.log("선택된 행: " + JSON.stringify(row))
    }
}
```

## 분할 레이아웃 (FluSplitLayout)

화면을 분할하여 내용을 배치하는 컴포넌트입니다.

### 주요 속성
- `orientation`: 분할 방향 (Qt.Horizontal, Qt.Vertical)
- `position`: 분할 위치 (0.0 ~ 1.0)
- `fillWidth`: 너비 채우기 여부
- `fillHeight`: 높이 채우기 여부

### 사용 예제
```qml
import FluentUI

FluSplitLayout {
    width: 600
    height: 400
    orientation: Qt.Horizontal
    position: 0.3
    
    // 왼쪽(또는 상단) 영역
    Rectangle {
        color: "#f0f0f0"
        anchors.fill: parent
        
        FluText {
            anchors.centerIn: parent
            text: "왼쪽 영역"
        }
    }
    
    // 오른쪽(또는 하단) 영역
    Rectangle {
        color: "#e0e0e0"
        anchors.fill: parent
        
        FluText {
            anchors.centerIn: parent
            text: "오른쪽 영역"
        }
    }
}
```

## 피벗 (FluPivot)

탭 형식으로 내용을 구성하는 컴포넌트입니다.

### 주요 속성
- `currentIndex`: 현재 선택된 인덱스
- `position`: 피벗 위치 (FluPivotType.Top, Bottom)
- `items`: 피벗 항목들

### 사용 예제
```qml
import FluentUI

FluPivot {
    width: 600
    height: 400
    
    FluPivotItem {
        title: "첫 번째 항목"
        
        FluText {
            anchors.centerIn: parent
            text: "첫 번째 항목의 내용입니다."
        }
    }
    
    FluPivotItem {
        title: "두 번째 항목"
        
        FluText {
            anchors.centerIn: parent
            text: "두 번째 항목의 내용입니다."
        }
    }
    
    FluPivotItem {
        title: "세 번째 항목"
        
        FluText {
            anchors.centerIn: parent
            text: "세 번째 항목의 내용입니다."
        }
    }
}
```

## 확장 패널 (FluExpander)

접거나 펼칠 수 있는 패널 컴포넌트입니다.

### 주요 속성
- `header`: 헤더 내용
- `content`: 내용
- `isExpand`: 확장 상태
- `expandWidth`: 확장 시 너비
- `expandHeight`: 확장 시 높이
- `animationEnabled`: 애니메이션 활성화 여부

### 사용 예제
```qml
import FluentUI

FluExpander {
    width: 300
    header: FluText {
        text: "확장 패널 헤더"
    }
    content: Rectangle {
        width: parent.width
        height: 200
        color: "#f0f0f0"
        
        FluText {
            anchors.centerIn: parent
            text: "확장 패널 내용"
        }
    }
}
```

## 앱 바 (FluAppBar)

앱 상단에 표시되는 바 컴포넌트입니다.

### 주요 속성
- `title`: 앱 바 제목
- `showBackButton`: 뒤로 가기 버튼 표시 여부
- `leftPadding`: 왼쪽 여백
- `rightPadding`: 오른쪽 여백
- `titleColor`: 제목 색상
- `blurHeight`: 블러 효과 높이
- `titleBarColor`: 제목 바 색상

### 신호 (Signals)
- `backClicked()`: 뒤로 가기 버튼 클릭 시 발생

### 사용 예제
```qml
import FluentUI

FluAppBar {
    width: parent.width
    title: "앱 제목"
    showBackButton: true
    
    onBackClicked: {
        console.log("뒤로 가기 버튼 클릭됨")
    }
}
```

## 스크롤 가능한 페이지 (FluScrollablePage)

스크롤이 가능한 페이지 컴포넌트입니다.

### 주요 속성
- `title`: 페이지 제목
- `contentWidth`: 내용 너비
- `spacing`: 항목 간 간격

### 사용 예제
```qml
import FluentUI

FluScrollablePage {
    title: "스크롤 가능한 페이지"
    anchors.fill: parent
    
    Column {
        spacing: 20
        width: parent.width
        
        // 여러 항목 추가
        Repeater {
            model: 20
            
            Rectangle {
                width: parent.width
                height: 50
                color: "#f0f0f0"
                
                FluText {
                    anchors.centerIn: parent
                    text: "항목 " + (index + 1)
                }
            }
        }
    }
}
```

## 격자 레이아웃 (FluStaggeredLayout)

비균일한 크기의 아이템을 격자 형태로 배열하는 컴포넌트입니다.

### 주요 속성
- `model`: 표시할 모델
- `delegate`: 아이템 표시 방식
- `columnCount`: 열 개수
- `columnSpacing`: 열 간격
- `rowSpacing`: 행 간격

### 사용 예제
```qml
import FluentUI

FluStaggeredLayout {
    anchors.fill: parent
    columnCount: 3
    columnSpacing: 10
    rowSpacing: 10
    
    model: 20
    
    delegate: Rectangle {
        width: 100
        // 랜덤한 높이로 아이템 생성
        height: 50 + Math.random() * 100
        color: Qt.rgba(Math.random(), Math.random(), Math.random(), 0.8)
        
        FluText {
            anchors.centerIn: parent
            text: "항목 " + (index + 1)
            color: "white"
        }
    }
}
``` 