# 03_Layouts: UI 요소 배치 및 정렬

이 카테고리에서는 QML 애플리케이션에서 사용자 인터페이스 요소들을 효과적으로 배치하고 정렬하는 데 사용되는 레이아웃(Layout) 컴포넌트들을 다룹니다. 주로 `QtQuick.Layouts` 모듈에서 제공하는 클래스들을 사용하며, 자식 아이템들의 크기와 위치를 동적으로 관리하여 반응형 UI를 쉽게 구현할 수 있도록 돕습니다.

레이아웃을 사용하면 아이템들을 수평, 수직, 또는 그리드 형태로 정렬하고, 아이템 간의 간격(spacing)을 설정하며, 아이템의 크기 정책(size policy)을 지정하여 레이아웃 컨테이너 크기 변화에 따라 아이템 크기가 어떻게 조절될지 정의할 수 있습니다.

## 주요 레이아웃 컴포넌트

이 섹션에서는 다음과 같은 주요 레이아웃 컴포넌트들에 대해 자세히 설명합니다.

*   **[RowLayout](./RowLayout.md)**: 자식 아이템들을 가로(행) 방향으로 배치합니다.
*   **[ColumnLayout](./ColumnLayout.md)**: 자식 아이템들을 세로(열) 방향으로 배치합니다.
*   **[GridLayout](./GridLayout.md)**: 자식 아이템들을 격자(그리드) 형태로 배치합니다.
*   **[StackLayout](./StackLayout.md)**: 자식 아이템들을 겹쳐 쌓아 한 번에 하나의 아이템만 보이도록 관리합니다. (탭 위젯이나 화면 전환 등에 사용)

## 레이아웃 활용 기본 개념

*   **자식 아이템에 `Layout` Attached Properties 사용**: 레이아웃 내의 아이템들은 `Layout.fillWidth`, `Layout.fillHeight`, `Layout.preferredWidth`, `Layout.alignment` 등과 같은 `Layout`의 Attached Properties를 사용하여 레이아웃 동작 방식을 제어할 수 있습니다.
*   **크기 제약 조건**: 레이아웃은 자식 아이템의 `implicitWidth/Height`, `Layout.preferredWidth/Height`, `Layout.minimumWidth/Height`, `Layout.maximumWidth/Height` 등을 고려하여 최종 크기와 위치를 결정합니다.
*   **간격**: `spacing` 프로퍼티를 통해 레이아웃 내 아이템들 사이의 간격을 조절할 수 있습니다.

이 카테고리의 문서들을 통해 각 레이아웃 컴포넌트의 사용법과 주요 속성, 그리고 효과적인 UI 구성을 위한 활용 방법을 익힐 수 있습니다. 