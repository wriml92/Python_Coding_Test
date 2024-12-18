```python
def solution(n):
    # 입력된 숫자 n을 문자열로 변환한 뒤,
    # 문자열을 reversed() 함수로 뒤집기
    # 뒤집어진 문자열의 각 문자를 int로 변환하여 리스트로 반환
    return list(map(int, reversed(str(n))))
```

&emsp;이 코드는 입력된 숫자 `n`을 **각 자리 숫자로 나누어 뒤집은 리스트**를 반환하는 함수이다.

---

### 함수 설명:

1. **`str(n)`**:
   - 입력된 숫자 `n`을 문자열로 변환한다.
   - 예: `12345` → `"12345"`.

2. **`reversed(str(n))`**:
   - 문자열을 뒤집는다.
   - 예: `"12345"` → `"54321"`.
   - `reversed()` 함수는 문자열을 뒤집은 결과를 반환한다.

3. **`map(int, reversed(str(n)))`**:
   - 뒤집어진 문자열의 각 문자를 정수(`int`)로 변환한다.
   - 예: `"54321"` → `[5, 4, 3, 2, 1]`.

4. **`list(map(...))`**:
   - `map` 객체를 리스트로 변환하여 반환한다.

---

### 사용 예시:

```python
result1 = solution(12345)
print(result1)  # 출력: [5, 4, 3, 2, 1]

result2 = solution(9876)
print(result2)  # 출력: [6, 7, 8, 9]
```

- **첫 번째 예시**:
  - `n = 12345`일 때:
    - `str(n)` → `"12345"`.
    - `reversed("12345")` → `"54321"`.
    - `map(int, ...)` → `[5, 4, 3, 2, 1]`.
    - `list(...)` → `[5, 4, 3, 2, 1]`.
- **두 번째 예시**:
  - `n = 9876`일 때:
    - 동일한 과정으로 `[6, 7, 8, 9]` 반환한다.

---

### 상세 설명:

1. **입력받는 값**:
   - `n`: 각 자리 숫자를 뒤집고자 하는 정수이다.

2. **처리 과정**:
   - **변환 및 뒤집기**:
     - `str(n)`으로 숫자를 문자열로 변환한다.
     - `reversed(...)`로 문자열을 뒤집는다.
   - **숫자 변환**:
     - `map(int, ...)`를 통해 각 문자를 정수로 변환한다.
   - **리스트로 반환**:
     - `list(...)`를 사용하여 최종적으로 리스트를 생성한다.

3. **결과 반환**:
   - 뒤집힌 각 자리 숫자를 정수로 변환한 리스트를 반환한다.

---

### 함수의 목적:

- 입력된 숫자의 각 자리 숫자를 뒤집은 순서대로 리스트 형태로 반환한다.
- 문자열 변환과 리스트 변환을 활용해 간단하고 효율적으로 구현한다.

---

### 장점:

1. **간결한 코드**:
   - `str`, `reversed`, `map` 등의 내장 함수를 사용해 반복문 없이 구현하였다.
2. **효율성**:
   - Python 내장 함수는 최적화되어 있어 빠른 처리가 가능하다.

---

### 주의사항:

1. **`n`이 음수일 경우**:
   - 음수는 문자열 변환 시 `-` 기호가 포함된다.
   - 음수 처리 로직을 추가하거나, 절댓값으로 변환 후 처리해야 한다:
     ```python
     n = abs(n)
     ```

2. **입력값 유형**:
   - `n`이 정수가 아닌 경우 오류가 발생할 수 있다. 이 경우 입력에 대한 검증을 추가해야 한다:
     ```python
     if not isinstance(n, int):
         raise ValueError("n은 정수여야 합니다.")
     ```

---

### 확장 가능성:

- 각 자리 숫자를 합산하거나 곱셈 연산을 수행하려면 다음과 같이 수정해야 한다:
  ```python
  def sum_of_digits(n):
      return sum(map(int, reversed(str(n))))
  ```

- 음수 처리 및 비정수 입력에 대한 확장도 고려할 필요가 있다.