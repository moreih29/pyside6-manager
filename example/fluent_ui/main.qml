import FluentUI

// Window 대신 FluWindow를 최상위 아이템으로 사용합니다.
FluWindow {
    width: 800
    height: 600
    visible: true // visible 속성 추가
    title: "FluentUI 예제"

    FluText {
        anchors.centerIn: parent
        text: FluTextStyle.family + "   FluentUI에 오신 것을 환영합니다!"
        font: FluTextStyle.Title
    }

}