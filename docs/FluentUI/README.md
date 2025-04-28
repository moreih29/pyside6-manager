# FluentUI 컴포넌트 개요

## Inputs
### Buttons
### Text
### TextBox
### Slider
### Checkbox
### Radio
### Switch
### TimePicker
### DatePicker
### ColorPicker
### CalendarPicker
### ShortcutPicker
### Rating (RatingControl)
### ComboBox

## Data Display
### Timeline
### Badge
### Clip
### Carousel
### Expander
### Tooltip
### Sheet
### TreeView
### TableView
### FlipView
### Acrylic
### Typography
### Icon
### Chart
### Tour


## Feedback
### Alert (InfoBar)
### Progress
### Dialog


## Surface
### Rectangle

## Navigation
### Menu
### Pivot
### BreadcrumbBar
### TabView
### Pagination

## Window
### MultiWindow

## Layout
### GroupBox
### StaggeredLayout
### SplitLayout
### StatusLayout

## Other
### Theme
### Watermark
### QRCode
### Captcha
### HotLoader

## 문서 형식 가이드

컴포넌트 문서는 다음 형식을 따릅니다.

1.  **제목**: `# Fluent UI [컴포넌트 그룹명] 컴포넌트`
2.  **개요**: 컴포넌트 그룹에 대한 간략한 설명 및 기반 Qt Quick 컨트롤 언급.
3.  **공통 임포트 방법**: 해당 그룹의 컴포넌트 사용에 필요한 일반적인 import 구문.
4.  **공통 기능 및 속성 (선택 사항)**: 그룹 내 여러 컴포넌트가 공유하는 기능, 프로퍼티, 메소드, 시그널 설명.
5.  **개별 컴포넌트 섹션**: `## [컴포넌트 이름]`
    *   **설명**: 컴포넌트의 역할과 특징.
    *   **주요 상속 프로퍼티/시그널 (선택 사항)**: 기반 클래스로부터 상속받는 중요한 멤버 목록.
    *   **고유/특징적 프로퍼티**: 해당 컴포넌트만의 프로퍼티 또는 동작 방식이 특별한 프로퍼티.
    *   **고유 메소드**: 해당 컴포넌트만의 메소드.
    *   **고유 시그널**: 해당 컴포넌트만의 시그널.
    *   **예제**: 간단한 사용 예시 코드.
    *   **참고 사항**: 주의할 점이나 추가 정보.

### 테이블 형식

문서 내 프로퍼티, 메소드, 시그널 정보는 다음 테이블 형식을 사용합니다.

**프로퍼티 테이블:**

| 이름     | 타입     | 기본값 | 설명           |
| :------- | :------- | :----- | :------------- |
| `propName` | `propType` | `값`   | 프로퍼티 설명. |

**메소드 테이블:**

| 이름         | 파라미터                   | 반환타입     | 설명         |
| :----------- | :------------------------- | :----------- | :----------- |
| `methodName` | `paramType`: `paramName` | `returnType` | 메소드 설명. |

**시그널 테이블:**

| 이름         | 파라미터                   | 반환타입 | 설명         |
| :----------- | :------------------------- | :------- | :----------- |
| `signalName` | `paramType`: `paramName` | -        | 시그널 설명. |
