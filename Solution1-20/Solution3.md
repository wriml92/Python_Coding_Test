```python
def solution(num1, num2):
    # 두 개의 숫자 num1과 num2를 받아서
    # num1을 num2로 나눈 몫을 정수로 반환
    return num1 // num2
```

&emsp;이 코드는 두 숫자를 입력받아 첫 번째 숫자를 두 번째 숫자로 나눈 **정수 몫**을 계산하여 반환하는 함수이다.

---

### 함수 설명:

- **함수 정의**: `def solution(num1, num2):`
  - `solution`이라는 이름의 함수를 정의한다.
  - 두 개의 매개변수 `num1`과 `num2`를 받는다.

- **연산 및 반환**: `return num1 // num2`
  - `num1`을 `num2`로 나눈 뒤, 그 결과의 **정수 몫**을 계산한다.
  - 계산된 정수 값을 반환한다.
  - 이 연산은 **정수 나눗셈 연산자** `//`를 사용한다.

---

### 사용 예시:

```python
result = solution(10, 3)
print(result)  # 출력: 3
```

- 위 예시에서 `solution(10, 3)`을 호출하면 `10 // 3`의 결과인 정수 `3`을 반환한다.

---

### 상세 설명:

- **입력받는 값**:
  - `num1`: 나눗셈 연산에서 피제수(나뉘는 숫자).
  - `num2`: 나눗셈 연산에서 제수(나누는 숫자).

- **처리 과정**:
  - 함수는 `num1`을 `num2`로 나눈다.
  - 정수 나눗셈 연산자 `//`를 사용하여 결과를 **소수점 아래를 버린 정수 값**으로 만든다.
  - 예를 들어, `7 // 2`는 `3`이 된다. (소수점 이하 버림)

- **결과 반환**:
  - 계산된 정수 몫을 `return` 키워드를 통해 반환한다.

---

### 주의사항:

1. **`num2`가 0일 경우**:
   - 나눗셈 연산에서 제수가 0이면 오류가 발생한다.
   - 이러한 상황에서는 에러 처리가 필요할 수 있다. 예를 들어:
     ```python
     if num2 == 0:
         raise ValueError("제수는 0일 수 없습니다.")
     ```

---

### 함수의 목적:

- 두 숫자를 나눈 뒤, 결과의 **정수 몫**을 구하는 작업을 쉽게 처리한다.
- 코드의 재사용성과 간결성을 높여준다.