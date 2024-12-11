```python
def solution(age):
    # 사용자의 나이를 입력받아
    # 사용자가 태어난 출생 연도를 계산하여 반환
    # 현재 연도는 2022년으로 고정
    return (2022 - age) + 1
```

&emsp;이 코드는 입력된 나이를 기준으로 **사용자의 출생 연도**를 계산하는 함수이다. 현재 연도를 **2022**로 고정하여 계산한다.

---

### 함수 설명:

- **함수 정의**: `def solution(age):`
  - `solution`이라는 이름의 함수를 정의한다.
  - 하나의 매개변수 `age`를 받는다.
  - `age`는 사용자의 나이를 의미한다.

- **연산 및 반환**: `return (2022 - age) + 1`
  - `2022 - age`를 계산하여 사용자의 태어난 연도를 구한다.
  - 태어난 연도를 계산할 때, 한국식 나이 계산을 반영하여 **+1**을 추가한다.

---

### 사용 예시:

```python
result = solution(25)
print(result)  # 출력: 1998
```

- `solution(25)`은 나이가 25인 사람의 출생 연도를 계산한다.
- `2022 - 25 = 1997`이고, 한국식 계산에서 출생 연도에 1을 더하여 `1998`을 반환한다.

---

### 상세 설명:

- **입력받는 값**:
  - `age`: 사용자의 현재 나이. (한국식 나이 또는 만 나이 기준에 따라 결과가 다를 수 있음)

- **처리 과정**:
  1. 현재 연도(2022)에서 사용자의 나이를 뺀다.
  2. 한국식 나이 계산법(출생 시 1살 추가)을 반영하기 위해 결과에 **+1**을 더한다.

- **결과 반환**:
  - 계산된 출생 연도를 `return` 키워드를 통해 반환한다.

---

### 주의사항:

1. **현재 연도 고정**:
   - 코드에서 현재 연도를 **2022**로 고정하였기 때문에 미래나 과거의 연도를 기준으로 동작하려면 이를 수정해야 한다.
   - 동적으로 현재 연도를 구하려면 `datetime` 모듈을 사용할 수 있다:
     ```python
     from datetime import datetime
     current_year = datetime.now().year
     return (current_year - age) + 1
     ```

2. **나이 기준**:
   - 입력된 나이가 만 나이인지, 한국식 나이인지 명확히 정의해야 한다.
   - 위 코드는 한국식 나이 계산법을 가정한다.

---

### 함수의 목적:

- 사용자의 나이를 입력하면 출생 연도를 빠르게 계산한다.
- 한국식 나이 계산법을 기반으로 결과를 제공한다.