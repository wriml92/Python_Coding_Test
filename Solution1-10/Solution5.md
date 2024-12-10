```python
def solution(num1, num2):
    # 두 개의 숫자 num1과 num2를 비교하여
    # 두 숫자가 같으면 1을 반환하고, 다르면 -1을 반환
    return 1 if num1 == num2 else -1
```

&emsp;이 코드는 두 숫자를 비교하여 같으면 `1`, 다르면 `-1`을 반환하는 함수이다. **삼항 연산자**를 활용하여 간결하게 작성된 비교 로직이다.

---

### 함수 설명:

- **함수 정의**: `def solution(num1, num2):`
  - `solution`이라는 이름의 함수를 정의한다.
  - 두 개의 매개변수 `num1`과 `num2`를 받는다.
  - 이 매개변수들은 비교 대상이 되는 두 숫자를 나타낸다.

- **삼항 연산자**: `1 if num1 == num2 else -1`
  - `num1`과 `num2`가 **같은지(`==`)** 비교한다.
  - 같으면 `1`을 반환하고, 그렇지 않으면 `-1`을 반환한다.

---

### 사용 예시:

```python
result1 = solution(10, 10)
print(result1)  # 출력: 1 (두 숫자가 같음)

result2 = solution(5, 3)
print(result2)  # 출력: -1 (두 숫자가 다름)
```

- 첫 번째 예에서는 `num1`과 `num2`가 같으므로 `1`이 반환된다.
- 두 번째 예에서는 `num1`과 `num2`가 다르므로 `-1`이 반환된다.

---

### 상세 설명:

1. **입력받는 값**:
   - `num1`: 비교할 첫 번째 숫자.
   - `num2`: 비교할 두 번째 숫자.

2. **처리 과정**:
   - `num1 == num2`: 두 숫자가 같은지 확인하는 비교 연산자이다.
   - **같을 경우**: `1` 반환.
   - **다를 경우**: `-1` 반환.

3. **결과 반환**:
   - 삼항 연산자의 결과(`1` 또는 `-1`)를 `return` 키워드를 통해 반환한다.

---

### 장점:

- **간결한 코드**: 삼항 연산자를 사용하여 조건문을 간략하게 작성.
- **빠른 비교**: 두 숫자를 간단히 비교하여 원하는 값을 반환.

---

### 함수의 목적:

- 두 숫자가 같은지 확인하고, 그 결과를 `1` 또는 `-1`로 간단히 표현.
- 조건에 따라 다른 값을 반환해야 할 때 유용한 패턴 제공.