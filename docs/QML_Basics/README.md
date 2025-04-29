# QML 기본 타입 및 컴포넌트

이 문서는 PySide6 애플리케이션 개발, 특히 Fluent UI 라이브러리 활용에 필요한 Qt Quick (QML)의 기본적인 타입, 컴포넌트, 그리고 핵심 개념을 설명합니다.

Fluent UI 컴포넌트는 QML의 기본 요소들을 기반으로 확장되거나 함께 사용되는 경우가 많으므로, 이 기본 지식을 이해하는 것은 Fluent UI를 효과적으로 사용하는 데 중요합니다.

## 문서 구조

문서는 기능별/모듈별 카테고리로 분류되어 있으며, 각 카테고리 폴더에는 관련된 개념이나 컴포넌트에 대한 개별 `.md` 파일이 포함됩니다.

*   **[01_Core_Concepts](./01_Core_Concepts/README.md)**: QML 언어의 핵심 개념 (데이터 타입, 속성 바인딩, 시그널/슬롯, JS 통합).
*   **[02_Basic_Elements](./02_Basic_Elements/README.md)**: 기본적인 시각적 빌딩 블록 (`Item`, `Rectangle`, `Text`, `Image` 등 - `QtQuick` 모듈).
*   **[03_Layouts](./03_Layouts/README.md)**: UI 요소 배치 및 정렬 (`RowLayout`, `ColumnLayout`, `GridLayout` 등 - `QtQuick.Layouts` 모듈).
*   **[04_Input_Handling](./04_Input_Handling/README.md)**: 사용자 입력 처리 (`MouseArea`, `Keys` 등 - `QtQuick` 모듈).
*   **[05_QtQuick_Controls](./05_QtQuick_Controls/README.md)**: 기본적인 UI 컨트롤 (`Button`, `TextField`, `CheckBox` 등 - `QtQuick.Controls` 모듈).
*   **[06_Views_Models](./06_Views_Models/README.md)**: 데이터 목록 표시를 위한 모델-뷰 시스템 (`ListModel`, `ListView` 등 - `QtQuick`, `QtQuick.Controls` 모듈).
*   **[07_Windows_Dialogs](./07_Windows_Dialogs/README.md)**: 최상위 창 및 기본 대화상자 (`Window`, `Dialog` 등 - `QtQuick.Window`, `QtQuick.Controls`, `QtQuick.Dialogs` 모듈).
*   **[08_States_Transitions_Animations](./08_States_Transitions_Animations/README.md)**: 동적인 UI 상태 변화 및 시각 효과 (`State`, `Transition`, `Animation` 등 - `QtQuick` 모듈).
*   **[09_Advanced_Topics](./09_Advanced_Topics/README.md)**: 동적 컴포넌트 로딩, 백그라운드 작업 등 (`Component`, `Loader`, `WorkerScript` 등 - `QtQuick`, `QtQml` 모듈).

각 카테고리 폴더 안에는 해당 카테고리의 개요를 설명하는 `README.md` 파일이 포함될 수 있습니다.

## 문서 형식 가이드

각 QML 개념 또는 컴포넌트 문서는 다음 형식을 따릅니다.

1.  **제목**: `# [개념 또는 컴포넌트 이름]` (예: `# Rectangle`, `# 프로퍼티 바인딩`)
2.  **모듈 정보 (컴포넌트의 경우)**: 해당 컴포넌트를 사용하기 위해 필요한 `import` 구문 명시.
3.  **개요**: 해당 개념 또는 컴포넌트의 역할과 주요 특징에 대한 간략한 설명.
4.  **기반 클래스 (컴포넌트의 경우, 선택 사항)**: 상속받는 주요 기반 클래스 언급.
5.  **주요 프로퍼티 (컴포넌트의 경우)**: 컴포넌트의 중요하거나 자주 사용되는 프로퍼티 설명. (테이블 형식 사용)
6.  **주요 시그널 (컴포넌트의 경우)**: 자주 사용되는 시그널 설명. (테이블 형식 사용)
7.  **주요 메소드 (컴포넌트의 경우, 선택 사항)**: 주요 메소드 설명. (테이블 형식 사용)
8.  **상세 설명 (개념의 경우)**: 개념에 대한 더 자세한 설명 및 예시.
9.  **예제**: 간단하고 명확한 QML 코드 사용 예시.
10. **참고 사항**: 관련 개념, 주의할 점, 추가 정보 등.

### 테이블 형식

문서 내 프로퍼티, 메소드, 시그널 정보는 다음 테이블 형식을 사용합니다. (Fluent UI 문서 형식과 동일)

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

이 README는 QML 기본 문서화 작업을 진행하면서 필요에 따라 수정될 수 있습니다. 