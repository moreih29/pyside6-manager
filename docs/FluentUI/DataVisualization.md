# 데이터 시각화 컴포넌트 (Data Visualization Components)

FluentUI는 데이터를 시각적으로 표현하기 위한 다양한 컴포넌트를 제공합니다. 이 문서에서는 각 데이터 시각화 컴포넌트의 주요 속성과 사용 예제를 설명합니다.

## 차트 (FluChart)

다양한 유형의 차트를 표시하는 컴포넌트입니다.

### 주요 속성
- `chartType`: 차트 유형 (FluChartType.Line, Bar, Pie, Doughnut, Area, Scatter)
- `chartData`: 차트 데이터
- `chartOptions`: 차트 옵션
- `chartAnimation`: 애니메이션 활성화 여부

### 사용 예제
```qml
import QtQuick
import FluentUI

FluChart {
    width: 500
    height: 300
    chartType: FluChartType.Line
    chartData: {
        return {
            "labels": ["1월", "2월", "3월", "4월", "5월", "6월"],
            "datasets": [
                {
                    "label": "데이터셋 1",
                    "data": [12, 19, 3, 5, 2, 3],
                    "backgroundColor": FluColors.Blue.toString(),
                    "borderColor": FluColors.Blue.toString(),
                    "borderWidth": 2,
                    "fill": false
                },
                {
                    "label": "데이터셋 2",
                    "data": [7, 11, 5, 8, 3, 7],
                    "backgroundColor": FluColors.Red.toString(),
                    "borderColor": FluColors.Red.toString(),
                    "borderWidth": 2,
                    "fill": false
                }
            ]
        }
    }
    chartOptions: {
        return {
            "responsive": true,
            "plugins": {
                "title": {
                    "display": true,
                    "text": "라인 차트 예제"
                }
            }
        }
    }
}
```

## 프로그레스 바 (FluProgressBar)

진행 상태를 표시하는 바 형태의 컴포넌트입니다.

### 주요 속성
- `value`: 현재 값 (0.0 ~ 1.0)
- `indeterminate`: 불확정 진행 여부
- `progressColor`: 진행 색상
- `progressBarHeight`: 프로그레스 바 높이

### 사용 예제
```qml
import QtQuick
import FluentUI

Column {
    spacing: 20
    
    // 확정 진행 프로그레스 바
    FluProgressBar {
        width: 400
        value: 0.7
        progressColor: FluColors.Blue
    }
    
    // 불확정 진행 프로그레스 바
    FluProgressBar {
        width: 400
        indeterminate: true
        progressColor: FluColors.Green
    }
}
```

## 프로그레스 링 (FluProgressRing)

진행 상태를 표시하는 원형 컴포넌트입니다.

### 주요 속성
- `value`: 현재 값 (0.0 ~ 1.0)
- `indeterminate`: 불확정 진행 여부
- `progressColor`: 진행 색상
- `strokeWidth`: 선 두께

### 사용 예제
```qml
import QtQuick
import FluentUI

Row {
    spacing: 40
    
    // 확정 진행 프로그레스 링
    FluProgressRing {
        width: 100
        height: 100
        value: 0.7
        progressColor: FluColors.Blue
    }
    
    // 불확정 진행 프로그레스 링
    FluProgressRing {
        width: 100
        height: 100
        indeterminate: true
        progressColor: FluColors.Green
    }
}
```

## 타임라인 (FluTimeline)

시간 순으로 사건이나 활동을 표시하는 컴포넌트입니다.

### 주요 속성
- `model`: 타임라인 항목 모델
- `mode`: 타임라인 모드 (FluTimelineType.Left, Right, Alternate)
- `lableDelegate`: 라벨에 대한 delegate (옵션)
- `textDelegate`: 텍스트에 대한 delegate (옵션)
- `dotDelegate`: 점에 대한 delegate (옵션)

### 사용 예제
```qml
import QtQuick
import FluentUI

Column {
    spacing: 20
    
    // 타임라인 모드 선택
    Row {
        spacing: 10
        
        FluText {
            text: "mode:"
            anchors.verticalCenter: parent.verticalCenter
        }
        
        FluDropDownButton {
            id: btnMode
            text: "Alternate"
            width: 100
            
            FluMenuItem {
                text: "Left"
                onClicked: {
                    btnMode.text = text
                    timeline.mode = FluTimelineType.Left
                }
            }
            
            FluMenuItem {
                text: "Right"
                onClicked: {
                    btnMode.text = text
                    timeline.mode = FluTimelineType.Right
                }
            }
            
            FluMenuItem {
                text: "Alternate"
                onClicked: {
                    btnMode.text = text
                    timeline.mode = FluTimelineType.Alternate
                }
            }
        }
    }
    
    // 타임라인 컴포넌트
    FluTimeline {
        id: timeline
        width: parent.width
        mode: FluTimelineType.Alternate
        model: [
            {
                lable: "2023-03-28",
                text: "이벤트 1 설명"
            },
            {
                lable: "2023-02-28",
                text: "이벤트 2 설명"
            },
            {
                lable: "2023-01-01",
                text: "이벤트 3 설명"
            }
        ]
    }
}
```

### 사용 예제 - 커스텀 Delegate 추가
```qml
import QtQuick
import FluentUI

FluTimeline {
    width: parent.width
    mode: FluTimelineType.Alternate
    
    // 커스텀 점 컴포넌트
    Component {
        id: customDot
        Rectangle {
            width: 16
            height: 16
            radius: 8
            border.width: 4
            border.color: FluTheme.dark ? FluColors.Teal.lighter : FluColors.Teal.dark
        }
    }
    
    // 커스텀 라벨 컴포넌트
    Component {
        id: customLabel
        FluText {
            wrapMode: Text.WrapAnywhere
            font.bold: true
            horizontalAlignment: isRight ? Qt.AlignRight : Qt.AlignLeft
            text: modelData.lable
            color: FluTheme.dark ? FluColors.Teal.lighter : FluColors.Teal.dark
            
            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: {
                    console.log(modelData.lable)
                }
            }
        }
    }
    
    // 커스텀 텍스트 컴포넌트
    Component {
        id: customText
        FluText {
            wrapMode: Text.WrapAnywhere
            horizontalAlignment: isRight ? Qt.AlignRight : Qt.AlignLeft
            text: modelData.text
            linkColor: FluTheme.dark ? FluColors.Teal.lighter : FluColors.Teal.dark
            onLinkActivated: (link) => {
                Qt.openUrlExternally(link)
            }
        }
    }
    
    model: [
        {
            lable: "2023-03-28",
            text: '이벤트 설명과 <a href="https://example.com">링크</a>',
            lableDelegate: () => customLabel,
            textDelegate: () => customText,
            dot: () => customDot
        },
        {
            lable: "2023-02-28",
            text: "이벤트 2 설명"
        }
    ]
}
```

## 트리 뷰 (FluTreeView)

계층 구조 데이터를 트리 형태로 표시하는 컴포넌트입니다.

### 주요 속성
- `model`: 트리 항목 모델
- `selectionMode`: 선택 모드 (FluTreeViewType.None, Single, Multiple)
- `checkable`: 체크 박스 표시 여부
- `draggable`: 드래그 가능 여부
- `itemHeight`: 항목 높이
- `expandIcon`: 확장 아이콘
- `collapseIcon`: 축소 아이콘

### 사용 예제
```qml
import QtQuick
import FluentUI

FluTreeView {
    width: 300
    height: 400
    selectionMode: FluTreeViewType.Single
    checkable: true
    itemHeight: 40
    
    // 트리 모델 설정 (FluTreeModel 사용)
    Component.onCompleted: {
        let rootItem1 = treeModel.createItem("폴더 1", FluentIcons.Folder)
        let childItem1 = treeModel.createItem("파일 1-1", FluentIcons.Document)
        let childItem2 = treeModel.createItem("파일 1-2", FluentIcons.Document)
        rootItem1.appendChild(childItem1)
        rootItem1.appendChild(childItem2)
        
        let rootItem2 = treeModel.createItem("폴더 2", FluentIcons.Folder)
        let childItem3 = treeModel.createItem("파일 2-1", FluentIcons.Document)
        let subFolderItem = treeModel.createItem("하위 폴더", FluentIcons.Folder)
        let subChildItem = treeModel.createItem("파일 2-1-1", FluentIcons.Document)
        subFolderItem.appendChild(subChildItem)
        rootItem2.appendChild(childItem3)
        rootItem2.appendChild(subFolderItem)
        
        treeModel.rootItem.appendChild(rootItem1)
        treeModel.rootItem.appendChild(rootItem2)
    }
    
    onItemClicked: function(item) {
        console.log("선택된 항목: " + item.text)
    }
}
```

## 테이블 뷰 (FluTableView)

데이터를 표 형태로 표시하는 컴포넌트입니다.

### 주요 속성
- `rows`: 행 수
- `columns`: 열 수
- `columnSource`: 열 정보 소스
- `rowHeight`: 행 높이
- `columnWidth`: 열 너비
- `editTriggers`: 편집 트리거 (FluTableViewEditTrigger.None, DoubleClicked, SelectedClicked)

### 주요 메서드
- `appendRow(obj)`: 행 추가
- `removeRow(row)`: 행 삭제
- `setRow(row, obj)`: 행 설정
- `getRow(row)`: 행 가져오기
- `customItem(component, options)`: 커스텀 아이템 생성
- `closeEditor()`: 편집기 닫기
- `sort(compareFn)`: 정렬 수행
- `filter(filterFn)`: 필터 적용

### 사용 예제
```qml
import QtQuick
import QtQuick.Layouts
import FluentUI

Item {
    width: 600
    height: 500
    
    Component {
        id: comCheckbox
        Item {
            FluCheckBox {
                anchors.centerIn: parent
                checked: true === options.checked
                animationEnabled: false
                clickListener: function() {
                    var obj = tableView.getRow(row)
                    obj.checkbox = tableView.customItem(comCheckbox, {checked: !options.checked})
                    tableView.setRow(row, obj)
                }
            }
        }
    }
    
    Component {
        id: comAction
        Item {
            RowLayout {
                anchors.centerIn: parent
                FluButton {
                    text: qsTr("Delete")
                    onClicked: {
                        tableView.closeEditor()
                        tableView.removeRow(row)
                    }
                }
                FluFilledButton {
                    text: qsTr("Edit")
                    onClicked: {
                        var obj = tableView.getRow(row)
                        obj.name = "수정된 이름"
                        tableView.setRow(row, obj)
                    }
                }
            }
        }
    }
    
    FluTableView {
        id: tableView
        anchors.fill: parent
        rowHeight: 50
        columnSource: [
            {
                title: "체크박스",
                dataIndex: "checkbox",
                width: 100
            },
            {
                title: "이름",
                dataIndex: "name",
                width: 150
            },
            {
                title: "나이",
                dataIndex: "age", 
                width: 100
            },
            {
                title: "작업",
                dataIndex: "action",
                width: 200
            }
        ]
        
        Component.onCompleted: {
            for (var i = 0; i < 20; i++) {
                tableView.appendRow({
                    checkbox: tableView.customItem(comCheckbox, {checked: true}),
                    name: "사용자 " + i,
                    age: 20 + i,
                    action: tableView.customItem(comAction)
                })
            }
        }
    }
}
```

## 별점 컨트롤 (FluRatingControl)

사용자가 별점을 매길 수 있는 컴포넌트입니다.

### 주요 속성
- `value`: 현재 값
- `maxValue`: 최대 값 (기본값: 5)
- `readOnly`: 읽기 전용 여부
- `starSize`: 별 크기
- `spacing`: 별 간격
- `fillColor`: 채워진 별 색상
- `emptyColor`: 빈 별 색상

### 사용 예제
```qml
import QtQuick
import FluentUI

Column {
    spacing: 20
    
    // 읽기 전용 별점
    FluRatingControl {
        value: 3.5
        maxValue: 5
        readOnly: true
        fillColor: "gold"
    }
    
    // 상호작용 가능한 별점
    FluRatingControl {
        id: ratingControl
        value: 0
        maxValue: 5
        readOnly: false
        onValueChanged: {
            console.log("현재 별점: " + value)
        }
    }
    
    // 별점 표시
    FluText {
        text: "현재 별점: " + ratingControl.value.toFixed(1)
    }
}
```

## 상태 레이아웃 (FluStatusLayout)

로딩, 빈 상태, 오류 등 다양한 상태를 표시하는 컴포넌트입니다.

### 주요 속성
- `status`: 상태 값 (FluStatusLayoutType.Loading, Empty, Error, Success, None)
- `loadingText`: 로딩 상태 텍스트
- `emptyText`: 빈 상태 텍스트
- `errorText`: 오류 상태 텍스트
- `successText`: 성공 상태 텍스트
- `loadingIcon`: 로딩 아이콘
- `emptyIcon`: 빈 상태 아이콘
- `errorIcon`: 오류 아이콘
- `successIcon`: 성공 아이콘

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 20
    
    FluStatusLayout {
        id: statusLayout
        width: 400
        height: 300
        status: FluStatusLayoutType.None
        loadingText: "로딩 중..."
        emptyText: "데이터가 없습니다."
        errorText: "오류가 발생했습니다."
        successText: "성공적으로 처리되었습니다."
    }
    
    Row {
        spacing: 10
        
        FluButton {
            text: "로딩"
            onClicked: statusLayout.status = FluStatusLayoutType.Loading
        }
        
        FluButton {
            text: "빈 상태"
            onClicked: statusLayout.status = FluStatusLayoutType.Empty
        }
        
        FluButton {
            text: "오류"
            onClicked: statusLayout.status = FluStatusLayoutType.Error
        }
        
        FluButton {
            text: "성공"
            onClicked: statusLayout.status = FluStatusLayoutType.Success
        }
        
        FluButton {
            text: "콘텐츠"
            onClicked: statusLayout.status = FluStatusLayoutType.None
        }
    }
}
```

## 페이지네이션 (FluPagination)

데이터 페이지를 표시하는 컴포넌트입니다.

### 주요 속성
- `currentPage`: 현재 페이지
- `totalPage`: 전체 페이지 수
- `maxVisibleButtons`: 최대 표시 버튼 수
- `size`: 크기 (FluPaginationType.Small, Medium, Large)

### 신호 (Signals)
- `pageChanged(int page)`: 페이지 변경 시 발생

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 20
    
    FluPagination {
        id: pagination
        currentPage: 1
        totalPage: 20
        maxVisibleButtons: 7
        size: FluPaginationType.Medium
        
        onPageChanged: function(page) {
            console.log("페이지 변경: " + page)
            // 페이지 데이터 로드 로직 추가
        }
    }
    
    FluText {
        text: "현재 페이지: " + pagination.currentPage + " / " + pagination.totalPage
    }
}
```

## 캘린더 피커 (FluCalendarPicker)

날짜를 선택할 수 있는 캘린더 컴포넌트입니다.

### 주요 속성
- `selectedDate`: 선택된 날짜
- `minDate`: 최소 선택 가능 날짜
- `maxDate`: 최대 선택 가능 날짜
- `firstDayOfWeek`: 주의 첫 요일 (FluCalendarViewType.Monday, Sunday)
- `todayColor`: 오늘 날짜 색상
- `selectedDateColor`: 선택된 날짜 색상
- `weekendTextColor`: 주말 텍스트 색상

### 신호 (Signals)
- `dateClicked(date date)`: 날짜 클릭 시 발생
- `selectedDateChanged()`: 선택된 날짜 변경 시 발생

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 20
    
    FluCalendarPicker {
        id: calendar
        width: 400
        selectedDate: new Date()
        
        onDateClicked: function(date) {
            console.log("선택된 날짜: " + date.toLocaleDateString())
        }
    }
    
    FluText {
        text: "선택된 날짜: " + calendar.selectedDate.toLocaleDateString()
    }
}
```

## 날짜 피커 (FluDatePicker)

날짜를 선택할 수 있는 입력 필드와 드롭다운 캘린더를 제공하는 컴포넌트입니다.

### 주요 속성
- `selectedDate`: 선택된 날짜
- `minDate`: 최소 선택 가능 날짜
- `maxDate`: 최대 선택 가능 날짜
- `firstDayOfWeek`: 주의 첫 요일 (FluCalendarViewType.Monday, Sunday)
- `dateFormat`: 날짜 형식
- `placeholderText`: 플레이스홀더 텍스트

### 신호 (Signals)
- `selectedDateChanged()`: 선택된 날짜 변경 시 발생

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 20
    
    FluDatePicker {
        id: datePicker
        dateFormat: "yyyy-MM-dd"
        placeholderText: "날짜를 선택하세요"
        
        onSelectedDateChanged: {
            if (selectedDate)
                console.log("선택된 날짜: " + selectedDate.toLocaleDateString())
        }
    }
    
    FluText {
        text: datePicker.selectedDate ? "선택된 날짜: " + datePicker.selectedDate.toLocaleDateString() : "날짜가 선택되지 않았습니다."
    }
}
```

## 시간 피커 (FluTimePicker)

시간을 선택할 수 있는 입력 필드와 드롭다운 시간 선택기를 제공하는 컴포넌트입니다.

### 주요 속성
- `hourFormat`: 시간 형식 (12, 24)
- `selectedTime`: 선택된 시간 (QTime)
- `timeFormat`: 시간 표시 형식
- `placeholderText`: 플레이스홀더 텍스트

### 신호 (Signals)
- `selectedTimeChanged()`: 선택된 시간 변경 시 발생

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 20
    
    FluTimePicker {
        id: timePicker
        hourFormat: 24
        timeFormat: "hh:mm:ss"
        placeholderText: "시간을 선택하세요"
        
        onSelectedTimeChanged: {
            console.log("선택된 시간: " + selectedTime.toString())
        }
    }
    
    FluText {
        text: "선택된 시간: " + (timePicker.selectedTime ? timePicker.selectedTime.toString() : "없음")
    }
}
```

## 색상 피커 (FluColorPicker)

색상을 선택할 수 있는 컴포넌트입니다.

### 주요 속성
- `color`: 선택된 색상
- `showAlpha`: 알파 채널 표시 여부
- `showPreview`: 미리보기 표시 여부
- `showHex`: 16진수 코드 표시 여부
- `showRgb`: RGB 값 표시 여부
- `showHsv`: HSV 값 표시 여부

### 신호 (Signals)
- `colorChanged()`: 색상 변경 시 발생

### 사용 예제
```qml
import FluentUI

Column {
    spacing: 20
    
    FluColorPicker {
        id: colorPicker
        width: 400
        showAlpha: true
        showPreview: true
        showHex: true
        showRgb: true
        
        onColorChanged: {
            console.log("선택된 색상: " + color)
        }
    }
    
    Rectangle {
        width: 100
        height: 40
        color: colorPicker.color
        
        FluText {
            anchors.centerIn: parent
            text: colorPicker.color.toString()
            color: isDarkColor(colorPicker.color) ? "white" : "black"
        }
    }
    
    // 색상의 명도 계산 함수
    function isDarkColor(color) {
        var r = color.r * 255
        var g = color.g * 255
        var b = color.b * 255
        var brightness = (r * 299 + g * 587 + b * 114) / 1000
        return brightness < 128
    }
}
``` 