# FluentUI 고급 예제

이 문서에서는 FluentUI를 사용한 고급 사용 사례와 예제를 제공합니다. 단순한 컴포넌트 사용을 넘어서는 복잡한 UI 패턴과 시나리오를 다룹니다.

## 네비게이션 뷰 레이아웃

`FluNavigationView`를 사용한 모던한 탐색 인터페이스 구현 예제입니다.

```qml
import QtQuick
import QtQuick.Layouts
import QtQuick.Window
import FluentUI

FluWindow {
    id: window
    width: 1200
    height: 800
    title: "네비게이션 뷰 예제"
    
    FluNavigationView {
        id: navigationView
        anchors.fill: parent
        
        // 앱 로고 및 타이틀
        logo: "qrc:/images/logo.png"
        title: "FluentUI 앱"
        
        // 상단 아이템들
        topPadding: 10
        
        // 네비게이션 메뉴 아이템
        FluPaneItem {
            title: "홈"
            icon: FluentIcons.Home
            onTapped: {
                navigationView.push("qrc:/pages/HomePage.qml")
            }
        }
        
        FluPaneItem {
            title: "프로필"
            icon: FluentIcons.Contact
            onTapped: {
                navigationView.push("qrc:/pages/ProfilePage.qml")
            }
        }
        
        FluPaneItemExpander {
            title: "설정"
            icon: FluentIcons.Settings
            
            FluPaneItem {
                title: "일반"
                onTapped: {
                    navigationView.push("qrc:/pages/GeneralSettingsPage.qml")
                }
            }
            
            FluPaneItem {
                title: "테마"
                onTapped: {
                    navigationView.push("qrc:/pages/ThemeSettingsPage.qml")
                }
            }
            
            FluPaneItem {
                title: "알림"
                onTapped: {
                    navigationView.push("qrc:/pages/NotificationSettingsPage.qml")
                }
            }
        }
        
        // 하단 메뉴 아이템
        FluPaneItemSeparator {}
        
        FluPaneItem {
            title: "도움말"
            icon: FluentIcons.Help
            onTapped: {
                navigationView.push("qrc:/pages/HelpPage.qml")
            }
        }
        
        // 기본 콘텐츠 영역
        Component.onCompleted: {
            navigationView.push("qrc:/pages/HomePage.qml")
        }
    }
}
```

## 응답형 레이아웃

화면 크기에 따라 적응하는 반응형 UI 구현 예제입니다.

```qml
import QtQuick
import QtQuick.Layouts
import FluentUI

FluWindow {
    id: window
    width: 1000
    height: 700
    title: "응답형 레이아웃 예제"
    
    property bool isMobile: width < 600
    property bool isTablet: width >= 600 && width < 900
    property bool isDesktop: width >= 900
    
    FluNavigationView {
        id: navView
        anchors.fill: parent
        
        // 모바일에서는 컴팩트 모드
        displayMode: isMobile ? FluNavigationViewType.Minimal :
                   isTablet ? FluNavigationViewType.Compact :
                   FluNavigationViewType.Open
        
        // 기본 메뉴 아이템들
        FluPaneItem {
            title: "대시보드"
            icon: FluentIcons.ViewDashboard
            onTapped: {
                mainLoader.source = "qrc:/pages/DashboardPage.qml"
            }
        }
        
        // 콘텐츠 영역
        contentItem: Item {
            FluLoader {
                id: mainLoader
                anchors.fill: parent
                source: "qrc:/pages/DashboardPage.qml"
            }
        }
    }
    
    // 화면 크기에 따른 글꼴 크기 조정
    Component.onCompleted: {
        adjustFontSizes()
    }
    
    onWidthChanged: {
        adjustFontSizes()
    }
    
    function adjustFontSizes() {
        if (isMobile) {
            FluTheme.textSize = 14
        } else if (isTablet) {
            FluTheme.textSize = 16
        } else {
            FluTheme.textSize = 18
        }
    }
}
```

## 테마 전환 애니메이션

다크 모드와 라이트 모드 간의 부드러운 전환 효과를 구현한 예제입니다.

```qml
import QtQuick
import QtQuick.Controls
import FluentUI

FluWindow {
    id: window
    width: 800
    height: 600
    title: "테마 전환 애니메이션"
    
    property color backgroundColor: FluTheme.dark ? "#202020" : "#f3f3f3"
    
    Rectangle {
        id: backgroundRect
        anchors.fill: parent
        color: backgroundColor
        
        Behavior on color {
            ColorAnimation {
                duration: 300
                easing.type: Easing.InOutQuad
            }
        }
    }
    
    Column {
        anchors.centerIn: parent
        spacing: 20
        
        FluText {
            text: "현재 테마: " + (FluTheme.dark ? "다크" : "라이트")
            font: FluTextStyle.Title
            color: FluTheme.dark ? "white" : "black"
            
            Behavior on color {
                ColorAnimation {
                    duration: 300
                    easing.type: Easing.InOutQuad
                }
            }
        }
        
        FluToggleSwitch {
            text: "다크 모드"
            checked: FluTheme.dark
            onClicked: {
                // 테마 변경
                FluTheme.darkMode = FluTheme.dark ? FluThemeType.Light : FluThemeType.Dark
            }
        }
        
        FluFilledButton {
            text: "랜덤 테마 색상"
            onClicked: {
                // 랜덤 강조색 설정
                var colors = [FluColors.Yellow, FluColors.Orange, FluColors.Red, 
                             FluColors.Magenta, FluColors.Purple, FluColors.Blue, 
                             FluColors.Teal, FluColors.Green]
                var randomColor = colors[Math.floor(Math.random() * colors.length)]
                FluTheme.accentColor = randomColor
            }
        }
    }
}
```

## 데이터 바인딩 및 모델 사용

`ListModel`과 `Repeater`를 사용한 데이터 바인딩 예제입니다.

```qml
import QtQuick
import QtQuick.Layouts
import FluentUI

FluWindow {
    id: window
    width: 800
    height: 600
    title: "데이터 바인딩 예제"
    
    // 샘플 데이터 모델
    ListModel {
        id: usersModel
        
        ListElement {
            name: "홍길동"
            email: "hong@example.com"
            role: "관리자"
            avatar: "qrc:/images/avatars/avatar1.png"
        }
        ListElement {
            name: "김철수"
            email: "kim@example.com"
            role: "개발자"
            avatar: "qrc:/images/avatars/avatar2.png"
        }
        ListElement {
            name: "이영희"
            email: "lee@example.com"
            role: "디자이너"
            avatar: "qrc:/images/avatars/avatar3.png"
        }
    }
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 10
        
        // 타이틀
        FluText {
            text: "사용자 목록"
            font: FluTextStyle.TitleLarge
            Layout.alignment: Qt.AlignHCenter
            Layout.bottomMargin: 20
        }
        
        // 사용자 카드 리스트
        GridLayout {
            columns: window.width > 700 ? 3 : window.width > 500 ? 2 : 1
            Layout.fillWidth: true
            Layout.fillHeight: true
            columnSpacing: 15
            rowSpacing: 15
            
            Repeater {
                model: usersModel
                
                // 각 사용자 카드
                Rectangle {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 150
                    radius: 8
                    color: FluTheme.dark ? "#333333" : "white"
                    
                    // 그림자
                    FluShadow {
                        radius: 30
                    }
                    
                    RowLayout {
                        anchors.fill: parent
                        anchors.margins: 15
                        spacing: 15
                        
                        // 아바타
                        FluClip {
                            Layout.preferredWidth: 80
                            Layout.preferredHeight: 80
                            radius: 40
                            
                            Image {
                                anchors.fill: parent
                                source: model.avatar
                                fillMode: Image.PreserveAspectCrop
                            }
                        }
                        
                        // 사용자 정보
                        ColumnLayout {
                            Layout.fillWidth: true
                            spacing: 5
                            
                            FluText {
                                text: model.name
                                font: FluTextStyle.Subtitle
                            }
                            
                            FluText {
                                text: model.email
                                color: FluTheme.dark ? "#cccccc" : "#666666"
                            }
                            
                            FluBadge {
                                text: model.role
                                color: {
                                    if (model.role === "관리자") return FluColors.Red.normal
                                    if (model.role === "개발자") return FluColors.Blue.normal
                                    return FluColors.Green.normal
                                }
                            }
                        }
                        
                        // 액션 버튼
                        FluIconButton {
                            iconSource: FluentIcons.MoreVertical
                            Layout.alignment: Qt.AlignTop | Qt.AlignRight
                            onClicked: {
                                userContextMenu.popup()
                            }
                            
                            // 사용자 컨텍스트 메뉴
                            FluMenu {
                                id: userContextMenu
                                
                                FluMenuItem {
                                    text: "프로필 보기"
                                    iconSource: FluentIcons.Contact
                                }
                                
                                FluMenuItem {
                                    text: "메시지 보내기"
                                    iconSource: FluentIcons.Mail
                                }
                                
                                FluMenuItem {
                                    text: "삭제"
                                    iconSource: FluentIcons.Delete
                                    textColor: FluColors.Red.normal
                                }
                            }
                        }
                    }
                }
            }
        }
        
        // 새 사용자 추가 버튼
        FluFilledButton {
            text: "새 사용자 추가"
            Layout.alignment: Qt.AlignHCenter
            Layout.topMargin: 10
            onClicked: {
                addUserDialog.open()
            }
        }
        
        // 새 사용자 추가 다이얼로그
        FluContentDialog {
            id: addUserDialog
            title: "새 사용자 추가"
            message: "새 사용자 정보를 입력하세요."
            
            contentDelegate: ColumnLayout {
                spacing: 15
                width: 400
                
                FluTextBox {
                    id: nameTextBox
                    placeholderText: "이름"
                    Layout.fillWidth: true
                }
                
                FluTextBox {
                    id: emailTextBox
                    placeholderText: "이메일"
                    Layout.fillWidth: true
                }
                
                FluComboBox {
                    id: roleComboBox
                    Layout.fillWidth: true
                    model: ["관리자", "개발자", "디자이너"]
                    currentIndex: 1
                }
            }
            
            positiveText: "추가"
            negativeText: "취소"
            
            onPositiveClicked: {
                usersModel.append({
                    name: nameTextBox.text,
                    email: emailTextBox.text,
                    role: roleComboBox.model[roleComboBox.currentIndex],
                    avatar: "qrc:/images/avatars/avatar_default.png"
                })
            }
        }
    }
}
```

## 드래그 앤 드롭 기능

드래그 앤 드롭 기능을 활용한 사용자 인터페이스 예제입니다.

```qml
import QtQuick
import QtQuick.Layouts
import FluentUI

FluWindow {
    id: window
    width: 800
    height: 600
    title: "드래그 앤 드롭 예제"
    
    // 작업 모델
    ListModel {
        id: tasksModel
        
        ListElement { name: "디자인 시안 작성"; status: "할 일"; priority: "높음" }
        ListElement { name: "API 개발"; status: "할 일"; priority: "중간" }
        ListElement { name: "테스트 케이스 작성"; status: "할 일"; priority: "낮음" }
        ListElement { name: "코드 리뷰"; status: "진행 중"; priority: "높음" }
        ListElement { name: "버그 수정"; status: "진행 중"; priority: "중간" }
        ListElement { name: "문서 작성"; status: "완료"; priority: "낮음" }
        ListElement { name: "환경 설정"; status: "완료"; priority: "중간" }
    }
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15
        
        // 타이틀
        FluText {
            text: "칸반 보드"
            font: FluTextStyle.TitleLarge
            Layout.alignment: Qt.AlignHCenter
            Layout.bottomMargin: 10
        }
        
        // 칸반 보드
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 15
            
            // 할 일 칸반 열
            Rectangle {
                Layout.fillHeight: true
                Layout.preferredWidth: parent.width / 3 - 10
                color: FluTheme.dark ? "#333333" : "#f9f9f9"
                radius: 8
                
                DropArea {
                    id: todoDropArea
                    anchors.fill: parent
                    
                    onDropped: function(drop) {
                        var task = JSON.parse(drop.getDataAsString("text/task"))
                        tasksModel.setProperty(task.index, "status", "할 일")
                    }
                }
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 10
                    spacing: 10
                    
                    // 칸반 열 헤더
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: FluColors.Blue.lighter
                        radius: 5
                        
                        FluText {
                            anchors.centerIn: parent
                            text: "할 일"
                            font: FluTextStyle.Subtitle
                            color: FluColors.Blue.dark
                        }
                    }
                    
                    // 작업 목록
                    ListView {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        spacing: 8
                        clip: true
                        model: tasksModel
                        
                        delegate: Rectangle {
                            width: parent.width
                            height: 80
                            visible: model.status === "할 일"
                            color: FluTheme.dark ? "#444444" : "white"
                            radius: 4
                            
                            // 그림자
                            FluShadow {
                                radius: 15
                            }
                            
                            // 드래그 영역
                            MouseArea {
                                id: dragArea
                                anchors.fill: parent
                                drag.target: parent
                                
                                property int startX
                                property int startY
                                
                                onPressed: {
                                    startX = parent.x
                                    startY = parent.y
                                }
                                
                                onReleased: {
                                    parent.Drag.drop()
                                    parent.x = startX
                                    parent.y = startY
                                }
                            }
                            
                            Drag.active: dragArea.drag.active
                            Drag.hotSpot.x: width / 2
                            Drag.hotSpot.y: height / 2
                            Drag.mimeData: { "text/task": JSON.stringify({ index: index }) }
                            
                            ColumnLayout {
                                anchors.fill: parent
                                anchors.margins: 10
                                spacing: 5
                                
                                RowLayout {
                                    Layout.fillWidth: true
                                    
                                    FluText {
                                        text: model.name
                                        font: FluTextStyle.BodyStrong
                                        Layout.fillWidth: true
                                    }
                                    
                                    FluBadge {
                                        text: model.priority
                                        color: {
                                            if (model.priority === "높음") return FluColors.Red.normal
                                            if (model.priority === "중간") return FluColors.Orange.normal
                                            return FluColors.Green.normal
                                        }
                                    }
                                }
                                
                                FluText {
                                    text: "상태: " + model.status
                                    font: FluTextStyle.Caption
                                    color: FluTheme.fontSecondaryColor
                                }
                            }
                        }
                    }
                }
            }
            
            // 진행 중 칸반 열
            Rectangle {
                Layout.fillHeight: true
                Layout.preferredWidth: parent.width / 3 - 10
                color: FluTheme.dark ? "#333333" : "#f9f9f9"
                radius: 8
                
                DropArea {
                    id: inProgressDropArea
                    anchors.fill: parent
                    
                    onDropped: function(drop) {
                        var task = JSON.parse(drop.getDataAsString("text/task"))
                        tasksModel.setProperty(task.index, "status", "진행 중")
                    }
                }
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 10
                    spacing: 10
                    
                    // 칸반 열 헤더
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: FluColors.Orange.lighter
                        radius: 5
                        
                        FluText {
                            anchors.centerIn: parent
                            text: "진행 중"
                            font: FluTextStyle.Subtitle
                            color: FluColors.Orange.dark
                        }
                    }
                    
                    // 작업 목록
                    ListView {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        spacing: 8
                        clip: true
                        model: tasksModel
                        
                        delegate: Rectangle {
                            width: parent.width
                            height: 80
                            visible: model.status === "진행 중"
                            color: FluTheme.dark ? "#444444" : "white"
                            radius: 4
                            
                            // 그림자
                            FluShadow {
                                radius: 15
                            }
                            
                            // 드래그 영역
                            MouseArea {
                                id: inProgressDragArea
                                anchors.fill: parent
                                drag.target: parent
                                
                                property int startX
                                property int startY
                                
                                onPressed: {
                                    startX = parent.x
                                    startY = parent.y
                                }
                                
                                onReleased: {
                                    parent.Drag.drop()
                                    parent.x = startX
                                    parent.y = startY
                                }
                            }
                            
                            Drag.active: inProgressDragArea.drag.active
                            Drag.hotSpot.x: width / 2
                            Drag.hotSpot.y: height / 2
                            Drag.mimeData: { "text/task": JSON.stringify({ index: index }) }
                            
                            ColumnLayout {
                                anchors.fill: parent
                                anchors.margins: 10
                                spacing: 5
                                
                                RowLayout {
                                    Layout.fillWidth: true
                                    
                                    FluText {
                                        text: model.name
                                        font: FluTextStyle.BodyStrong
                                        Layout.fillWidth: true
                                    }
                                    
                                    FluBadge {
                                        text: model.priority
                                        color: {
                                            if (model.priority === "높음") return FluColors.Red.normal
                                            if (model.priority === "중간") return FluColors.Orange.normal
                                            return FluColors.Green.normal
                                        }
                                    }
                                }
                                
                                FluText {
                                    text: "상태: " + model.status
                                    font: FluTextStyle.Caption
                                    color: FluTheme.fontSecondaryColor
                                }
                            }
                        }
                    }
                }
            }
            
            // 완료 칸반 열
            Rectangle {
                Layout.fillHeight: true
                Layout.preferredWidth: parent.width / 3 - 10
                color: FluTheme.dark ? "#333333" : "#f9f9f9"
                radius: 8
                
                DropArea {
                    id: doneDropArea
                    anchors.fill: parent
                    
                    onDropped: function(drop) {
                        var task = JSON.parse(drop.getDataAsString("text/task"))
                        tasksModel.setProperty(task.index, "status", "완료")
                    }
                }
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 10
                    spacing: 10
                    
                    // 칸반 열 헤더
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: FluColors.Green.lighter
                        radius: 5
                        
                        FluText {
                            anchors.centerIn: parent
                            text: "완료"
                            font: FluTextStyle.Subtitle
                            color: FluColors.Green.dark
                        }
                    }
                    
                    // 작업 목록
                    ListView {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        spacing: 8
                        clip: true
                        model: tasksModel
                        
                        delegate: Rectangle {
                            width: parent.width
                            height: 80
                            visible: model.status === "완료"
                            color: FluTheme.dark ? "#444444" : "white"
                            radius: 4
                            
                            // 그림자
                            FluShadow {
                                radius: 15
                            }
                            
                            // 드래그 영역
                            MouseArea {
                                id: doneDragArea
                                anchors.fill: parent
                                drag.target: parent
                                
                                property int startX
                                property int startY
                                
                                onPressed: {
                                    startX = parent.x
                                    startY = parent.y
                                }
                                
                                onReleased: {
                                    parent.Drag.drop()
                                    parent.x = startX
                                    parent.y = startY
                                }
                            }
                            
                            Drag.active: doneDragArea.drag.active
                            Drag.hotSpot.x: width / 2
                            Drag.hotSpot.y: height / 2
                            Drag.mimeData: { "text/task": JSON.stringify({ index: index }) }
                            
                            ColumnLayout {
                                anchors.fill: parent
                                anchors.margins: 10
                                spacing: 5
                                
                                RowLayout {
                                    Layout.fillWidth: true
                                    
                                    FluText {
                                        text: model.name
                                        font: FluTextStyle.BodyStrong
                                        Layout.fillWidth: true
                                    }
                                    
                                    FluBadge {
                                        text: model.priority
                                        color: {
                                            if (model.priority === "높음") return FluColors.Red.normal
                                            if (model.priority === "중간") return FluColors.Orange.normal
                                            return FluColors.Green.normal
                                        }
                                    }
                                }
                                
                                FluText {
                                    text: "상태: " + model.status
                                    font: FluTextStyle.Caption
                                    color: FluTheme.fontSecondaryColor
                                }
                            }
                        }
                    }
                }
            }
        }
        
        // 새 작업 추가 버튼
        FluFilledButton {
            text: "새 작업 추가"
            icon.source: FluentIcons.Add
            Layout.alignment: Qt.AlignHCenter
            Layout.topMargin: 10
            onClicked: {
                addTaskDialog.open()
            }
        }
        
        // 새 작업 추가 다이얼로그
        FluContentDialog {
            id: addTaskDialog
            title: "새 작업 추가"
            message: "새 작업 정보를 입력하세요."
            
            contentDelegate: ColumnLayout {
                spacing: 15
                width: 400
                
                FluTextBox {
                    id: taskNameTextBox
                    placeholderText: "작업 이름"
                    Layout.fillWidth: true
                }
                
                FluText {
                    text: "우선순위"
                }
                
                FluRadioButtons {
                    Layout.fillWidth: true
                    model: ["높음", "중간", "낮음"]
                    currentIndex: 1
                }
            }
            
            positiveText: "추가"
            negativeText: "취소"
            
            onPositiveClicked: {
                tasksModel.append({
                    name: taskNameTextBox.text,
                    status: "할 일",
                    priority: ["높음", "중간", "낮음"][Math.floor(Math.random() * 3)]
                })
            }
        }
    }
}
``` 