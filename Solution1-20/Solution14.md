```python
def solution(n):
    # 초기값을 0으로 설정하여 약수의 합을 저장할 변수 answer를 생성
    answer = 0
    # 1부터 n까지 반복하면서 i가 n의 약수인지 확인
    for i in range(1, n + 1):
        if n % i == 0:  # n을 i로 나누었을 때 나머지가 0이면 i는 n의 약수
            answer += i  # 약수인 i를 answer에 더하기
    # 모든 약수를 더한 결과를 반환
    return answer
```

---

### 함수 설명:

&emsp;이 코드는 입력된 정수 `n`의 **모든 약수의 합**을 계산하여 반환하는 함수이다. 약수는 `n`을 나누었을 때 나머지가 0인 수이다.

---

### 상세 설명:

1. **변수 초기화**:
   - `answer = 0`: 약수의 합을 저장할 변수 `answer`를 0으로 초기화한다.

2. **반복문**:
   - `for i in range(1, n + 1)`:
     - 1부터 `n`까지의 숫자 `i`를 순회한다.
   - `if n % i == 0`:
     - `i`가 `n`의 약수인지 확인한다. 약수는 `n % i == 0` 조건을 만족하는 숫자이다.
   - `answer += i`:
     - 약수로 확인된 `i`를 `answer`에 더한다.

3. **결과 반환**:
   - 반복문이 끝난 뒤, `answer`에는 모든 약수의 합이 저장되어 있다.
   - `return answer`을 통해 최종 약수의 합을 반환한다.

---

### 사용 예시:

```python
result1 = solution(6)
print(result1)  # 출력: 12 (1 + 2 + 3 + 6)

result2 = solution(10)
print(result2)  # 출력: 18 (1 + 2 + 5 + 10)
```

- **첫 번째 예시**:
  - `n = 6`의 약수는 `1, 2, 3, 6`입니다. 이들의 합은 `12`이다.
- **두 번째 예시**:
  - `n = 10`의 약수는 `1, 2, 5, 10`입니다. 이들의 합은 `18`이다.

---

### 함수의 목적:

- 입력된 정수의 모든 약수를 찾아 합산한다.
- 약수의 성질을 활용한 계산을 수행한다.

---

### 장점:

1. **단순하고 명확한 로직**:
   - 반복문과 조건문을 통해 약수를 직접 확인하므로 이해하기 쉽다.
2. **재사용성**:
   - 다양한 입력값에 대해 약수의 합을 계산할 수 있다.

---

### 효율성:

- 반복문이 `1`부터 `n`까지 실행되므로 시간 복잡도는 \(O(n)\)이다.
- 큰 `n`에 대해 효율성을 높이려면 약수는 대칭성을 가진다는 점을 이용해 \(1\)부터 \(\sqrt{n}\)까지만 확인할 수 있다:
  ```python
  def solution(n):
      answer = 0
      for i in range(1, int(n**0.5) + 1):
          if n % i == 0:
              answer += i  # 작은 약수 추가
              if i != n // i:  # i와 짝이 되는 약수가 다른 경우 추가
                  answer += n // i
      return answer
  ```

---

### 확장 가능성:

- 특정 조건(예: 짝수 약수만 합산)을 추가할 수 있다:
  ```python
  def solution_even_divisors(n):
      answer = 0
      for i in range(1, n + 1):
          if n % i == 0 and i % 2 == 0:
              answer += i
      return answer
  ```