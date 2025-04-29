# 05_QtQuick_Controls: 기본적인 UI 컨트롤

이 카테고리에서는 QML 애플리케이션의 사용자 인터페이스를 구성하는 기본적인 컨트롤(Controls) 컴포넌트들을 다룹니다. 이 컴포넌트들은 `QtQuick.Controls` 모듈에서 제공하며, 사용자와의 상호작용을 위한 표준적인 UI 요소들(버튼, 입력 필드, 체크박스 등)을 포함합니다.

`QtQuick.Controls`는 플랫폼별 네이티브 스타일 또는 사용자 정의 스타일을 적용할 수 있는 유연한 컨트롤들을 제공하여 일관되고 보기 좋은 UI를 쉽게 만들 수 있도록 돕습니다.

## 주요 컨트롤 컴포넌트

이 섹션에서는 다음과 같은 주요 컨트롤 컴포넌트들에 대해 자세히 설명합니다.

*   **[AbstractButton](./AbstractButton.md)**: `Button`, `CheckBox`, `RadioButton` 등의 기반 클래스 (개념 설명용).
*   **[Button](./Button.md)**: 사용자가 클릭하여 특정 동작을 수행하도록 하는 기본적인 버튼입니다.
*   **[TextField](./TextField.md)**: 사용자가 한 줄의 텍스트를 입력하고 편집할 수 있는 필드입니다.
*   **[TextArea](./TextArea.md)**: 사용자가 여러 줄의 텍스트를 입력하고 편집할 수 있는 영역입니다.
*   **[CheckBox](./CheckBox.md)**: 사용자가 선택/해제할 수 있는 옵션을 나타내는 체크박스입니다.
*   **[RadioButton](./RadioButton.md)**: 여러 옵션 중 하나만 선택할 수 있는 라디오 버튼 그룹의 일부입니다.
*   **[ComboBox](./ComboBox.md)**: 드롭다운 목록에서 항목을 선택할 수 있는 컨트롤입니다.
*   **[Slider](./Slider.md)**: 특정 범위 내의 값을 사용자가 슬라이더를 움직여 선택할 수 있도록 합니다.
*   **[RangeSlider](./RangeSlider.md)**: 두 개의 핸들을 사용하여 값의 범위를 선택하는 슬라이더입니다.
*   **[SpinBox](./SpinBox.md)**: 위/아래 버튼이나 직접 입력을 통해 숫자 값을 조절하는 컨트롤입니다.
*   **[Switch](./Switch.md)**: 두 가지 상태(on/off)를 토글하는 스위치 컨트롤입니다.
*   **[Label](./Label.md)**: 텍스트 레이블을 표시하는 컨트롤입니다. `Text` 요소보다 스타일링 및 접근성 기능이 강화되었습니다.
*   **[Frame](./Frame.md)**: 시각적인 그룹화를 위해 다른 컨트롤들을 감싸는 프레임(테두리 및 배경)입니다.
*   **[GroupBox](./GroupBox.md)**: `Frame`과 유사하지만 제목(title)을 가질 수 있는 그룹 상자입니다.
*   **[PageIndicator](./PageIndicator.md)**: 여러 페이지(예: `SwipeView`) 중 현재 활성화된 페이지를 시각적으로 나타내는 인디케이터입니다.
*   **[ProgressBar](./ProgressBar.md)**: 작업 진행률을 시각적으로 표시합니다.
*   **[BusyIndicator](./BusyIndicator.md)**: 작업이 진행 중임을 나타내는 애니메이션 인디케이터입니다.
*   **[ScrollBar](./ScrollBar.md)**: `Flickable` 등 스크롤 가능한 콘텐츠 영역의 스크롤 위치를 제어하고 표시하는 스크롤바입니다.
*   **[ScrollIndicator](./ScrollIndicator.md)**: 터치 인터페이스에 더 적합한 스크롤 위치 표시기입니다.
*   **[SplitView](./SplitView.md)**: 크기 조절 가능한 분할선을 가진 두 개의 아이템 영역을 제공하여 공간을 동적으로 나눌 수 있게 합니다.
*   **[Dial](./Dial.md)**: 원형 다이얼을 돌려 값을 선택하는 컨트롤입니다.
*   **[Tumbler](./Tumbler.md)**: 회전하는 원통형 목록에서 항목을 선택하는 컨트롤입니다 (주로 모바일).
*   **[ToolTip](./ToolTip.md)**: 컨트롤 위에 마우스를 올렸을 때 나타나는 도움말 텍스트입니다.

## 스타일링

`QtQuick.Controls`는 다양한 스타일을 지원합니다. 애플리케이션 전체 또는 개별 컨트롤에 대해 스타일을 설정할 수 있으며, 기본 제공 스타일(Default, Fusion, Imagine, Material, Universal, Windows, macOS 등)을 사용하거나 사용자 정의 스타일을 만들 수 있습니다.

이 카테고리의 문서들을 통해 각 컨트롤의 사용법, 주요 속성 및 시그널, 그리고 기본적인 활용 예제를 익힐 수 있습니다. 