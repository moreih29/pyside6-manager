# 07_Windows_Dialogs: 최상위 창 및 기본 대화상자

이 카테고리에서는 QML 애플리케이션의 최상위 컨테이너 역할을 하는 창(Window)과 사용자에게 메시지를 표시하거나 입력을 받는 표준 대화상자(Dialog) 컴포넌트들을 다룹니다.

애플리케이션의 기본적인 틀을 구성하고 사용자와의 간단한 상호작용을 처리하는 데 필수적인 요소들입니다.

## 주요 컴포넌트 및 개념

이 섹션에서는 창 및 대화상자와 관련된 주요 컴포넌트들을 설명합니다.

*   **창 (Windows)**:
    *   **[Window](./Window.md)** (`QtQuick.Window`): QML 장면(scene)을 표시하는 최상위 네이티브 창입니다. 크기, 위치, 제목, 가시성 등 창의 기본적인 속성을 제어합니다.
    *   **[ApplicationWindow](./ApplicationWindow.md)** (`QtQuick.Controls`): `Window`를 기반으로 메뉴 바, 툴 바, 스테이터스 바 등 일반적인 애플리케이션 창 구조를 쉽게 추가할 수 있도록 확장된 컨트롤입니다. (Fluent UI 사용 시에는 `FluentWindow` 등 대체 컴포넌트 사용 가능성 있음)
*   **대화상자 (Dialogs)**:
    *   **[Dialog](./Dialog.md)** (`QtQuick.Controls`): 사용자 정의 가능한 기본 대화상자 컨테이너입니다. 제목, 내용 영역, 표준 버튼(OK, Cancel 등) 등을 포함하며, 모달(modal) 또는 비모달(non-modal) 형태로 표시할 수 있습니다.
    *   **[MessageDialog](./MessageDialog.md)** (`QtQuick.Dialogs`): 사용자에게 정보, 경고, 질문 등을 간단한 메시지 형태로 표시하는 표준 대화상자입니다. 아이콘과 표준 버튼을 제공합니다.
    *   **[ColorDialog](./ColorDialog.md)** (`QtQuick.Dialogs`): 사용자가 색상을 선택할 수 있는 표준 대화상자입니다.
    *   **[FontDialog](./FontDialog.md)** (`QtQuick.Dialogs`): 사용자가 글꼴을 선택할 수 있는 표준 대화상자입니다.
    *   **[FileDialog](./FileDialog.md)** (`QtQuick.Dialogs`): 사용자가 파일을 열거나 저장할 위치를 선택할 수 있는 네이티브 파일 대화상자입니다.
*   **팝업 (Popups)**:
    *   **[Popup](./Popup.md)** (`QtQuick.Controls`): `ToolTip`, `Menu`, `Dialog` 등의 기반이 되는 기본 팝업 컨테이너입니다. 임시적인 UI 요소를 표시하는 데 사용됩니다.
    *   **[Menu](./Menu.md)** (`QtQuick.Controls`): 컨텍스트 메뉴나 드롭다운 메뉴를 구현하는 데 사용되는 팝업입니다. `MenuItem`들을 포함합니다.

## 모듈 정보

*   `Window`는 `QtQuick.Window` 모듈에 속합니다.
*   `ApplicationWindow`, `Dialog`, `Popup`, `Menu`, `ToolTip` 등은 `QtQuick.Controls` 모듈에 속합니다.
*   `MessageDialog`, `ColorDialog`, `FontDialog`, `FileDialog` 등 표준 대화상자는 `QtQuick.Dialogs` 모듈에 속합니다.

이 카테고리의 문서들을 통해 QML 애플리케이션의 기본 창 구조를 설정하고, 표준 대화상자를 활용하여 사용자와 소통하는 방법을 익힐 수 있습니다. 